
def listify(f):
    def wrapper(*args, **kwargs):
        return list(f(*args, **kwargs))
    return wrapper
