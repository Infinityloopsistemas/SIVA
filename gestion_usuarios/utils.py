def is_allowed_edit(user):
    if user:
        return (user.groups.filter(name='administradores').count() > 0) or (user.groups.filter(name='veterinarios').count() > 0)
    return False
def is_allowed_see(user):
    if user:
        return (user.groups.filter(name='administradores').count() > 0) or (user.groups.filter(name='veterinarios').count() > 0) or (user.groups.filter(name='responsables').count() > 0) or (user.groups.filter(name='coordinadores').count() > 0)
    return False