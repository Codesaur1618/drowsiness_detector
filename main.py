import cv2
import numpy as np
import dlib
from imutils import face_utils
import winsound



# to start camera and run the process
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("AK.dat")

# instances
slept= 0
drowsy = 0
active = 0
status = ""
colour = (0, 0, 0)



def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # the ratio of eyes closing using eucleadian ratio
    if (ratio > 0.35):
        return 2
    elif (ratio > 0.25 and ratio <= 0.35):
        return 1
    else:
        return 0


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = frame.copy()
    # detection mechanism
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # determinig landmark array
        left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        # now eye blink detect and result
        if (left_blink == 0 or right_blink == 0):
            slept += 1
            drowsy = 0
            active = 0
            if (slept > 8):
                status = "SLEEPING !!!"
                colour = (255, 0, 0)
                winsound.PlaySound("bigalarm.wav", winsound.SND_ASYNC)




        elif (left_blink == 1 or right_blink == 1):
            slept = 0
            active = 0
            drowsy += 1
            if (drowsy > 20):
                status = "Drowsy !"
                colour = (0, 200, 255)
                winsound.PlaySound("smallalarm.wav",winsound.SND_ASYNC)

        else:
            slept = 0
            drowsy = 0
            active += 1
            if (active > 5):
                status = "Active :)"
                colour = (0, 255, 0)

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, colour, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
