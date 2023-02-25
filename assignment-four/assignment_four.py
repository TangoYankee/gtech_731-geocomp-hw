from Geom import Circle, Square, Triangle
from random import seed

"""Use seed to make random functions always return predicted values"""
seed(2)

def test_square_area():
    side = 8
    test_sqr = Square(side)
    expected_area = 64
    assert(test_sqr.area() == expected_area)

test_square_area()

def test_square_string():
    side = 2
    test_sqr = Square(side)
    expected_str = "Name: Bill, Color: RED, Area: 4"
    assert(test_sqr.makeString() == expected_str)

test_square_string()

def test_create_circles():
    circles = [Circle(i) for i in range(2,4)]
    [one, two] = circles

    exp_one_str = "Name: Sally, Color: PURPLE, Area: 12.566370614359172"
    exp_two_str = "Name: Hussain, Color: RED, Area: 28.274333882308138"
    assert(one.makeString() == exp_one_str)
    assert(two.makeString() == exp_two_str)

test_create_circles()

def test_create_triangle():
    triangle = Triangle(3,6)
    exp_str = "Name: Tamica, Color: PURPLE, Area: 9.0"
    assert(triangle.makeString() == exp_str)

test_create_triangle()