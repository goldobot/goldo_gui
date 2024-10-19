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
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 3
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: zmqClient.ip_address
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
            }

            Repeater {
                model: 12
                Rectangle {
                    color: 'lightgray'
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.columnSpan: 1
                    Layout.rowSpan: 1
                    Label {
                        color: zmqClient.left_lift ? 'white' : 'black'
                        text: index + 1
                        font.pixelSize: 24
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: { zmqClient.center_slot(index + 1) }
                    }
                }
            }
        }
    }
}
