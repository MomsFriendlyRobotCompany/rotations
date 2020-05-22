# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################

import numpy as np

rad2deg = 180/np.pi
deg2rad = np.pi/180

def R321(a,b,c, degrees=False):
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad
    return None


def R1(a, degrees=False):
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad
    return None


def R2(a, degrees=False):
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad
    return None


def R3(a, degrees=False):
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad
    return None


def R313(a,b,c, degrees=False):
    """Returns a rotation matrix based on: Z1*X2*Z3"""
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad

    s3 = np.sin(c); c3 = np.cos(c)
    s2 = np.sin(b); c2 = np.cos(b)
    s1 = np.sin(a); c1 = np.cos(a)

    return np.array(
        [
            [c1*c3-c2*s1*s3, -c1*s3-c2*c3*s1, s1*s2],
            [c3*s1+c1*c2*c3, c1*c2*s3, c1*c2*c3-s1*s3,-c1*s2],
            [s2*s3, c3*s2, c2]
        ]
    )
