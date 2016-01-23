#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_t_dict
----------------------------------

Tests for `t_dict` module.
"""

import unittest

from t_dict.t_dict import TDict


class TDictFromTDict(unittest.TestCase):
    def setUp(self):
        self.td = TDict({
            'nested': {
                'dict': {
                    'key': 'Hello!!'
                }
            }
        })

    def test_passing_tdict_to_init(self):
        td = TDict(self.td)
        self.assertEqual(self.td.find('/nested/dict/key'), 'Hello!!')
        self.assertEqual(self.td.find('/nested/dict/notfound', 'mydefault'),
                         'mydefault')
        self.td.setin('/nested/dict/key', 'Horadric cube!')
        self.assertEqual(self.td['nested']['dict']['key'], 'Horadric cube!')


class TestJsonPointerTraversal(unittest.TestCase):

    def setUp(self):
        self.td = TDict({
            'nested': {
                'dict': {
                    'key': 'Hello!!'
                }
            }
        })

    def test_find_sanity(self):
        self.assertEqual(self.td.find('/nested/dict/key'), 'Hello!!')
        self.assertEqual(self.td.find('/nested/dict/notfound', 'mydefault'),
                         'mydefault')

    def test_find_undefined_paths(self):
        undefined_paths = ['/xxx/yyy/zzz/',
                           '/nested/xxx/yyy/',
                           '/nested/dict/xxx/']
        try:
            for path in undefined_paths:
                self.td.find(path)
        except:
            self.fail('.find() fails when given an undefined path: %s' % path)

    def test_setin(self):
        self.td.setin('/nested/dict/key', 'Horadric cube!')
        self.assertEqual(self.td['nested']['dict']['key'], 'Horadric cube!')

    def test_convert_dict_to_tdict(self):
        self.assertIsInstance(self.td.find('/nested/dict'), TDict)


if __name__ == '__main__':
    unittest.main()
