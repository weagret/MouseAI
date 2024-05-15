import cv2
import mediapipe as mp
import pyautogui as pag
import HandTrackingModule as htm
import time


class handAndGestureDetector:
    def __init__(
            self,
            staticMode=False,
            maxHands=1,
            detectionConfidence=0.6,
            trackConfidence=0.6
    ):

        self.mode = staticMode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutionsй.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            model_complexity=0,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackConfidence
        )
        self.detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    def start(self):
        x_len, y_len = pag.size()
        x_m, y_m = 720, 450
        pag.moveTo(720, 450)
        flag = False

        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, img = cap.read()
            # приводим в понятный для mediapipe вид
            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            # находим руку
            results = self.hands.process(image)

            img = self.detector.findHands(img)
            lmList, bbox = self.detector.findPosition(img, draw=False)

            if lmList and results.multi_hand_landmarks:
                fingersUp = self.detector.fingersUp()
                fingersUp[0] = int(not fingersUp[0])
                totalFingers = fingersUp.count(1)
                elem = results.multi_hand_landmarks[0].landmark[0]
                if totalFingers == 0:
                    pag.click()
                if fingersUp[0] == 1 and totalFingers == 1:
                    pag.rightClick()
                if totalFingers == 5:

                    flag = False
                if totalFingers == 4 and fingersUp[0] == 0 and not flag:
                    flag = True
                    x = round(elem.x * x_len - 80)
                    y = round(elem.y * y_len - 80)
                if totalFingers == 4 and fingersUp[0] == 0 and flag:
                    x_0, y_0 = x, y
                    x = round(elem.x * x_len - 80)
                    y = round(elem.y * y_len - 80)

                    if (not (x > x_0 + 5) or not (x < x_0 - 5)) or (not (y > y_0 + 5) or not (y < y_0 - 5)):
                        pag.moveTo(x - x_0 + x_m, y - y_0 + y_m)
                        x_m = x - x_0 + x_m
                        y_m = y - y_0 + y_m
            # чтобы прервать надо зажать q, но оно пока не работает,  почему-то :(
            if cv2.waitKey(10) & 0xFF == ord('q'):
                print(cv2.waitKey(10) & 0xFF)
                break




def main():
    a = handAndGestureDetector()
    a.start()

main()
