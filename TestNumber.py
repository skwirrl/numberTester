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
        self.is_fibonacci =
        self.is_palindrome =
        self.is_automorphic =



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
            if divisor ** 2 == 0:
                return True
        return False

    def cube_test(self):
        for divisor in self.divisors:
            if divisor ** 3 == 0:
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

