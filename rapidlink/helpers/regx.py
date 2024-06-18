import re


def is_phone(value):
    return re.match(r"^1[3-9]\d{9}$", value)


def is_email(value):
    return re.match(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", value)
