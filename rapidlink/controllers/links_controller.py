from rapidlink.helpers import id, response
from rapidlink.database.links_database import links_db


def create_link(type,value):
    linkid = id.gen_uuid()
    try:
        link = links_db.insert(
            linkid=linkid,
            type=type,
            value=value,
        )
        return response.ResponseClass.success(message="Link created", data={"linkid": linkid})
    except Exception:
        return response.ResponseClass.error(
            message="Failed to create link",
        )


def get_link(linkid):
    try:
        link = links_db.get(linkid=linkid)
        if not link:
            return response.ResponseClass.not_found(
                message="Link not found",
                data={"linkid": linkid},
            )
        return response.ResponseClass.success(message="Link found", data=link)
    except Exception as e:
        return response.ResponseClass.error(
            message="Failed to get link",
            reason=str(e),
        )


def update_link(linkid, title, description, expires_in, content, value, type):
    try:
        link = links_db.update(
            linkid=linkid,
            title=title,
            description=description,
            expires_in=expires_in,
            content=content,
            value=value,
            type=type,
        )
        if not link:
            return response.ResponseClass.not_found(
                message="Link not found",
                data={"linkid": linkid},
            )
        return response.ResponseClass.success(message="Link updated", data=link)
    except Exception as e:
        return response.ResponseClass.error(
            message="Failed to update link",
            reason=str(e),
        )


def delete_link(linkid):
    try:
        link = links_db.delete(linkid=linkid)
        if not link:
            return response.ResponseClass.not_found(
                message="Link not found",
                data={"linkid": linkid},
            )
        return response.ResponseClass.success(message="Link deleted", data=link)
    except Exception as e:
        return response.ResponseClass.error(
            message="Failed to delete link",
            reason=str(e),
        )
