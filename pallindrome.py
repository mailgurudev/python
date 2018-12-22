number = input ( "Enter number : " )

print ( reversed ( number ) )


def palindrome(number):
    if str ( number ) == reversed ( str ( number ) ):
        print ( "This is a palindrome" )
    else:
        print ( "This is not a a palindrome" )


palindrome ( number )
