import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
    property var square_height: parent.height * 0.225
    property var square_width: parent.width * 0.15

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

    function isPlateSelected(index){
        if(index == zmqClient.start_plate_selected)
            return true
        else
            return false
    }
    }

    Image {
        source: "../res/table.png"
        anchors.fill : parent
    }

    Repeater{
        model: zmqClient.robot_detection
        Rectangle{
            width: parent.width/12
            height: width
            radius: width / 2
            color: "lavender"
            visible: detectionVisible(modelData.x, modelData.y, modelData.quality)
            x: modelData.x * parent.width / 3.000 - width/2
            y: (modelData.y+1.000) * parent.height / 2.000 - height / 2
            Label {
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: parent.height / 2
                color: "black"
                text: modelData.quality
            }
        }
    }

    
    // Top left
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(1) ? 0.5 : 0
        anchors.top: parent.top
        anchors.left: parent.left
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(1)
            }
        }
    }

    // Left middle top
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(2) ? 0.5 : 0
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.leftMargin:parent.width * 0.15 * 2
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(2)
            }
        }
    }

    // Right middle top
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(3) ? 0.5 : 0
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.rightMargin:parent.width * 0.15 * 2
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(3)
            }
        }
    }

    // Top right
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(4) ? 0.5 : 0
        anchors.top: parent.top
        anchors.right: parent.right
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(4)
            }
        }
    }

    // Right top middle
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(5) ? 0.5 : 0
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.topMargin:parent.height * 0.25
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(5)
            }
        }
    }

    // Right bottom middle
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(6) ? 0.5 : 0
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.bottomMargin:parent.height * 0.25
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(6)
            }
        }
    }

    // Bottom right
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(7) ? 0.5 : 0
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(7)
            }
        }
    }

    // Right middle bottom
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(8) ? 0.5 : 0
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.rightMargin: parent.width * 0.15 * 2
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(8)
            }
        }
    }

    // Left middle bottom
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(9) ? 0.5 : 0
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.leftMargin: parent.width * 0.15 * 2

        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(9)
            }
        }
    }

    // Bottom left
    Rectangle{
        width: square_width
        height: square_height
        color: "red"
        opacity: isPlateSelected(10) ? 0.5 : 0
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(10)
            }
        }
    }

    Image {
        id: robot_shape
        source: "../res/robot.png"
        width: parent.width / 12
        height: parent.height / 12
        x: zmqClient.robot_pose_x * parent.width / 3.000 - width/2
        y: (-zmqClient.robot_pose_y + 1) * parent.height / 2.000 - height / 2
        transform: Rotation { origin.x: robot_shape.width/2 ; origin.y: robot_shape.height/2; angle: 90 + ((-1) * (180 * zmqClient.robot_pose_yaw / Math.PI))}
    }

}
