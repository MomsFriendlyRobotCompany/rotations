import sympy as sp

def sR1(a):
    ca = sp.cos(a)
    sa = sp.sin(a)
    r = np.array(
        [[1,  0,   0],
         [0,  ca, sa],
         [0, -sa, ca]]
    )
    return sp.Matrix(r)


def sR2(a):
    ca = sp.cos(a)
    sa = sp.sin(a)
    r = np.array(
        [[ ca, 0, -sa],
         [  0, 1,   0],
         [ sa, 0,  ca]]
    )
    return sp.Matrix(r)


def sR3(a):
    ca = sp.cos(a)
    sa = sp.sin(a)
    r = np.array(
        [[ ca, sa, 0],
         [-sa, ca, 0],
         [  0,  0, 1]]
    )
    return sp.Matrix(r)

def sR123(x,y,z):
    """Returns a rotation matrix based on: Z*Y*X * vector"""

    s3 = sp.sin(x); c3 = sp.cos(x)
    s2 = sp.sin(y); c2 = sp.cos(y)
    s1 = sp.sin(z); c1 = sp.cos(z)

    r = np.array(
        [
            [c1*c2, c1*s2*s3+c3*s1, s1*s3-c1*c3*s2],
            [-c2*s1, c1*c3-s1*s2*s3, c3*s1*s2+c1*s3],
            [  s2,          -c2*s3,          c2*c3]
        ]
    )
    return sp.Matrix(r)

def sR313(x,y,z):
    """Returns a rotation matrix based on: R3(z) @ R1(y) @ R3(x)"""
    s3 = sp.sin(z); c3 = sp.cos(z)
    s2 = sp.sin(y); c2 = sp.cos(y)
    s1 = sp.sin(x); c1 = sp.cos(x)

    r = np.array(
        [
            [ c1*c3-c2*s1*s3, c3*s1+c1*c2*s3, s2*s3],
            [-c1*s3-c2*c3*s1, c1*c2*c3-s1*s3, c3*s2],
            [          s1*s2,         -c1*s2,    c2]
        ]
    )
    return sp.Matrix(r)

def R321(x,y,z):
    """Returns a rotation matrix based on: X*Y*Z * vector"""
    s3 = sp.sin(x); c3 = sp.cos(x)
    s2 = sp.sin(y); c2 = sp.cos(y)
    s1 = sp.sin(z); c1 = sp.cos(z)

    r = np.array(
        [
            [         c1*c2,          c2*s1,  -s2],
            [c1*s2*s3-c3*s1, c1*c3+s1*s2*s3, c2*s3],
            [s1*s3+c1*c3*s2, c3*s1*s2-c1*s3, c2*c3]
        ]
    )
    return sp.Matrix(r)