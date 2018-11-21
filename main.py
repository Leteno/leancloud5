#!/usr/bin/env python3

import os, time

from script import graphic, adb, cli

def main():
    logTime('script begin')
    assert adb.hasDevice()
    logTime('hasDevice spends')

    file = getScreenShot()
    logTime('screenshot spends')
    # screenSize = adb.getScreenSize()
    screenSize = (1080, 1920)
    logTime('screensize spends')
    positions = graphic.getHitPositions(file, screenSize=screenSize)
    logTime('analysis hit positions spends')
    graphic.drawDots(file, positions, targetFile='build/result.png')
    logTime('drawDots spends')
    cli.execute('open build/result.png', '.')
    logTime('open result file spends')

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