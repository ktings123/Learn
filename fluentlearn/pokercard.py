import collections
from math import hypot

import unittest


# 卡牌
# card = collections.namedtuple('card', ['rank', 'suit'])
#
#
# class Frenchdeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suit = "spades diamons clubs hearts".split()
#
#     def __init__(self):
#         self.cards = [card(rank, suit) for suit in self.suit for rank in self.ranks]
#
#     def __len__(self):
#         return len(self.cards)
#
#     def __getitem__(self, position):
#         return self.cards[position]
#
#     def spades_high(self, card):
#         suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#         rank_value = Frenchdeck.ranks.index(card.ranks)
#         return rank_value * len(suit_values) + suit_values[card.suit]
#
#
# bee_card = card('7', 'diamonds')
# print(bee_card)
# deck = Frenchdeck()
# print(len(deck))
# print(deck[11])
# print(deck[:3])
# print(deck[12::13])


# 二维向量
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({x},{y})".format(x=self.x, y=self.y)

    def __abs__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# v1 = Vector(2, 4)
# v2 = Vector(1, 3)
# print(v1 + v2)


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')


defaultSizeTestCase = WidgetTestCase('test_default_size')
resizeTestCase = WidgetTestCase('test_resize')

widgetTestSuite = unittest.TestSuite()
widgetTestSuite.addTest(WidgetTestCase('test_default_size'))
widgetTestSuite.addTest(WidgetTestCase('test_resize'))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_size'))
    suite.addTest(WidgetTestCase('test_resize'))
    return suite

ss = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
