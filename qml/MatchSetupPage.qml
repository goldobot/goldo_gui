import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
  GridLayout {
    columns: 2
    Label { 
      text: "Heartbeat"
      font.pixelSize: 20
    }
    Label { 
      text: zmqClient.heartbeat
      font.pixelSize: 20
    }
    Label { 
      text: "Config Nucleo"
      font.pixelSize: 40
    }
    Rectangle {
      width: 40
      height: 40
      color: {0: 'lightgray', 1: 'green', 2: 'red'}[zmqClient.config_status]
      MouseArea {
        anchors.fill: parent
        onClicked: { zmqClient.configNucleo() }
      }
    }
    
    Label { 
      text: "Side"
      font.pixelSize: 80
    }
    Rectangle {
        width: 80
        height: 80
        color: 'lightgray'
        Rectangle {
          id: selectSide
          height:70
          width: 70
          anchors.horizontalCenter : parent.horizontalCenter 
          anchors.verticalCenter  : parent.verticalCenter  
          color: {0: 'gray', 1: 'blue', 2: 'yellow'}[zmqClient.side]
          MouseArea {
            anchors.fill: parent
            onClicked: { zmqClient.side = (zmqClient.side + 1) % 3 }
          }
        }
      }
    Label { 
      text: "PreMatch"
      font.pixelSize: 80
    }
    Rectangle {
      width: 80
      height: 80
      color: 'lightgray'
      Label {
        font.pixelSize: 40
        text: zmqClient.match_state
        anchors.horizontalCenter : parent.horizontalCenter 
        anchors.verticalCenter  : parent.verticalCenter        
      }
    MouseArea {
          anchors.fill: parent
          onClicked: { zmqClient.preMatch() }
        }
    }
    Label { 
      text: "ODrive calib"
      font.pixelSize: 80
    }
    Rectangle {
      width: 80
      height: 80
      color: zmqClient.odrive_error ? 'red': 'lightgreen'
      Label {
        font.pixelSize: 40
        text: zmqClient.odrive_state
        anchors.horizontalCenter : parent.horizontalCenter 
        anchors.verticalCenter  : parent.verticalCenter        
      }
    MouseArea {
          anchors.fill: parent
          onClicked: { zmqClient.odriveCalibration() }
        }
    }
  }
}
 
 