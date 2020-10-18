import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.1
ApplicationWindow {
    title: qsTr("Fenêtre de connexion")
    visible: true
    visibility: "FullScreen"
    flags: Qt.FramelessWindowHint
    width: 800
    height: 480

    
    Rectangle
    {
      id: leftPanel
      width:160
      height:parent.height
      color: 'blue'
      Rectangle
      {
        id: selectSide
        height:160
        width: 160
        color: {0: 'gray', 1: 'blue', 2: 'yellow'}[zmqClient.side]
        MouseArea {
        anchors.fill: parent
        onClicked: { zmqClient.side = (zmqClient.side + 1) % 3 }
    }
      }
    }
    Item
    {
        anchors.left: leftPanel.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    
        Label {
            id: login
            Layout.fillWidth: true
            anchors.horizontalCenter : parent.horizontalCenter 
            anchors.verticalCenter  : parent.verticalCenter  
            font.pixelSize: 240
            text: zmqClient.score
        }
    }

   
}
