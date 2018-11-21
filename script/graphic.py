import cv2, os
import numpy as np

def getHitPositions(searchFile, templateFile, threshold, paintIt=False):
    searchImage = getRedChannel(getImage(searchFile))
    templateImage = getRedChannel(getImage(templateFile))

    result = []

    res = cv2.matchTemplate(searchImage, templateImage, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        result.append(pt)

    if paintIt:
        w, h = templateImage.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv2.rectangle(searchImage, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imwrite('build/result.png', searchImage)

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
