import QtQuick 2.4
import QtQuick.Controls 2.4
import QtGraphicalEffects 1.0
import QtQuick.Layouts 1.4

Item {
    id: statusBar
    width: parent.width
    height: parent.height / 12

    function getPowerStatus(){
        return !zmqClient.emergency_stop && zmqClient.config_status == 1
    }
    
    function getStmStatus(){
        return zmqClient.config_status == 1 && zmqClient.nucleo_responding
    }

    function getFPGAStatus(){
        return true
    }

    function getLidarStatus(){
        return zmqClient.rplidar_running
    }

    function getOdrvStatus(){
        return getStmStatus() && !zmqClient.odrv_axis0_error && !zmqClient.odrv_axis1_error
    }

    function getVisionStatus(){
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

    Rectangle {
        height: parent.height
        width: parent.width
        color: "#242424"

        Row {
            id: row
            height: parent.height
            spacing: 2

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            // HB display, heart blinks if heartbeat works properly
            Item {
                height: parent.height
                width: statusBar.width / 7
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

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            // Power display
            Item {
                id: power_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: power_icon
                    source: "../res/power.svg"
                    height: parent.height * 0.8
                    width: height
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
                    anchors.left: power_icon.right
                    anchors.leftMargin: parent.height / 4
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

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            // STM status display
            Item {
                id: stm_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: stm_icon
                    source: "../res/stm.png"
                    height: parent.height * 0.8
                    width: height
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
                    anchors.left: stm_icon.right
                    anchors.leftMargin: parent.height / 4
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

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            Item {
                id: fpga_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: fpga_icon
                    source: "../res/fpga.png"
                    height: parent.height * 0.8
                    width: height
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
                    anchors.left: fpga_icon.right
                    anchors.leftMargin: parent.height / 4
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

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            Item {
                id: odrv_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: odrv_icon
                    source: "../res/odrv.png"
                    height: parent.height * 0.8
                    width: height
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    antialiasing: true
                    visible: false
                }
                ColorOverlay{
                    anchors.fill: odrv_icon
                    source: odrv_icon
                    color: "white"
                    antialiasing: true
                }
                Image{
                    id: odrv_status_icon
                    source: getOdrvStatus() ? "../res/tick.svg" : "../res/cross.svg"
                    height: parent.height * 0.8
                    width: height
                    anchors.leftMargin: parent.height / 4
                    anchors.left: odrv_icon.right
                    anchors.verticalCenter: parent.verticalCenter
                    antialiasing: true
                    visible: false
                }
                ColorOverlay{
                    id: odrv_status_overlay
                    anchors.fill: odrv_status_icon
                    source: odrv_status_icon
                    color: getOdrvStatus() ? "#40bf80" : "#ff4d4d";
                    antialiasing: true
                    visible: true
                }
            }

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            Item {
                id: lidar_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: lidar_icon
                    source: "../res/lidar.png"
                    height: parent.height * 0.8
                    width: height
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    antialiasing: true
                }
                Image{
                    id: lidar_status_icon
                    source: getLidarStatus() ? "../res/tick.svg" : "../res/cross.svg"
                    height: parent.height * 0.8
                    width: height
                    anchors.leftMargin: parent.height / 4
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

            // Separator
            Rectangle{
                height: parent.height
                width: 2
                color: "#484848"
            }

            Item {
                id: vision_column
                height: parent.height
                width: statusBar.height * 2
                Image{
                    id: vision_icon
                    source: "../res/vision.svg"
                    height: parent.height * 0.8
                    width: height
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    antialiasing: true
                }
                ColorOverlay{
                    anchors.fill: vision_icon
                    source: vision_icon
                    color: "red"
                    antialiasing: true
                }
                Image{
                    id: vision_status_icon
                    source: getVisionStatus() ? "../res/tick.svg" : "../res/cross.svg"
                    height: parent.height * 0.8
                    width: height
                    anchors.leftMargin: parent.height / 4
                    anchors.left: vision_icon.right
                    anchors.verticalCenter: parent.verticalCenter
                    antialiasing: true
                    visible: false
                }
                ColorOverlay{
                    id: vision_status_overlay
                    anchors.fill: vision_status_icon
                    source: vision_status_icon
                    color: getVisionStatus() ? "#40bf80" : "#ff4d4d";
                    antialiasing: true
                    visible: true
                }
            }
        }
    }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:600;width:800}
}
##^##*/
