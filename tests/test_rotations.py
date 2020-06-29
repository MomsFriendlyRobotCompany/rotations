from rotations.rotations import R1,R2,R3,R313,R321
import numpy as np
# from scipy.spatial.transform import Rotation as R


def test_313():
    for one in [-65,0,90]:
        for two in  [90, -45, -90]:
            for three in [-90, -45, 0]:
                r313 = R3(three, True) @ R1(two,True) @ R3(one,True)
                # r313 = R3(one, True) @ R1(two,True) @ R3(three,True)
                # r = R313(one,two,three,True) # big errors
                r = R313(one,two,three,True)
                # r = R313(three,two,one,True)
                # print("")
                # print(r313)
                # print(r)
                # print(r-r313)
                assert np.allclose(r313, r)

def test_321():
    for one in [-65,0,90]:
        for two in  [90, -45, -90]:
            for three in [-90, -45, 0]:
                r321 = R1(three, True) @ R2(two,True) @ R3(one,True)
                r = R321(one,two,three,True)
                # print("")
                # print(r321)
                # print(r)
                # print(r-r321)
                assert np.allclose(r321, r)

                # rr = R.from_euler('zyx',
                #     [[one,0,0],
                #      [0,two,0],
                #      [0,0,three]],
                #     degrees=True)
                # print(rr)
                # print(R.from_euler('z', 90, degrees=True))
                # print(r-rr)
                # assert np.allclose(r, rr)
