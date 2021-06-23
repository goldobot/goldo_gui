import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
    
    function getStatusColor(textColor){
        if(!textColor){
            switch(zmqClient.config_status){
                case 0:
                    return 'lightgray'
                case 1:
                    return 'green'
                case 2:
                    return 'red'
            }
        }
        else{
            switch(zmqClient.config_status){
                case 0:
                    return 'black'
                case 1:
                    return 'white'
                case 2:
                    return 'white'
            }
        }
    }
    
    function getSideColor(textColor){
        if(!textColor){
            switch(zmqClient.side){
                case 0:
                    return 'gray'
                case 1:
                    return 'blue'
                case 2:
                    return 'yellow'
            }
        }
        else {
            switch(zmqClient.side){
                case 0:
                    return 'black'
                case 1:
                    return 'white'
                case 2:
                    return 'black'
            }
        }
    }

    function isSideUndefined(){
        if(zmqClient.side == 0){
            return true
        }
        else{
            return false
        }
    }

    //Title bar, also displays warnings
    Rectangle{
        anchors.fill: parent
        color: "#222222"
        GridLayout {
            id: gridLayout
            anchors.fill: parent
            columnSpacing: 5
            rowSpacing: 5
            rows: 6
            columns: 2

            Rectangle {
                id: rectangle1
                color: isSideUndefined() || zmqClient.pavillon ? "#FF0000" : "#222222"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Layout.row: 0
                Layout.column: 0
                Label {
                    color: "white"
                    visible: isSideUndefined() || !zmqClient.pavillon == false ? true : false
                    text: "Configuration"
                    font.pixelSize: 44
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.top
                }
                Label {
                    id: warningSide
                    color: "white"
                    visible: isSideUndefined() ? true : false
                    text: "Warning : side is not selected"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: parent.bottom
                }
                Label {
                    id: warningPavillon
                    color: "white"
                    visible: !zmqClient.pavillon == false ? true : false
                    text: "Warning : Flag is not closed"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: warningSide.top
                }
                Label {
                    color: "white"
                    visible: isSideUndefined() || zmqClient.pavillon ? false : true
                    text: "Configuration"
                    font.pixelSize: 64
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
            
            // Config nucleo button
            Rectangle {
                color: getStatusColor(false)
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.configNucleo() }
                }
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: getStatusColor(true)
                    text: "Config nucleo"
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.configNucleo() }
                }
            }
            
            // Side button
            Rectangle {
                color: getSideColor(false)
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: getSideColor(true)
                    text: "Side"
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.side = (zmqClient.side + 1) % 3 }
                }
            }

            // Odrive calibration button
            Rectangle {
                color: zmqClient.odrive_error ? 'red': zmqClient.odrive_state == 11 ? 'green' : 'lightgreen'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "black"
                    text: "ODrive calib : " + zmqClient.odrive_state
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
				MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.odriveCalibration() }
                }
            }

            // Opponents number
            Rectangle {
                color: "#333333"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "black"
                    text: "Opponents : " + zmqClient.opponents_number
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        if(zmqClient.opponents_number == 1){
                            zmqClient.opponents_number = 2
                        }
                        else{
                            zmqClient.opponents_number = 1
                        }
                    }
                }
            }

            //Tirette state
            Rectangle {
                color: !zmqClient.tirette == 1 ? "lightgreen" : "red"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "black"
                    text: "Tirette"
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            //Emergency stop state
            Rectangle {
                color: zmqClient.emergency_stop ? 'red' : 'lightgreen' 
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "black"
                    text: "Emergency"
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
    }
}
