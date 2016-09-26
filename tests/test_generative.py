import unittest
from hypothesis import given
from hypothesis.strategies import text
import generative as example
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):

    # @given(text())
    # def test_decode_inverts_encode(self, s):
    #     assert example.decode(example.encode(s)) == s

    @unpack
    @data({'fullname': 'Jennifer Souza', 'expected': 'Jennifer'},
          {'fullname': 'J S Smith', 'expected':'J'},
          {'fullname': ' ', 'expected':''})
    def test_first_name(self, fullname, expected):
        self.assertEqual(example.first_name(fullname), expected)

    # @given(text(), text())
    # def test_first_name_gen(self, firstname, lastname):
    #     fullname = firstname + " " + lastname
    #     self.assertEqual(example.first_name(fullname), firstname)

    @given(text().filter(lambda c: ' ' not in c), text())
    def test_first_name_gen(self, firstname, lastname):
        fullname = firstname + " " + lastname
        self.assertEqual(example.first_name(fullname), firstname)




if __name__ == '__main__':
    unittest.main()
