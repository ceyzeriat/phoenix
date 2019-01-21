#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


from .context import <package>


# https://docs.pytest.org/en/latest/getting-started.html


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
