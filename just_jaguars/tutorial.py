import cv2
import time


def play_tutorial():
    """Credit goes to https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html"""
    cap = cv2.VideoCapture('assets/tutorial.mov')

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret or cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow('tutorial', frame)
        time.sleep(1 / 30)  # 30 fps

    cap.release()
    cv2.destroyAllWindows()


# test if the tutorial needs to be played
try:
    tutorial_file = open('saves/tutorial.txt')  # error causing function 1

    tutorial_content = tutorial_file.read()
    tutorial_file.close()

    assert tutorial_content == 'done'
except Exception:
    play_tutorial()

    with open('saves/tutorial.txt', 'w') as f:
        f.write('done')
