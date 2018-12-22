def num_reverse(number):
    number = input ( "Enter the number : " )
    result = number.split ( " " )
    new_result = [ ]
    for i in reversed ( result ):
        new_result.append ( i )
        final_result = " ".join ( new_result )
