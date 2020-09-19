import integer


class TestInteger:

    def test_gcd(self):
        actual = integer.gcd(4,5)
        expected = 1
        assert actual == expected

        actual = integer.gcd(3,6)
        expected = 3
        assert actual == expected

    def test_lcm(self):
        actual = integer.lcm(2,4)
        expected = 4
        assert actual == expected

        actual = integer.lcm(3,7)
        expected = 21
        assert actual == expected

    def test_enumerate_divs(self):
        actual = integer.enumerate_divs(10)
        expected = [(1,10), (2,5)]
        assert actual == expected

    def test_get_priimes(self):
        actual = integer.get_primes(10)
        expected = [2,3,5,7]
        assert actual == expected

    def test_prime_factor(self):
        actual = integer.prime_factor(10)
        expected = [2,5]
        assert actual == expected