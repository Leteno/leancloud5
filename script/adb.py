import re

if __name__ == '__main__':
    import cli
else:
    from script import cli

def hasDevice():
    cmd = 'adb devices'
    _, output = cli.execute(cmd, '.')
    return not output == 'List of devices attached\n\n'

def getDensity():
    cmd = 'adb shell wm density'
    _, output = cli.execute(cmd, '.')
    m = re.search('([0-9]+)', output)
    if m:
        return int(m.group(1))
    return -1

def getScreenSize():
    cmd = 'adb shell wm size'
    _, output = cli.execute(cmd, '.')
    m = re.search('([0-9]+)[xX]([0-9]+)', output)
    width, height = 0, 0
    if m:
        width, height = int(m.group(1)), int(m.group(2))
    return width, height

def screenShot(targetPath):
    '''
    return success
    '''
    tmpFile = '/sdcard/MrZhengWantIt.png'
    cmd = 'adb shell screencap -p %s' % tmpFile
    ok1, _ = cli.execute(cmd, '.')
    cmd = 'adb pull %s %s' % (tmpFile, targetPath)
    ok2, _ = cli.execute(cmd, '.')
    return ok1 and ok2

def tap(x, y):
    # 0.4 s for one tap
    cmd = 'adb shell input tap %s %s' % (x, y)
    # cli.execute(cmd, '.')  # 7.139
    # cli.execute1(cmd)  # 7.115
    # cli.execute2(cmd)  # 7.165
    # cli.execute3(cmd) # 7.282
    # cli.execute4(cmd) # 7.192
    # cli.execute4(cmd) # 4.136 if use emulator
    cli.execute1(cmd)

def test():
    assert hasDevice(), 'No Device, No Talk'
    print('density: %s' % getDensity())
    print('screensize: %s,%s' % getScreenSize())
    print('screenshot: %s' % screenShot('s.png'))

def testTap():
    for x in range(10):
        tap(x, x)

def testScreenShot():
    import time
    f1, f2 = 'f1.png', 'f2.png'
    t1 = time.time()
    screenShot(f1)
    t2 = time.time()
    screenShot(f2)
    t3 = time.time()
    print('t2-t1: %s, t3 - t2: %s' % (t2-t1, t3-t2))

if __name__ == '__main__':
    testScreenShot()