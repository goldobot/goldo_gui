from PyQt5.QtGui import QImage
from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtCore import pyqtSlot

import cv2
from cv2 import aruco
import numpy as np

class CameraItem(QQuickPaintedItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.setRenderTarget(QQuickPaintedItem.FramebufferObject) 
        self._frame = QImage()
        self._detections = None

    def paint(self, painter):
        painter.drawImage(0, 0, self._frame)
        
    @pyqtSlot(object)
    def updateDetections(self, msg):
        self._detections = msg
        
        
    @pyqtSlot(object)
    def updateFrame(self, msg):
        frame = cv2.imdecode(np.fromstring(msg.data, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        if self._detections:
            ids = np.array([d.tag_id for d in self._detections.detections])
            corners = [np.array([[[c.x, c.y] for c in d.corners]], dtype=np.float32) for d in self._detections.detections]
            frame = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        frame = cv2.resize(frame, (int(self.width()), int(self.height())), cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        self._frame = QImage(frame, frame.shape[1], frame.shape[0], 17)
        self.update()  