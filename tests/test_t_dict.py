#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_t_dict
----------------------------------

Tests for `t_dict` module.
"""

import unittest

from t_dict.t_dict import TDict


class TestJsonPointerTraversal(unittest.TestCase):

    def setUp(self):
        self.td = TDict({
            'nested': {
                'dict': {
                    'key': 'Hello!!'
                }
            }
        })

    def test_find(self):
        self.assertEqual(self.td.find('/nested/dict/key'), 'Hello!!')
        self.assertEqual(self.td.find('/nested/dict/notfound', 'mydefault'), 'mydefault')

    def test_setin(self):
        self.td.setin('/nested/dict/key', 'Horadric cube!')
        self.assertEqual(self.td['nested']['dict']['key'], 'Horadric cube!')


if __name__ == '__main__':
    unittest.main()
