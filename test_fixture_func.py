import pytest


def setup():
    print(f"------------------------basic setup into module")


def teardown():
    print(f"--------------------------basic teardown into module")


def setup_module(module):
    print(f"\n--------------start---------------module setup {module.__name__}")


def teardown_module(module):
    print(f"---------------end------------------module teardown {module.__name__}")


def setup_function(function):
    print(f"function setup {function.__name__}")


def teardown_function(function):
    print(f"function teardown {function.__name__}")


def test_numbers_3_4():
    print(f"test 3*4")
    assert 3*4 == 12


def test_strings_a_3():
    print(f"test a*3")
    assert 'a'*3 == 'aaa'


class TestUM:
    def setup(self):
        print(f"basic setup into class")

    def teardown(self):
        print(f"basic teardown into class")

    def setup_class(cls):
        print(f"class setup")

    def teardown_class(cls):
        print(f"class teardown")

    def setup_method(self, method):
        print(f"method setup")

    def teardown_method(self, method):
        print(f"method teardown")

    def test_numbers_5_6(self):
        print(f"test 5*6")
        assert 5*6 == 30

    def test_strings_b_2(self):
        print(f"test b*2")
        assert 'b'*2 == 'bb'
