def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_full_name2(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("John", "Smith"))
print(get_full_name2("John", "Smith"))
