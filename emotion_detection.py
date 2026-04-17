from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    print("\nEmotion:", result[0]['dominant_emotion'])

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()