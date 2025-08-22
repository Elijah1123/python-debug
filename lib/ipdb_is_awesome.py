import ipdb

def tracking_the_function():
    inside_the_function = "we're inside the function"
    print("We're about to stop because of ipdb!")
    ipdb.set_trace()
    this_variable_hasnt_been_interpreted_yet = \
    "The Program froze before it could read me !"
    print(this_variable_hasnt_been_interpreted_yet)

tracking_the_function()    
