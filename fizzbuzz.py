# Div by 3 and 5

# 3 : fizz
# 5 : buzz
# 7 : foo
# 11 : bar

def fizzbuzz():
    for i in range(1, 101):
        if (i % 5 ) == 0 and (i % 3) == 0:
            print ("fizzbuzz")
        elif (i % 3) == 0:
            print ("fizz")
        elif (i % 5 ) == 0:
            print ("buzz")
        else:
            print(i)


fizzbuzz()