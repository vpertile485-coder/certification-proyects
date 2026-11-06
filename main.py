def add_setting(settings, key_values):
    key, value = key_values
    key = key.lower()
    value = value.lower()
    if key in settings: 
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else: 
       settings[key] = value
       return(f"Setting '{key}' added with value '{value}' successfully!")
test_settings = {"language": "spanish"}

result = add_setting(test_settings, ("Theme", "DARK"))

print(result)
print(test_settings)

def update_setting(settings, key_values):
    key, value = key_values
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
test_settings = {"theme": "dark", "language": "spanish"}

result = update_setting(test_settings, ("THEME", "LIGHT"))
print(result)
print(test_settings)

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return(f"Setting '{key}' deleted successfully!")
    else: 
       return(f'Setting not found!')
test_settings = {"theme": "dark", "language": "spanish"}

result = delete_setting(test_settings, "THEME")
print(result)
print(test_settings)

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result 

test_settings = {"language": "spanish"}
print(view_settings(test_settings))

print(view_settings({}))

test_settings = {"language": "spanish"}

print(add_setting(test_settings, ("LANGUAGE", "ENGLISH")))
print(test_settings)

test_settings = {"language": "spanish"}

print(update_setting(test_settings, ("theme", "dark")))

test_settings = {"language": "spanish"}

print(delete_setting(test_settings, "theme"))
