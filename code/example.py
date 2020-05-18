"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import sys
import cv2
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QImage, QPixmap, QCloseEvent
from PyQt5.QtWidgets import QApplication
from gaze_tracking.gaze_tracking import GazeTracking
from GUImain.GUIframe import MyApp

gaze = GazeTracking()
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#GUI
app = QApplication(sys.argv)
gui = MyApp()


while True:
    if gui.quit_sig:
        sys.exit()

    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)


    #GUI
    if bool(gui.start_btn.isChecked()):
        qformat = QImage.Format_Indexed8
        if len(frame.shape) == 3:
            if frame.shape[2] == 4:  # RGBA
                qformat = QImage.Format_RGBA8888
            else:  # RGB
                qformat = QImage.Format_RGB888
        out_image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], qformat)
        out_image = out_image.rgbSwapped()
        gui.face_label.setPixmap(QPixmap.fromImage(out_image))
        #cv2.imshow("Demo", frame)


    if cv2.waitKey(1) == 27:
        break

