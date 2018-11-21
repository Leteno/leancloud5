import cv2, os
import numpy as np

def drawDots(file, positions, targetFile):
    assert os.path.exists(file)
    image = cv2.imread(file)
    for pt in positions:
        cv2.circle(image, (int(pt[0]), int(pt[1])), 5, (0,0,255), -1)
    cv2.imwrite(targetFile, image)

def getHitPositions(searchFile, screenSize=(1080, 1920)):
    cakeFiles = ['asserts/cake1.png', 'asserts/cake2.png', 'asserts/cake3.png']
    searchImage = getRedChannel(getImage(searchFile))

    result = []
    for f in cakeFiles:
        print('checking: %s' % f)
        templateImage = getRedChannel(getImage(f))
        for pt in _getHitPositions(searchImage, templateImage, screenSize=screenSize):
            result.append(pt)

    return result

def _getHitPositions(searchImage, templateImage, threshold=0.56, screenSize=(1080, 1920), debug=False):
    if not screenSize == (1080, 1920):
        w, h = templateImage.shape[::-1]
        newWidth, newHeight = int(w * screenSize[0] / 1080), int(h * screenSize[1] / 1920)
        templateImage = cv2.resize(templateImage, (newWidth, newHeight))

    res = cv2.matchTemplate(searchImage, templateImage, cv2.TM_CCOEFF_NORMED)


    w, h = templateImage.shape[::-1]
    halfW, halfH = int(w/2), int(h/2)
    def square(x):
        return x * x
    def absolute(x):
        return x if x > 0 else -x
    suggestingDistance = 80
    def tooNear(existingPoints, pt):
        if debug:
            print('current points: %s' % existingPoints)
        for _pt in existingPoints:
            dist = absolute(_pt[0] - pt[0]) + absolute(_pt[1] - pt[1])
            if debug:
                print('dist: %s' % dist)
            if dist < suggestingDistance:
                return True
        return False

    result = []
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        center = (pt[0] + halfW, pt[1] + halfH)
        if not tooNear(result, center):
            result.append(center)
    return result

def getRedChannel(im):
    r, g, b = cv2.split(im)
    return r

def getImage(file):
    assert os.path.exists(file)
    return cv2.imread(file)

def writeToFile(im, file):
    cv2.imwrite(file, im)

def test():
    testFile, templateFile = 'test.jpeg', 'asserts/cake3.png'

    array = getHitPositions(testFile, templateFile, 0.6)
    for pt in array:
        print(pt)

if __name__ == '__main__':
    test()
