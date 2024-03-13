class TestNumber:
    def __init__(self, value):
        self.value = value
        self.digits = self.digit_list()
        self.divisors = self.divisor_list()
        self.is_even = self.even_test()
        self.is_odd = self.odd_test()
        self.is_negative= self.neg_test()
        self.is_positive = self.pos_test()
        self.is_prime = self.prime_test()
        self.is_perfect_square = self.square_test()
        self.is_perfect_cube = self.cube_test()
        self.is_perfect = self.perfect_test()
        self.is_abundant = self.abundant_test()
        self.is_deficient = self.deficient_test()
        self.is_fibonacci = self.fibonacci_test()
        self.is_palindrome = self.palindrome_test()
        self.is_armstrong_number = self.armstrong_test()
        self.is_automorphic = self.automorphic_test()



    def digit_list(self):
        return [int(ch) for ch in str(self.value).strip("-")]

    def divisor_list(self):
        return [i for i in range(1, self.value) if self.value % i == 0]

    def even_test(self):
        return self.value % 2 == 0

    def odd_test(self):
        return not self.is_even

    def neg_test(self):
        string = str(self.value)
        if string[0] == "-":
            return True
        else:
            return False

    def pos_test(self):
        if self.value == 0:
            return False
        if not self.is_negative:
            return True
        else:
            return False

    def prime_test(self):
        if len(self.divisors) == 1:
            return True
        else:
            return False

    def square_test(self):
        for divisor in self.divisors:
            if divisor ** 2 == self.value:
                return True
        return False

    def cube_test(self):
        for divisor in self.divisors:
            if divisor ** 3 == self.value:
                return True
        return False

    def perfect_test(self):
        if sum(self.divisors) == self.value:
            return True
        else:
            return False

    def abundant_test(self):
        if sum(self.divisors) > self.value:
            return True
        else:
            return False

    def deficient_test(self):
        if sum(self.divisors) < self.value:
            return True
        else:
            return False

    def fibonacci_test(self):
        binet_number1 = ((self.value ** 2) * 5) + 4
        binet_number2 = ((self.value ** 2) * 5) - 4
        binet_divisors1 = [i for i in range(1, binet_number1) if binet_number1 % i == 0]
        binet_divisors2 = [i for i in range(1, binet_number2) if binet_number2 % i == 0]
        for divisor in binet_divisors1:
            if divisor ** 2 == binet_number1:
                return True
        for divisor in binet_divisors2:
            if divisor ** 2 == binet_number2:
                return True
        return False

    def palindrome_test(self):
        flipped_list = self.digits[::-1]
        if self.digits == flipped_list:
            return True
        else:
            return False

    def armstrong_test(self):
        exponent = len(self.digits)
        armstrong_list = [i ** exponent for i in self.digits]
        if self.value == sum(armstrong_list):
            return True
        else:
            return False

    def automorphic_test(self):
        square = self.value ** 2
        square_divisors = [i for i in range(1, square) if square % i == 0]
        while len(square_divisors) > len(self.divisors):
            del square_divisors[0]
        if self.divisors == square_divisors:
            return True
        else:
            return False


# testing

for i in range(1000):
    num = TestNumber(i)
    for attribute, value in vars(num).items():
        print(f'{attribute}: {value}')
    print("=========================")



