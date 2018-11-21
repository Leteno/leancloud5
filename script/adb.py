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

def test():
    assert hasDevice(), 'No Device, No Talk'
    print('density: %s' % getDensity())
    print('screensize: %s,%s' % getScreenSize())
    print('screenshot: %s' % screenShot('s.png'))

if __name__ == '__main__':
    test()