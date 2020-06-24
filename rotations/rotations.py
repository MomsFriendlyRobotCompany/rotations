# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################

import numpy as np

rad2deg = 180/np.pi
deg2rad = np.pi/180

# https://en.wikipedia.org/wiki/Rotation_matrix
def R1(a, degrees=False):
    if degrees:
        a *= deg2rad
    ca = np.cos(a)
    sa = np.sin(a)
    return np.array(
        [[1,  0,   0],
         [0, ca, -sa],
         [0, sa,  ca]]
    )


def R2(a, degrees=False):
    if degrees:
        a *= deg2rad
    ca = np.cos(a)
    sa = np.sin(a)
    return np.array(
        [[ ca, 0, sa],
         [  0, 1,  0],
         [-sa, 0, ca]]
    )


def R3(a, degrees=False):
    if degrees:
        a *= deg2rad
    ca = np.cos(a)
    sa = np.sin(a)
    return np.array(
        [[ca, -sa, 0],
         [sa,  ca, 0],
         [ 0,   0, 1]]
    )


def R313(a,b,c, degrees=False):
    """Returns a rotation matrix based on: Z1(c)*X2(b)*Z3(a)"""
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
            [c3*s1+c1*c2*s3, c1*c2*c3-s1*s3,-c1*s2],
            [s2*s3, c3*s2, c2]
        ]
    )


def R312(a,b,c, degrees=False):
    """Returns a rotation matrix based on: Y2*X1*Z3"""
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad

    s3 = np.sin(c); c3 = np.cos(c)
    s2 = np.sin(b); c2 = np.cos(b)
    s1 = np.sin(a); c1 = np.cos(a)

    return np.array(
        [
            [c1*c3-s1*s2*s3, -c2*s1, c1*s3+c3*s1*s2],
            [c3*s1+c1*s2*s3,  c1*c2, s1*s3-c1*c3*s2],
            [        -c2*s3,     s2,          c2*c3]
        ]
    )


def R321(a,b,c, degrees=False):
    """Returns a rotation matrix based on: Z3*Y2*X1"""
    if degrees:
        a *= deg2rad
        b *= deg2rad
        c *= deg2rad

    s3 = np.sin(c); c3 = np.cos(c)
    s2 = np.sin(b); c2 = np.cos(b)
    s1 = np.sin(a); c1 = np.cos(a)

    return np.array(
        [
            [c1*c2, c1*s2*s3-c3*s1, s1*s3+c1*c3*s2],
            [c2*s1, c1*c3+s1*s2*s3, c3*s1*s2-c1*s3],
            [  -s2,          c2*s3,          c2*c3]
        ]
    )
