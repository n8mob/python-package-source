#!/usr/bin/python3

import unittest

from helloer.hello import say_hello


class TestHello(unittest.TestCase):
    def test_none(self):
        actual = say_hello()

        self.assertEqual('Hello, World', actual)

    def test_empty(self):
        actual = say_hello('')

        self.assertEqual('Hello, World', actual)

    def test_a_name(self):
        actual = say_hello('there')

        self.assertEqual('Hello, there', actual)


if __name__ == '__main__':
    unittest.main()
