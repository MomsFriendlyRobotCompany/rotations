# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################

import numpy as np
from numpy import sin, cos, pi, sqrt
deg2rad = pi/180
rad2deg = 180/pi


# 
# class Frame:
#     def __init__(self, name, parent, child, orientation, translation):
#         pass
#
#     def to_parent(self, pt):
#         pass
#
#     def to_chile(self, pt):
#         pass
#
#     @property
#     def parent(self):
#         return None
#
#     @parent.setter
#     def parent(self, x):  # value?
#         return None
#
#     @property
#     def child(self):
#         return None
#
# class ECI(Frame):
#     def __init__(self):
#         super(ECI, self).__init__("eci",None,)





def ecef2ned(lat, lon, degrees=True):
    """
    Pned = R(Pecef - Pref)

    Note: R below equals R^T on wikipedia
    https://en.wikipedia.org/wiki/Local_tangent_plane_coordinates
    """
    if degrees:
        lat *= deg2rad
        lon *= deg2rad
    return np.array([
        [-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat)],
        [-sin(lon), cos(lon), 0],
        [-cos(lat)*cos(lon), -cos(lat)*sin(lon), -sin(lat)]
    ])

def ll2nwu(lat, lon, degrees=True):
    if degrees:
        lat *= deg2rad
        lon *= deg2rad
    return np.array([
        [-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat)],
        [sin(lon), -cos(lon), 0],
        [cos(lat)*cos(lon), -cos(lat)*sin(lon), sin(lat)]
    ])

def ll2ecef(lat,lon, alt, degrees=True):
    if degrees:
        lat *= deg2rad
        lon *= deg2rad

    a = 6378137.0 # WGS semi-major axis
    b = 6356752.314245 # WGS semi-minor axis
    e = sqrt(1-(b/a)**2)
    d = sqrt(1-e**2*sin(lat)**2)
    f = (a/d+alt)*cos(lat)

    x = f*cos(lon)
    y = f*sin(lon)
    z = (a*(1-e*e)/d+alt)*sin(lat)

    return np.array([x,y,z])

def ll2ecef2(lat, lon, H):
    # is this the same as the other ll2ecef?
    #
    # phi = lat
    # lambda = lon
    # H = height above mean sea-level (altitude)
    e = 1.0
    re = 6378137.0  # radius of Earth in meters
    
    # convert degrees to angles
    lat *= deg2rad
    lon *= deg2rad
    
    rm = re * (1.0 - e**2) / pow(1.0 - e**2 * sin(lat)**2, 3.0 / 2.0)
    rn = re / sqrt(1.0 - e**2 * sin(lat)**2)
    x = (rn + H) * cos(lat) * cos(lon)
    y = (rn + H) * cos(lat) * sin(lon)
    z = (rm + H) * sin(lat)
    return x, y, z
