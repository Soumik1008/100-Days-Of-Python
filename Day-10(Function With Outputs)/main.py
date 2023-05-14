def format_name(first_name,last_name):
    """
    Takes the first and last name and ormats it to the title case version
    of the string
    """
    if first_name=="" and last_name=="":
        return "No name to return"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Result: {formatted_first_name} {formatted_last_name}"

print(format_name(input("What is your first name?"),input("What is your last name?")))