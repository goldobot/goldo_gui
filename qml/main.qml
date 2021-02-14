import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4
//import goldo 1.0


ApplicationWindow {
    visible: true
    //visibility: "FullScreen"
    //flags: Qt.FramelessWindowHint
    width: 800
    height: 480

    /*Rectangle    
    {
      id: leftPanel
      width:120
      height:parent.height
      anchors.left: parent.left
      anchors.top: parent.top
      color: 'blue'
      
      ColumnLayout
      {
      
      Rectangle {
        width: 120
        height: 120
        color: 'lightgray'        
        MouseArea {
          anchors.fill: parent
          onClicked: { stackLayout.currentIndex = (stackLayout.currentIndex + 1) % stackLayout.count }
        }
      }
      Rectangle {
        width: 120
        height: 120
        color: 'lightgray'        
      }
      Rectangle {
        width: 120
        height: 120
        color: zmqClient.tirette ? 'lightgray' : 'yellow'         
      }
      Rectangle {
        width: 120
        height: 120
        color: zmqClient.emergency_stop ? 'red' : 'lightgreen'        
      }
      }
    }*/
    
    
    /*SwipeView 
    {
        id: view
        anchors.fill: parent
        currentIndex: 0
        
        MatchSetupPage { }
        ScorePage { }
        CameraDisplayPage { }
    }

    PageIndicator {
      id: indicator

      count: view.count
      currentIndex: view.currentIndex

      anchors.bottom: view.bottom
      anchors.horizontalCenter: parent.horizontalCenter
    }*/

    StatusBar{
      id: statusBar
    }

    LeftMenu{
      id: leftMenu
      anchors.top: statusBar.bottom
    }

    StackLayout {
      id: layout
      height: 440
      width: 660
      anchors.bottom: parent.bottom
      anchors.right: parent.right

      currentIndex: leftMenu.getSelected()
      MatchSetupPage {          
      }
      Rectangle {
          color: 'plum'
          anchors.fill: parent
      }
      Rectangle {
          color: 'cyan'
          anchors.fill: parent
      }
      CupDisplayPage {
      }
      CameraDisplayPage {
      }
      ScorePage {        
      }
    }


    
}


