import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
    function detectionVisible(x, y, quality){
        if(quality == 0){
            return false
        }
        else if(Math.abs(zmqClient.robot_pose_x - x < 0.1) && Math.abs(zmqClient.robot_pose_y - y < 0.1)){
            return false
        }
        else {
            return true
        }
    }

    Image {
        source: "../res/table.png"
        anchors.fill : parent
    }

    Image {
        id: robot_shape
        source: "../res/robot.png"
        width: parent.width / 12
        height: parent.height / 12
        x: (zmqClient.robot_pose_y + 1.500) * parent.width / 3.000 - width/2
        y: zmqClient.robot_pose_x * parent.height / 2.000 - height / 2
        transform: Rotation { origin.x: robot_shape.width/2 ; origin.y: robot_shape.height/2; angle: 180 + ((-1) * (180 * zmqClient.robot_pose_yaw / Math.PI))}
    }

    Repeater{
        model: zmqClient.robot_detection
        Rectangle{
            width: parent.width/12
            height: width
            radius: width / 2
            color: "lavender"
            visible: detectionVisible(modelData.x, modelData.y)
            x: (modelData.y + 1.500) * parent.width / 3.000 - width/2
            y: modelData.x * parent.height / 2.000 - height / 2
            Label {
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: parent.height / 2
                color: "black"
                text: modelData.quality
            }
        }
    }
}
