from flask import jsonify


class ResponseClass(object):
    def __init__(self, status_code, message, data=None, success=True, reason=None, bs_code=None):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.reason = reason
        self.success = success
        self.bs_code = bs_code

    @classmethod
    def bad_request(cls, message="Bad Request", reason=None, bs_code=None):
        res = cls(400, message, reason=reason, success=False, bs_code=bs_code)
        return res.to_json()

    @classmethod
    def not_found(cls, message="Not Fount", reason=None, bs_code=None):
        return cls(
            404, message, reason=reason, success=False, bs_code=bs_code
        ).to_json()

    @classmethod
    def success(cls, message="", data=None, bs_code=None):
        return cls(200, message, data=data, success=True, bs_code=bs_code).to_json()

    @classmethod
    def error(cls, message="Unkonw Error", data=None, bs_code=None):
        return cls(500, message, data=data, success=False, bs_code=bs_code).to_json()

    def to_json(self):
        return jsonify(
            {
                "code": self.status_code,
                "message": self.message,
                "data": self.data,
                "success": self.success,
                "reason": self.reason,
                "bs_code": self.bs_code,
            }
        )
