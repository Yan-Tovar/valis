from functools import wraps

from auth.guards import Guards


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        Guards.auth_required()

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        Guards.admin_required()

        return func(*args, **kwargs)

    return wrapper