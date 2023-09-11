
fname = input("What is your first name?:")
lname = input("What is your last name?:")

#function with outputs
def format_name(f_name,l_name):
    #docstrings
    """Take a first name and last name and format it to return to a title case version of the name. """
    if f_name == '' or l_name == '':
        return "No inputs were provided."
    name1 = f_name.title()
    name2 = l_name.title()
    return f'Results: {name1} {name2}'
    
print(format_name(fname,lname))   
