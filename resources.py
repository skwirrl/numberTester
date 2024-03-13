# resources for a number tester

def convert(string):
    number = float(string)
    if number % 1 == 0:
        return int(number)
    else:
        return number


def divisors(test_number):
    return [_ for _ in range(1, test_number) if test_number % _ == 0]


def digits(test_number):
    return [int(ch) for ch in str(test_number).strip("-")]


def even_odd_test(test_number):
    if test_number % 2 == 0:
        return "is even"
    else:
        return "is odd"


def neg_pos_test(test_number):
    string = str(test_number)
    if string[0] == "-":
        return "is negative"
    else:
        return "is positive"


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
            return "is a triangular number"
        else:
            sum_check += next_add
            next_add += 1
    return "not a triangular number"


def fibonacci_test(test_number):
    binet_number1 = ((test_number ** 2) * 5) + 4
    binet_number2 = ((test_number ** 2) * 5) - 4
    binet_divisors1 = divisors(binet_number1)
    binet_divisors2 = divisors(binet_number2)
    if (square_cube_test(binet_number1, binet_divisors1) == "Perfect Square" or
            square_cube_test(binet_number2, binet_divisors2) == "Perfect Square"):
        return "a Fibonacci number"
    else:
        return "not a Fibonacci number"


def palindrome_test(digit_list):
    reversed_list = digit_list[::-1]
    if digit_list == reversed_list:
        return "a palindromic number"
    else:
        return "not a palindromic number"


def armstrong_test(test_number, digit_list):
    exponent = len(digit_list)
    armstrong_list = [i ** exponent for i in digit_list]
    if sum(armstrong_list) == test_number:
        return "an Armstrong number"
    else:
        return "not an Armstrong number"


def automorphic_test(test_number, digit_list):
    square = test_number ** 2
    square_digit_list = digits(square)
    while len(square_digit_list) > len(digit_list):
        del square_digit_list[0]
    if square_digit_list == digit_list:
        return "an automorphic number"
    else:
        return "not an automorphic number"
