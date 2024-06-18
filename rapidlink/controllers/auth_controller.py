from rapidlink.helpers import response
from flask_jwt_extended import create_access_token
from rapidlink.database.user_datebase import user_db
from rapidlink.helpers import id


def login(username, password):
    user = user_db.get(username=username)
    if not user:
        return response.ResponseClass.bad_request(
            message="User not found",
            data={"username": username},
        )

    password = id.sha256(password)
    if password != user["password"]:
        return response.ResponseClass.bad_request(
            message="User or password is incorrect",
            data={"username": username},
        )

    if user["password"] != password:
        return response.ResponseClass.bad_request(
            message="User or password is incorrect",
            data={"username": username},
        )

    access_token = create_access_token(username)
    return response.ResponseClass.success(
        message="Login successful",
        data={
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": 15 * 60,  # 15 minutes
            "user": {
                "username": user["username"],
                "userid": user["userid"],
                "status": user["status"],
            },
        },
    )


def signup(username, password):
    user = user_db.get(username=username)
    if user:
        return response.ResponseClass.bad_request(
            message="User already exists. If this is your account, please log in directly.",
            data={"username": username},
        )
    try:
        user = user_db.insert(
            userid=id.gen_uuid(), username=username, password=id.sha256(password)
        )
        return response.ResponseClass.success(
            message="User created successfully",
            data={
                "username": user["username"],
                "userid": user["userid"],
                "status": user["status"],
            },
        )
    except Exception as e:
        return response.ResponseClass.error(
            message="Failed to create user",
            data={"username": username},
            reason=str(e),
        )
