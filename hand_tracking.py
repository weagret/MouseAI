import cv2
import pyautogui as pag
from HandTrackingModule import handDetector as HTM

class cursorAndGestureDetection:
    def __init__(self):
        self.cursorActive = True
        self.cursorFingersVisible = False
        self.cursorFingers = {
            "leftClick": 3,
            "moveCursor": 4,
            "rightClick": 2
        }
        self.keys = ["a", "b", "c", "d", "e", "f"]
        self.handDetector = HTM()

        self.sumOfFingers = 0
        self.lmList = []

        self.x0 = None
        self.y0 = None
    
    def processActions(self):
        if not self.cursorActive:
            pag.press(self.keys[self.sumOfFingers])
            return

        if self.sumOfFingers == self.cursorFingers["leftClick"]:
            pag.click()
        elif self.sumOfFingers == self.cursorFingers["rightClick"]:
            pag.rightClick()
        elif self.sumOfFingers == self.cursorFingers["moveCursor"]:
            pointerLandmark = self.lmList[9]
            _, x, y = pointerLandmark
            if not self.cursorFingersVisible:
                self.x0 = x
                self.y0 = y
                self.cursorFingersVisible = True
            else:
                pag.moveTo(x, y, 0.00001)
        else:
            pag.press(self.keys[self.sumOfFingers])


    def start(self):
        video = cv2.VideoCapture(0)
        while True:
            _, img = video.read()
            
            img = self.handDetector.findHands(img)
            self.lmList = self.handDetector.findPosition(img, pag.size())
            if self.lmList:
                fingers = self.handDetector.fingersUp()
                self.sumOfFingers = sum(fingers)
                self.processActions()
            else:
                self.cursorFingersVisible = False

            cv2.imshow("MouseAI", img)
            cv2.waitKey(1)

def main():
    detector = cursorAndGestureDetection()
    detector.start()
main()
if __name__ == "__name__":
    main()
