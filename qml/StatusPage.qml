import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
    Rectangle{
        anchors.fill: parent
        color: "#222222"
        GridLayout {
            id: gridLayout
            anchors.fill: parent
            columnSpacing: 5
            rowSpacing: 5
            rows: 6
            columns: 3

            Rectangle {
                color: zmqClient.left_lift ? 'green' : 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.left_lift ? 'white' : 'black'
                    text: "Ascenseur G"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            Rectangle {
                color: zmqClient.right_lift ? 'green' : 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.right_lift ? 'white' : 'black'
                    text: "Ascenseur D"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }    

            Rectangle {
                color: zmqClient.left_lift ? 'green' : 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.left_lift ? 'white' : 'black'
                    text: "Ascenseur G"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            Rectangle {
                color: zmqClient.right_lift ? 'green' : 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.right_lift ? 'white' : 'black'
                    text: "Ascenseur D"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            Rectangle {
                color: zmqClient.tirette ? 'green' : 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                Label {
                    color: zmqClient.tirette ? 'white' : 'black'
                    text: "Tirette"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }    
        }
    }
}
