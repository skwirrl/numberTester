# resources for a number tester

def convert(string):
    number = float(string)
    if number % 1 == 0:
        return int(number)
    else:
        return number


def divisors(test_number):
    return [i for i in range(1, test_number) if test_number % i == 0]


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


def square_test(test_number, divisor_list):
    for divisor in divisor_list:
        if divisor ** 2 == test_number:
            return "Perfect Square"
    else:
        return False


def perfect_deficient_abundant(test_number, divisor_list):
    if sum(divisor_list) == test_number:
        return "Perfect"
    elif sum(divisor_list) > test_number:
        return "Abundant"
    else:
        return "Deficient"

