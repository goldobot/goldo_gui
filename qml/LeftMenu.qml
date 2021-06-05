import QtQuick 2.4
import QtQuick.Controls 2.4
import QtGraphicalEffects 1.0
import QtQuick.Layouts 1.4

Item {
    property var selected: 0

    function isSelected(number){
        if(number == selected)
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
        width: 140
        height: 440
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
                anchors.top: parent.top
                
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
                        setSelected(0)
                    }
                }
            }

            Rectangle {
                id: strat_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                anchors.top: match_button.bottom
                
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
                        setSelected(1)
                    }
                }
            }

            Rectangle {
                id: control_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                anchors.top: strat_button.bottom
                
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
                        setSelected(2)
                    }
                }
            }

            Rectangle {
                id: status_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                anchors.top: control_button.bottom
                
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
                        setSelected(3)
                    }
                }
            }

            Rectangle {
                id: vision_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                anchors.top: status_button.bottom
                
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
                        setSelected(4)
                    }
                }
            }

            Rectangle {
                id: score_button
                height: leftMenuBar.height / 6
                width: leftMenuBar.width
                anchors.top: vision_button.bottom
                
                color: isSelected(5) ? "#ff1a1a" : "#424242"

                Label{
                    color: "white"
                    text: "Score"
                    font.pixelSize: (leftMenuBar.width / 6) * 0.8
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        setSelected(5)
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
