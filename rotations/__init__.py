# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
try:
    from importlib.metadata import version # type: ignore
except ImportError:
    from importlib_metadata import version # type: ignore

from rotations.rotations import R1,R2,R3,R321,R123,R313

__author__ = 'Kevin Walchko'
__license__ = 'MIT'
__version__ = version("rotations")
