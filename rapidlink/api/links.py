from flask import request
from flask_jwt_extended import jwt_required
from rapidlink.api import api
from rapidlink.helpers import response, regx
from rapidlink.controllers import links_controller


@api.route("/links", methods=["GET"])
@jwt_required()
def get_links():
    return "get_links"


@api.route("/links", methods=["POST"])
@jwt_required()
def create_link():
    # 链接类型: 短信/邮件/电话
    # 可选值: sms/email/phone
    type = request.form.get("type")

    # 链接值: 手机号/邮箱/短信
    value = request.form.get("value")

    if not type or type not in ["sms", "email", "phone"]:
        return response.ResponseClass.bad_request(
            message="Invalid type"
        )
    
    # 如果是短信或电话, 则需要验证值是否为手机号
    if (type == "sms" or type == "phone") and (not value or not regx.is_phone(value)):
        return response.ResponseClass.bad_request(
            message="Invalid phone number"
        )
    # 如果是邮件, 则需要验证值是否为邮箱
    if type == "email" and (not value or not regx.is_email(value)):
        return response.ResponseClass.bad_request(
            message="Invalid email address"
        )
    return links_controller.create_link(type, value)


@api.route("/links/<linkid>", methods=["GET"])
def get_link(linkid):
    if not linkid:
        return response.ResponseClass.bad_request(
            message="Invalid linkid", data={"linkid": linkid}
        )
    return links_controller.get_link(linkid)
