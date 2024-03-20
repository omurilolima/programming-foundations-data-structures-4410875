user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    # new_pref = {}
    # for key, value in user_pref.items():
    #     if user_pref[key] is not None:
    #         new_pref[key] = value
    # return new_pref
    return {key: value for key, value in user_pref.items() if value is not None}


print(update_preferences(user_preferences))
