import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4
import QtQml.Models 2.15

Page {
    function getCompassColor(textColor){
        if(!textColor){
            switch(zmqClient.compass){
                case 0:
                    return "red"
                case 1:
                    return "black"
                case 2:
                    return "white"
            }
        }
        else{
            if(zmqClient.compass == 2){
                return "black"
            }
            else{
                return "white"
            }
        }
    }

    function getCompassText(){
        switch(zmqClient.compass){
            case 0:
                return "?"
            case 1:
                return "N"
            case 2:
                return "S"
        }
    }

    Image {
        source: "../res/table.png"
        anchors.fill : parent
    }

    Rectangle {
        id: compass_rect
        width: parent.width / 10
        height: parent.height / 6.7
        color: getCompassColor(false)
        opacity: 0.7
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
    }
    Text {
        anchors.horizontalCenter: compass_rect.horizontalCenter
        anchors.verticalCenter: compass_rect.verticalCenter
        font.pixelSize: compass_rect.height / 2
        color: getCompassColor(true)
        text: getCompassText()
    }

    Image {
        id: robot_shape
        source: "../res/robot.png"
        width: parent.width / 12
        height: parent.height / 12
        x: (zmqClient.robot_pose_y + 1.500) * parent.width / 3.000 - width/2
        y: zmqClient.robot_pose_x * parent.height / 2.000 - height / 2
        transform: Rotation { origin.x: robot_shape.width/2 ; origin.y: robot_shape.height/2; angle: 180 + 180 * zmqClient.robot_pose_yaw / Math.PI}
    }

    Repeater{
        model: zmqClient.robot_detection
        Rectangle{
            width: parent.width/12
            height: width
            radius: width / 2
            color: "lavender"
            visible: modelData.quality == 0 ? false : true
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