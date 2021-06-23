import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {

    function getCompassColor(textColor){
        if(!textColor){
            switch(zmqClient.compass){
                case 0:
                    return "red"
                case 1:
                    return "black"
                case 2:
                    return "white"
            }
        }
        else{
            if(zmqClient.compass == 2){
                return "black"
            }
            else{
                return "white"
            }
        }
    }

    function getCompassText(){
        switch(zmqClient.compass){
            case 0:
                return "?"
            case 1:
                return "N"
            case 2:
                return "S"
        }
    }

    Image {
        source: "../res/table.png"
        anchors.fill : parent
    }

    Rectangle {
        id: compass_rect
        width: parent.width / 10
        height: parent.height / 6.7
        color: getCompassColor(false)
        opacity: 0.7
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
    }
    Text {
        anchors.horizontalCenter: compass_rect.horizontalCenter
        anchors.verticalCenter: compass_rect.verticalCenter
        font.pixelSize: compass_rect.height / 2
        color: getCompassColor(true)
        text: getCompassText()
    }
}