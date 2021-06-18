import QtQuick 2.4
import QtQuick.Controls 2.4
import QtGraphicalEffects 1.0
import QtQuick.Layouts 1.4

Item {
    id: statusBar
    width: 800
    height: 40

    function getPowerStatus(){
        return !zmqClient.emergency_stop
    }
    
    function getStmStatus(){
        return zmqClient.config_status == 1 && zmqClient.nucleo_responding
    }

    function getFPGAStatus(){
        return true
    }

    function getLidarStatus(){
        return true
    }

    function blinkHeartbeat(){
        if(Math.floor(zmqClient.heartbeat / 100) % 5 == 0){
            return true
        }
        else{
            return false
        }
    }

    Row {
        id: row
        height: parent.height
        spacing: 0

        Rectangle {
            id: hb_column
            height: parent.height
            width: statusBar.width / 4
            color: "#242424"
            Image{
                id: hb_icon
                source: "../res/heartbeat.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                anchors.fill: hb_icon
                source: hb_icon
                color: blinkHeartbeat() ? "#ffffff" : "#ff4d4d"
                antialiasing: true
            }
            Label{
                color: "white"
                text: Math.floor(zmqClient.heartbeat / 100)
                font.pixelSize: parent.height / 2
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                anchors.rightMargin: parent.height / 10
            }
        }

        Rectangle {
            id: power_column
            anchors.left: hb_column.right
            height: parent.height
            width: statusBar.width / 5
            color: "#242424"
            Image{
                id: power_icon
                source: "../res/power.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                anchors.fill: power_icon
                source: power_icon
                color: "yellow"
                antialiasing: true
            }
            Image{
                id: power_status_icon
                source: getPowerStatus() ? "../res/tick.svg" : "../res/cross.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: power_icon.right
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                id: power_status_overlay
                anchors.fill: power_status_icon
                source: power_status_icon
                color: getPowerStatus() ? "#40bf80" : "#ff4d4d";
                antialiasing: true
                visible: true
            }
        }

        Rectangle {
            id: stm_column
            anchors.left: power_column.right
            height: parent.height
            width: statusBar.width / 5
            color: "#242424"
            Image{
                id: stm_icon
                source: "../res/stm.png"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                anchors.fill: stm_icon
                source: stm_icon
                color: "#3399ff"
                antialiasing: true
            }
            Image{
                id: stm_status_icon
                source: getStmStatus() ? "../res/tick.svg" : "../res/cross.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: stm_icon.right
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                id: stm_status_overlay
                anchors.fill: stm_status_icon
                source: stm_status_icon
                color: getStmStatus() ? "#40bf80" : "#ff4d4d";
                antialiasing: true
                visible: true
            }
        }

        Rectangle {
            id: fpga_column
            anchors.left: stm_column.right
            height: parent.height
            width: statusBar.width / 5
            color: "#242424"
            Image{
                id: fpga_icon
                source: "../res/fpga.png"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                anchors.fill: fpga_icon
                source: fpga_icon
                color: "white"
                antialiasing: true
            }
            Image{
                id: fpga_status_icon
                source: getFPGAStatus() ? "../res/tick.svg" : "../res/cross.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: fpga_icon.right
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                id: fpga_status_overlay
                anchors.fill: fpga_status_icon
                source: fpga_status_icon
                color: getFPGAStatus() ? "#40bf80" : "#ff4d4d";
                antialiasing: true
                visible: true
            }
        }

        Rectangle {
            id: lidar_column
            anchors.left: fpga_column.right
            height: parent.height
            width: statusBar.width / 5
            color: "#242424"
            Image{
                id: lidar_icon
                source: "../res/lidar.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                anchors.fill: lidar_icon
                source: lidar_icon
                color: "red"
                antialiasing: true
            }
            Image{
                id: lidar_status_icon
                source: getLidarStatus() ? "../res/tick.svg" : "../res/cross.svg"
                height: parent.height * 0.8
                width: height
                anchors.leftMargin: parent.height / 10
                anchors.left: lidar_icon.right
                anchors.verticalCenter: parent.verticalCenter
                antialiasing: true
                visible: false
            }
            ColorOverlay{
                id: lidar_status_overlay
                anchors.fill: lidar_status_icon
                source: lidar_status_icon
                color: getLidarStatus() ? "#40bf80" : "#ff4d4d";
                antialiasing: true
                visible: true
            }
        }
    }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:600;width:800}
}
##^##*/
