import QtQuick 2.4
import QtQuick.Controls 2.4

Page {    
    Image {
        source: "../res/goldo_detect.png"
        anchors.fill : parent
    }

    Label {
        color : "white"
        style : Text.Outline
        styleColor : "black"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.pixelSize: 96
        text: "DETECTION !"
    }
}