def fizzBuzz():

    while True:
        print("Fizz Buzz Game")
        number =int(input("enter the number"))
        if number % 5 == 0 and number % 3 == 0 :
            print("Fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            break

fizzBuzz()