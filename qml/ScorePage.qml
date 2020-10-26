import QtQuick 2.4
import QtQuick.Controls 2.4

Page {    
  Label {
    anchors.horizontalCenter : parent.horizontalCenter 
    anchors.verticalCenter  : parent.verticalCenter  
    font.pixelSize: 320
    text: zmqClient.score
  }
  Label {
    anchors.top: parent.top
    anchors.right: parent.right
    font.pixelSize: 80
    text: zmqClient.match_timer
    }
}

