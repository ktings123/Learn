# -*- coding:utf-8 -*-

import unittest
from sel.teple import *


class TestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3,add(1,2))

    def test_mul(self):
        self.assertEqual(3, mul(1, 3))


    def test_min(self):
        self.assertEqual(5,minu(8, 3))


