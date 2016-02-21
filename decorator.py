from my_decorator import my_decorator

# @my_decorator is same as just_some_function = my_decorator(just_some_function)
#

@my_decorator
def just_some_function():
    print("Whee")

just_some_function()    
