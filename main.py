#!/usr/bin/env python3

import os

from script import graphic, adb

def main():
    file = getScreenShot()
    graphic.getHitPositions(file, 'asserts/cake3.png', 0.56, True)

def getScreenShot():
    ssFile = 'build/s.png'
    adb.screenShot(ssFile)
    assert os.path.exists(ssFile)
    return ssFile

if __name__ == '__main__':
    main()