import cv2
import mediapipe as mp

class handDetector:
    def __init__(
            self,
            mode=False,
            maxHands=1,
            modelComplexity=0,
            detectionConfidence=0.6,
            trackConfidence=0.6
        ):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionConfidence
        self.trackCon = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode,
            self.maxHands,
            self.modelComplexity,
            self.detectionCon,
            self.trackCon
        )
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = cv2.flip(img, 1)
        self.results = self.hands.process(imgRGB)
        return imgRGB

    def findPosition(self, img, sizes, handNo=0):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * sizes[0]), int(lm.y * sizes[1])
                self.lmList.append([id, cx, cy])
        return self.lmList


    def fingersUp(self):
        fingers = []

        fingers.append(self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1])
        for id in range(1, 5):
            fingers.append(self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2])
        return fingers



