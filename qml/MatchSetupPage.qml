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
                color: "#222222"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Layout.row: 0
                Layout.column: 0
                Label {
                    color: "white"
                    text: "Configuration"
                    font.pixelSize: 64
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
            
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
                    text: "Pre-match config"
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

            Rectangle {
                color: "#333333"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "black"
                    text: "PreMatch : " + zmqClient.match_state
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            Rectangle {
                color: zmqClient.Tirette == 1 ? "lightgreen" : "red"
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