#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, signal
import zmq
from PyQt5.QtCore import QObject, QSocketNotifier, pyqtSignal, pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

from google.protobuf.wrappers_pb2 import Int32Value

proto_types = {
    'gui/score': Int32Value
    }

class ZmqClient(QObject):
    notifyScore = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._context = zmq.Context()
        
        self._sub_socket = self._context.socket(zmq.SUB)
        self._sub_socket.bind('tcp://*:3901')
        self._sub_socket.setsockopt(zmq.SUBSCRIBE,b'')
        
        self._pub_socket = self._context.socket(zmq.PUB)
        self._pub_socket.bind('tcp://*:3902')
        
        self._notifier = QSocketNotifier(self._sub_socket.getsockopt(zmq.FD), QSocketNotifier.Read, self)
        self._notifier.activated.connect(self._on_sub_socket_event)
        
        self._score = 0
        self._side = 0
        
    def _on_sub_socket_event(self):        
        self._notifier.setEnabled(False)
        flags = self._sub_socket.getsockopt(zmq.EVENTS)
        while flags & zmq.POLLIN:
            topic, body = self._sub_socket.recv_multipart()
            topic = topic.decode('utf8')
            proto_class = proto_types[topic]
            if proto_class is not None:
                value = proto_class()
                value.ParseFromString(body)
                self._on_message_received(topic, value)
            flags = self._sub_socket.getsockopt(zmq.EVENTS)
        self._notifier.setEnabled(True)
        
    def _on_message_received(self, topic, value):
        if topic == 'gui/score':
            self._score = value.value
            self.notifyScore.emit()
            
    @pyqtProperty(int, notify=notifyScore)
    def score(self):
        return self._score
        
    def setSide(self, side):
        self._side = side
        self.notifyScore.emit()
        msg = Int32Value(value=side)
        self._pub_socket.send_multipart([b'gui/score', msg.SerializeToString()])
        
    @pyqtProperty(int, fset=setSide, notify=notifyScore)
    def side(self):
        return self._side
        
        
            
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    zmq_client = ZmqClient()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("zmqClient", zmq_client)
    engine.load('main.qml')
    win = engine.rootObjects()[0]
    win.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())