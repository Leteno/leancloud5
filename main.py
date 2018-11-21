#!/usr/bin/env python3

import os, time

from script import graphic, adb, cli

def main():
    logTime('script begin')
    assert adb.hasDevice()
    logTime('hasDevice spends')
    screenSize = adb.getScreenSize()
    logTime('screensize spends')

    beginTime = time.time()
    currentTime, endTime = beginTime, beginTime + 20
    while currentTime < endTime:
        file = getScreenShot()
        logTime('screenshot spends')
        recordTime = time.time()

        positions = graphic.getHitPositions(file, screenSize=screenSize)
        logTime('analysis hit positions spends')
        # graphic.drawDots(file, positions, targetFile='build/result.png')
        # logTime('drawDots spends')
        # cli.execute('open build/result.png', '.')
        # logTime('open result file spends')

        speed = 200
        for pt in positions:
            elapse = time.time() - recordTime
            dy = elapse * speed
            adb.tap(pt[0], pt[1] + dy)
        currentTime = time.time()
        logTime('finish one loop')

    logTime('done')

lastTime = 0
def logTime(msg):
    global lastTime
    currentTime = time.time()
    if lastTime:
        print('%s  %s' % (msg, currentTime - lastTime)) 
    else:
        print(msg)
    lastTime = currentTime

def getScreenShot():
    ssFile = 'build/s.png'
    adb.screenShot(ssFile)
    assert os.path.exists(ssFile)
    return ssFile


if __name__ == '__main__':
    main()