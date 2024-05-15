import cv2
import mediapipe as mp

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

        self.mpHands = mp.solution

        self.hand = self.mpHands.Hands(
            static_image_mode=self.mode,
            model_complexity=0,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackConfidence
        )
# I am animeboy(tima)
    def start(self):
        video = cv2.VideoCapture(0)


def main():
    detector = handAndGestureDetector()
    detector.start()

if __name__ == "__name__":
    main()
