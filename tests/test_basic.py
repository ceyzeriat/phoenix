#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


from .context import phoenix


def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
