import numpy as np
from numpy import sin, cos, pi


def ll2ned(lat, lon):
    return np.array([
        [-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat)],
        [-sin(lon), cos(lon), 0],
        [-cos(lat)*cos(lon), -cos(lat)*sin(lon), -sin(lat)]
    ])

def ll2nwu(lat, lon):
    return np.array([
        [-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat)],
        [sin(lon), -cos(lon), 0],
        [cos(lat)*cos(lon), -cos(lat)*sin(lon), sin(lat)]
    ])

def ll2ecef(lat,lon, alt, degrees=True):
    if degrees:
        lat *= deg2rad
        lon *=deg2rad

    a = 6378137.0 # WGS semi-major axis
    b = 6356752.314245 # WGS semi-minor axis
    e = sqrt(1-(b/a)**2)
    d = sqrt(1-e**2*sin(lat)**2)
    f = (a/d+alt)*cos(lat)

    x = f*cos(lon)
    y = f*sin(lon)
    z = (a*(1-e*e)/d+alt)*sin(lat)

    return np.array([x,y,z])
