import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4
//import goldo 1.0


ApplicationWindow {
    visible: true
	  visibility: (windowed == true) ? "Windowed" : "FullScreen"
	  flags: (windowed == true) ? Qt.Window : Qt.FramelessWindowHint
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
      height: parent.height - statusBar.height
      width: parent.width - leftMenu.width
      anchors.bottom: parent.bottom
      anchors.right: parent.right

      currentIndex: leftMenu.getSelected()
      MatchSetupPage {          
      }
      StratPage {
      }
      Rectangle {
          color: 'cyan'
          height: parent.height
          width: parent.width
      }
      CupDisplayPage {
      }
      CameraDisplayPage {
      }
      ScorePage {        
      }
    }    
}


