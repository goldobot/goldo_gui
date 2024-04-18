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


    function cakeVisible(here){
        if(here == true){
            return true
        }
        return false
    }
    
    function cakeType(color){
        switch(color) {
            case 0:
                return "../res/unknown_cake.png"
            case 1:
                return "../res/brown_cake.png"
            case 2:
                return "../res/yellow_cake.png"
            case 3:
                return "../res/pink_cake.png"
            case 4:
                return "../res/perfect_cake.png"
        }
    }
    
    function isPlateSelected(index){
        if(index == zmqClient.start_plate_selected)
            return true
        else
            return false
    }

    // Table vinyl
    Image {
        source: "../res/table.png"
        anchors.fill : parent
    }

    // Lidar detections
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

    // Lidar detections
    Repeater{
        model: zmqClient.cakes
        // Robot position
        Image {
            source: cakeType(modelData.color)
            width: 0.12 * parent.width / 3.000
            height: 0.12 * parent.height / 2.000
            x: modelData.x * parent.width / 3.000 - width/2
            y: (modelData.y+1.000) * parent.height / 2.000 - height / 2
            visible: cakeVisible(modelData.here)
        }
    }
    
    // Available start zones

    // Bottom left
    Rectangle{
        width: square_width
        height: square_height
        color: isPlateSelected(1) ? "#5500FF00" : "#0000FF00"
        anchors.bottom: parent.bottom
        anchors.left: parent.left

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "1"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(1)
            }
        }
    }

    // Left middle
    Rectangle{
        width: square_width
        height: square_height
        color: isPlateSelected(2) ? "#5500FF00" : "#0000FF00"
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        //anchors.topMargin:parent.height * 0.25

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "2"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(2)
            }
        }
    }

    // Top left
    Rectangle{
        width: square_width
        height: square_height
        color: isPlateSelected(3) ? "#5500FF00" : "#0000FF00"
        anchors.top: parent.top
        anchors.left: parent.left

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "3"
        }
        
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
        color: isPlateSelected(4) ? "#5500FF00" : "#0000FF00"
        anchors.top: parent.top
        anchors.right: parent.right

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "4"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(4)
            }
        }
    }

    // Right middle
    Rectangle{
        width: square_width
        height: square_height
        color: isPlateSelected(5) ? "#5500FF00" : "#0000FF00"
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        //anchors.topMargin:parent.height * 0.25

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "5"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(5)
            }
        }
    }

    // Bottom right
    Rectangle{
        width: square_width
        height: square_height
        color: isPlateSelected(6) ? "#5500FF00" : "#0000FF00"
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "6"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(6)
            }
        }
    }


    // Start pos display

    Image {
        source: "../res/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(1)
        x: 0.25 * parent.width / 3.000 - width/2
        y: (1.75)  * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(2)
        x: 0.70 * parent.width / 3.000 - width/2
        y: 1.75 * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/arrow270.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(3)
        x: 0.25 * parent.width / 3.000 - width/2
        y: 0.25 * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/arrow270.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(4)
        x: 2.80 * parent.width / 3.000 - width/2
        y: (1.00 - 0.8) * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(5)
        x: 2.3 * parent.width / 3.000 - width/2
        y: 1.75 * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isPlateSelected(6)
        x: 2.75 * parent.width / 3.000 - width/2
        y: (1.00 + 0.80) * parent.height / 2.000 - height / 2
    }

    // Robot position
    Image {
        id: robot_shape
        source: "../res/robot.png"
        width: parent.width / 12
        height: parent.height / 12
        x: (zmqClient.robot_pose_y+ 1.500) * parent.width / 3.000 - width / 2
        y: (zmqClient.robot_pose_x) * parent.height / 2.000 - height / 2
        transform: Rotation { origin.x: robot_shape.width/2 ; origin.y: robot_shape.height/2; angle: 180 + ((-1) * (180 * zmqClient.robot_pose_yaw / Math.PI))}
    }


}
