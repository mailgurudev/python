enter_input = input("Write something that you want to see in reverse")

def string_reverse(enter_input):
    result = enter_input.split ( " " )
    new_result = [ ]
    for i in reversed ( result ):
        new_result.append ( i )
        final_result = " ".join ( new_result )