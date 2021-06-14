import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4
//import goldo 1.0


ApplicationWindow {
    visible: true
	  visibility: (windowed == true) ? "Windowed" : "FullScreen"
	  flags: (windowed == true) ? null : Qt.FramelessWindowHint
    width: 800
    height: 480

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
      width: 700
      anchors.bottom: parent.bottom
      anchors.right: parent.right

      currentIndex: leftMenu.getSelected()
      MatchSetupPage {          
      }
      StratPage {
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


