import QtQuick 2.4
import QtQuick.Controls 2.4
import QtGraphicalEffects 1.0
import QtQuick.Layouts 1.4

Item {
    width: parent.width / 8
    height: parent.height - (parent.height/ 12)

    function isSelected(number){
        if(number == zmqClient.gui_screen_selected)
            return true
        else
            return false
    }

    function getSelected(){
        return selected
    }

    function setSelected(number){
        selected = number
    }

    Rectangle {
        id: leftMenuBar
        width: parent.width
        height: parent.height
        color: "#424242"

        Column {
            id: column
            width: 140
            height: 440
            spacing: 0

            Rectangle {
                id: match_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                color: isSelected(0) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Match"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(0)
                    }
                }
            }

            Rectangle {
                id: strat_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width                
                color: isSelected(1) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Strategy"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(1)
                    }
                }
            }

            Rectangle {
                id: control_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width                
                color: isSelected(2) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Control"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(2)
                    }
                }
            }

            Rectangle {
                id: status_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                color: isSelected(3) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Status"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(3)
                    }
                }
            }

            Rectangle {
                id: vision_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                color: isSelected(4) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Vision"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(4)
                    }
                }
            }

            Rectangle {
                id: score_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                color: isSelected(5) ? "#ff1a1a" : "#424242"

                Column{
                    //height: parent.height
                    width: parent.width
                    anchors.verticalCenter: parent.verticalCenter
                    
                    Label{
                        id: score_button_label
                        color: "white"
                        text: "Score"
                        font.pixelSize: (leftMenuBar.width / 6) * 0.8
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    Image{
                        id: star_icon
                        source: "../res/points.png"
                        height: 20
                        width: 20
                        antialiasing: true
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    Label{
                        color: "white"
                        text: zmqClient.score
                        font.pixelSize: (leftMenuBar.width / 6) * 0.8
                        anchors.leftMargin: 2 * star_icon.width
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        zmqClient.selectScreen(5)
                    }
                }
            }
        }
    }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:600;width:800}
}
##^##*/
