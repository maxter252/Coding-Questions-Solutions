# Div by 3 and 5

# 3 : fizz
# 5 : buzz
# 7 : foo
# 11 : bar

def fizzbuzzSimple():
    for i in range(1, 101):
        if (i % 5 ) == 0 and (i % 3) == 0:
            print ("fizzbuzz")
        elif (i % 3) == 0:
            print ("fizz")
        elif (i % 5 ) == 0:
            print ("buzz")
        else:
            print(i)

# fizzbuzzSimple()

def fizzbuzzParam(n, conditions):
    for i in range(1, 101):
        output = ''
        for condition in conditions:
            if (i % condition[1]) == 0:
                output += condition[0]
        print(i, output)


# fizzbuzzParam(100, [("fizz",3),("buzz",5)])

def fizzbuzzwizz(n, conditions):
    for i in range(1, 101):
        output = ''
        for condition in conditions:
            if condition[1](i):
                output += condition[0]
        print(i, output)

fizzbuzzwizz(100, [
    ("fizz",lambda a : (a % 3) == 0),
    ("buzz",lambda a : (a % 5) == 0),
    ("wizz",lambda a : a > 90)
    ])