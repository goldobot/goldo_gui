import QtQuick 2.4
import QtQuick.Controls 2.4

Page {    
    Image {
        source: "../res/Goldorak.jpg"
        anchors.fill : parent
    }
	Rectangle {
        color: "black"
		opacity: 0.5
        anchors.fill : parent
    }
    Label {
        color : "white"
        style : Text.Outline
        styleColor : "black"
        anchors.horizontalCenter : parent.horizontalCenter 
        anchors.verticalCenter  : parent.verticalCenter  
        font.pixelSize: 320
        text: zmqClient.score
    }
    Label {
        color : "white"
        style : Text.Outline
        styleColor : "black"
        anchors.top: parent.top
        anchors.right: parent.right
        font.pixelSize: 80
        text: zmqClient.match_timer
    }
}

