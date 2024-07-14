# outside function with is what gets called using the @
def make_bold(func):
    # wrapper function which is the body where a function is executed

    def wrapper():

# function converted into a variable
        text = func()
# here we are able to add into the string which was returned by the function
        text = f"<b>{text}<b>"

        return text
    # !! wrapper when returned ALWAYS WITHOUT ()
    return wrapper
# text and wrapper are returned when the decorator is called 
def make_italic(func):
    def wrapper():

        text = func()

        text = f"<em>{text}<em>"
        return text
    return wrapper
def make_underline(func):
    def wrapper():

        text = func()

        text = f"<u>{text}<u>"
        return text
    return wrapper

