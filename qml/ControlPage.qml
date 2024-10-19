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
            columns: 10

            Rectangle {
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 10
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Purge Carrousel"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.empty_carrousel() }
                }
            }

            Rectangle {
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 10
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Test Turbines"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.test_turbines() }
                }
            }

            Repeater {
                model:10
                Rectangle {
                    color: 'lightgray'
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.columnSpan: 1
                    Layout.rowSpan: 1
                    Label {
                        color: 'black'
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

            Rectangle {
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 10
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Check up actionneurs"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.check_actionneurs() }
                }
            }

            Rectangle {
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 10
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Changement de zone"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.change_zone() }
                }
            }

            Rectangle {
                color: 'lightgray'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 10
                Layout.rowSpan: 1
            }    
        }
    }
}
