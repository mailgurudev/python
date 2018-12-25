a = [ 1, 2, 3, 4, 5, 6, 7 ]
d = 5

b = [ ]
c = [ ]
for i in a:
    if i <= d:
        b.append ( i )
    else:
        c.append ( i )

final_list = c + b
print ( final_list )
