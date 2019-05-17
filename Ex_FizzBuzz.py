def fizz_buzz(input) -> int:
    rem_3 = input % 3
    rem_5 = input % 5
    if (not rem_3) and (not rem_5):
        return("FizzBuzz")
    elif (not rem_3):
        return("Fizz")
    elif (not rem_5):
        return("Buzz")
    else:
        return(input)


x = input("Enter an integer: ")
print(fizz_buzz(int(x)))
