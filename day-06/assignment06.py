def get_active_users(users):
    active_users = [user for user in users if user["active"]]
    return active_users