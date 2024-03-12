# resources for a number tester

def convert(string):
    number = float(string)
    if number % 1 == 0:
        return int(number)
    else:
        return number


def divisors(test_number):
    return [_ for _ in range(1, test_number) if test_number % _ == 0]


def even_odd_test(test_number):
    if test_number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def neg_pos_test(test_number):
    string = str(test_number)
    if string[0] == "-":
        return "Negative"
    else:
        return "Positive"


def prime_test(divisor_list):
    if len(divisor_list) == 1:
        return "Prime"
    else:
        return "Not Prime"


def square_cube_test(test_number, divisor_list):
    for divisor in divisor_list:
        if divisor ** 2 == test_number:
            return "Perfect Square"
        if divisor ** 3 == test_number:
            return "Perfect Cube"
    return "Neither"


def perfect_deficient_abundant(test_number, divisor_list):
    if sum(divisor_list) == test_number:
        return "Perfect"
    elif sum(divisor_list) > test_number:
        return "Abundant"
    else:
        return "Deficient"


def triangular_test(test_number):
    next_add = 1
    sum_check = 0
    for _ in range(test_number + 1):
        if test_number == sum_check:
            return "Triangular"
        else:
            sum_check += next_add
            next_add += 1
    return "Not Triangular"


def fibonacci_test(test_number):
    binet_number1 = ((test_number ** 2) * 5) + 4
    binet_number2 = ((test_number ** 2) * 5) - 4
    binet_divisors1 = divisors(binet_number1)
    binet_divisors2 = divisors(binet_number2)
    if (square_cube_test(binet_number1, binet_divisors1) == "Perfect Square" or
            square_cube_test(binet_number2, binet_divisors2) == "Perfect Square"):
        return "a Fibonacci Number"
    else:
        return "Not a Fibonacci Number"

