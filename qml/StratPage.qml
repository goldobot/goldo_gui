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
    
    function isStartZoneSelected(index){
        if(index == zmqClient.start_zone_selected)
            return true
        else
            return false
    }

    // Table vinyl
    Image {
        source: "../res/map/table.png"
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
            x: (modelData.y+1.500) * parent.width / 3.000 - width/2
            y: (modelData.x) * parent.height / 2.000 - height / 2
            Label {
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: parent.height / 2
                color: "black"
                text: modelData.quality
            }
        }
    }

    // Available start zones
    // Bottom left
    Rectangle{
        width: square_width
        height: square_height
        color: isStartZoneSelected(1) ? "#AAFFCC88" : "#55FFFFFF"
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.leftMargin:parent.width * 0.335

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "1"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneDA_J"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(1)
            }
        }
    }

    // Middle left
    Rectangle{
        width: square_width
        height: square_height
        color: isStartZoneSelected(2) ? "#AA3333FF" : "#55FFFFFF"
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: parent.height * 0.45

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "2"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneDL_B"
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
        color: isStartZoneSelected(3) ? "#AAFFCC88" : "#55FFFFFF"
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.leftMargin:parent.width * 0.05

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "3"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneA_J"
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
        color: isStartZoneSelected(4) ? "#AA3333FF" : "#55FFFFFF"
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.rightMargin:parent.width * 0.05

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "4"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneA_B"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(4)
            }
        }
    }

    // Middle right
    Rectangle{
        width: square_width
        height: square_height
        color: isStartZoneSelected(5) ? "#AAFFCC88" : "#55FFFFFF"
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.topMargin: parent.height * 0.45

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "5"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneDL_J"
        }
        
        MouseArea {
            anchors.fill: parent
            onClicked: {
                zmqClient.selectPlate(5)
            }
        }
    }

    // Top right
    Rectangle{
        width: square_width
        height: square_height
        color: isStartZoneSelected(6) ? "#AA3333FF" : "#55FFFFFF"
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.rightMargin: parent.width*0.335

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 3
            opacity: 0.5
            color: "black"
            text: "6"
        }
        Label {
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.rightMargin:parent.width/10
            anchors.bottomMargin:parent.height/30
            font.pixelSize: parent.height / 6
            opacity: 1
            color: "white"
            text: "ZoneDA_B"
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
        source: "../res/map/arrow270.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(1)
        x: 0.50 * parent.width / 3.000 - width/2
        y: (1.55)  * parent.height / 2.000 - height / 2
    }

    Rectangle{
        width: (0.25) * parent.width / 3.000
        height: (0.45) * parent.height / 2.000
        color: "#CC943C3C"
        visible: isStartZoneSelected(1)
        x: 0.0* parent.width / 3.000 //- width/2
        y: (1.6)  * parent.height / 2.000 - height / 2

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 4
            opacity: 0.5
            color: "white"
            text: "CALE"
        }
    }

    Image {
        source: "../res/map/arrow180.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(2)
        x: 0.2 * parent.width / 3.000 - width/2
        y: 1.75 * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/map/arrow270.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(3)
        x: 0.50 * parent.width / 3.000 - width/2
        y: (0.6)  * parent.height / 2.000 - height / 2
    }

    Rectangle{
        width: (0.25) * parent.width / 3.000
        height: (0.45) * parent.height / 2.000
        color: "#CC943C3C"
        visible: isStartZoneSelected(3)
        x: 0.0* parent.width / 3.000 //- width/2
        y: (0.68)  * parent.height / 2.000 - height / 2

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 4
            opacity: 0.5
            color: "white"
            text: "CALE"
        }
    }

        Image {
        source: "../res/map/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(4)
        x: 2.50 * parent.width / 3.000 - width/2
        y: (0.6)  * parent.height / 2.000 - height / 2
    }

    Rectangle{
        width: (0.25) * parent.width / 3.000
        height: (0.45) * parent.height / 2.000
        color: "#CC943C3C"
        visible: isStartZoneSelected(4)
        x: 3.000* parent.width / 3.000 - width
        y: (0.68)  * parent.height / 2.000 - height / 2

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 4
            opacity: 0.5
            color: "white"
            text: "CALE"
        }
    }

    Image {
        source: "../res/map/arrow180.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(5)
        x: 2.8 * parent.width / 3.000 - width/2
        y: 1.75 * parent.height / 2.000 - height / 2
    }

    Image {
        source: "../res/map/arrow90.png"
        opacity: 0.7
        width: parent.width / 5
        height: parent.height / 3
        visible: isStartZoneSelected(6)
        x: 2.50 * parent.width / 3.000 - width/2
        y: (1.55)  * parent.height / 2.000 - height / 2
    }

    Rectangle{
        width: (0.25) * parent.width / 3.000
        height: (0.45) * parent.height / 2.000
        color: "#CC943C3C"
        visible: isStartZoneSelected(6)
        x: 3.00 * parent.width / 3.000 - width
        y: (1.6) * parent.height / 2.000 - height / 2

        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: parent.height / 4
            opacity: 0.5
            color: "white"
            text: "CALE"
        }
    }

    // Robot position
    Image {
        id: robot_shape
        source: "../res/map/robot.png"
        width: parent.width / 12
        height: parent.height / 12
        x: (zmqClient.robot_pose_y+ 1.500) * parent.width / 3.000 - width / 2
        y: (zmqClient.robot_pose_x) * parent.height / 2.000 - height / 2
        transform: Rotation { origin.x: robot_shape.width/2 ; origin.y: robot_shape.height/2; angle: 180 + ((-1) * (180 * zmqClient.robot_pose_yaw / Math.PI))}
    }


}
