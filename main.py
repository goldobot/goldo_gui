#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys, signal
from PyQt5 import QtCore, QtGui, QtQml
from zmq_client import ZmqClient
from camera_item import CameraItem

parser = argparse.ArgumentParser(description='Robot control GUI')
parser.add_argument('--windowed', dest='windowed', action='store_true', help='Run GUI in windowed mode')
parser.set_defaults(windowed=False)
args = parser.parse_args()

if __name__ == "__main__":
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

    app = QtGui.QGuiApplication(sys.argv)
    if args. windowed == False:
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app.setOverrideCursor(QtCore.Qt.BlankCursor);

    QtQml.qmlRegisterType(CameraItem, "goldo", 1, 0, "CameraItem")
    
    engine = QtQml.QQmlApplicationEngine()
    zmq_client = ZmqClient()
    engine.rootContext().setContextProperty("zmqClient", zmq_client)
    engine.rootContext().setContextProperty("windowed", args.windowed)
    engine.load('qml/main.qml')
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())
