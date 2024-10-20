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
    
    function getPrematchColor(textColor){
        if(!textColor){
            switch(zmqClient.match_state){
                case 0:
                    return 'lightgray'
                case 1:
                    return 'lightgreen'
                default:
                    return 'green'
            }
        }
        else{
            if(zmqClient.match_state >= 2){
                return 'white'
            }
            else{
                return 'black'
            }
        }
    }
    
    function getSideColor(textColor){
        if(!textColor){
            switch(zmqClient.side){
                case 0:
                    return 'lightgray'
                case 1:
                    return 'yellow'
                case 2:
                    return 'blue'
            }
        }
        else {
            switch(zmqClient.side){
                case 0:
                    return 'black'
                case 1:
                    return 'black'
                case 2:
                    return 'white'
            }
        }
    }

    //Propulsion button color
    function getPropulsionColor(textColor){
        if(!textColor){
            switch(zmqClient.propulsionControllerState) {
                case 0:
                    return 'lightgray'; // Inactive
                case 1:
                    return 'lightgreen'; // Stopped
                case 7:
                    return 'red'; // Error
                default:
                    return 'green'; // Moving
            }
        }
        else {
            switch(zmqClient.propulsionControllerState) {
                case 0:
                case 1:
                    return 'black'; // Inactive or stopped
                default:
                    return 'white'; // Error or moving
            }
        }
    }

    function getPropulsionStatus(){
        if(zmqClient.propulsionControllerState == 7) {
            switch(zmqClient.propulsionControllerError){
                case 1:
                    return 'EMERGENCY STOP';
                case 2:
                    return 'ROBOT BLOCKED';
                case 3:
                    return 'TRACKING ERROR';
                default:
                    return 'ERROR';
            }
        }
        else {
            switch(zmqClient.propulsionControllerState){
                case 0:
                    return 'Inactive';
                case 1:
                    return 'Stopped';
                case 2:
                    return 'Trajectory';
                case 3:
                    return 'Rotate';
                case 4:
                    return 'Reposition';
                case 5:
                    return 'Manual';
                case 6:
                    return 'Emergency stop';
                default:
                    return 'Unknown';
            }
        }
    }

    //Odrive button color
    function getOdrvColor(textColor){
        if(!textColor){
            if (!zmqClient.nucleo_responding || zmqClient.config_status != 1){
                return 'lightgray' //default color
            }
            else if(zmqClient.odrv_axis0_error || zmqClient.odrv_axis1_error){
                return 'red' //error color
            }
            else if(zmqClient.odrv_axis0_state == 0 || zmqClient.odrv_axis1_state == 0){
                return 'lightgreen' //odrive responding but not initialized yet color
            }
            else if(zmqClient.odrv_axis0_state == 6 || zmqClient.odrv_axis1_state == 6){
                return 'lightgreen' //odrive responding but initializing ongoing
            }
            else{
                return 'green' //everything ok color
            }
        }
        else {
            if (!zmqClient.nucleo_responding || zmqClient.config_status != 1){
                return 'black'
            }
            else if(zmqClient.odrv_axis0_error || zmqClient.odrv_axis1_error){
                return 'white'
            }
            else if(zmqClient.odrv_axis0_state == 0 || zmqClient.odrv_axis1_state == 0){
                return 'black'
            }
            else if(zmqClient.odrv_axis0_state == 6 || zmqClient.odrv_axis1_state == 6){
                return 'black'
            }
            else{
                return 'white'
            }
        }
    }

    function odrvStateToStr(state) {
        switch(state){
            case 0:
                return 'Undef';
            case 1:
                return 'Idle';
            case 2:
                return 'Start';
            case 3:
                return 'Full Calib';
            case 4:
                return 'Mot Calib';
            case 6:
                return 'Find idx';
            case 7:
                return 'Enc Calib';
            case 8:
                return 'Control';
            case 9:
                return 'Lockin';
            default:
                return 'Unknown';
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

    function isStartPlateUndefined(){
        if (zmqClient.start_zone_selected == 0) {
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
                color: isSideUndefined() || isStartPlateUndefined() ? "#FF0000" : "#222222"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Layout.row: 0
                Layout.column: 0
                Label {
                    color: "white"
                    visible: isSideUndefined() || isStartPlateUndefined() ? true : false
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
                    id: warningStart
                    color: "white"
                    visible: isStartPlateUndefined() ? true : false
                    text: "Warning : Start zone is not selected"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: warningSide.top
                }
                Label {
                    color: "white"
                    visible: isSideUndefined() || isStartPlateUndefined() ? false : true
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
                color: zmqClient.config_status ? 'green' : 'lightgray'
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.configNucleo() }
                }
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.config_status ? 'white' : 'black'
                    text: "Config Nucleo"
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

            // Propulsion
            Rectangle {
                color: getPropulsionColor(false)
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: getPropulsionColor(true)
                    text: "Propulsion :\n" + getPropulsionStatus()
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

            // Odrive calibration button
            Rectangle {
                color: getOdrvColor(false)
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: getOdrvColor(true)
                    text: "ODrive :\n" + odrvStateToStr(zmqClient.odrv_axis0_state) + " | " + odrvStateToStr(zmqClient.odrv_axis1_state)
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

            //Pre-match sequence
            Rectangle {
                color: getPrematchColor(false)
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: getPrematchColor(true)
                    text: "Pre-match sequence"
                    font.pixelSize: 32
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        onClicked: { zmqClient.preMatch() }
                    }
                }
            }

            //Tirette state
            Rectangle {
                color: !zmqClient.tirette == 1 ? "green" : "red"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: "white"
                    text: "Tirette"
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
