import QtQuick 2.4
import QtQuick.Controls 2.4
import goldo 1.0

Page {
    CameraItem {
        width:700
        height: 440
        anchors.horizontalCenter : parent.horizontalCenter
        anchors.verticalCenter  : parent.verticalCenter
        Component.onCompleted: {
            zmqClient.cameraFrameReceived.connect(updateFrame)
            zmqClient.cameraDetectionsReceived.connect(updateDetections)
        }
    }
}

