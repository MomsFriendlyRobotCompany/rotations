# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
from importlib.metadata import version # type: ignore

from .rotations import R1,R2,R3
from .rotations import R321,R123,R313
from .utils import rad2deg, deg2rad

# from .sym_rotations import sR1,sR2,sR3
# from .sym_rotations import sR321,sR123,sR313

__author__ = 'Kevin Walchko'
__license__ = 'MIT'
__version__ = version("rotations")
