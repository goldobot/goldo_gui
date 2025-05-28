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
            columns: 6

            Rectangle {
                color: 'lightgreen'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Compressor ON"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.start_compressor() }
                }
            }

            Rectangle {
                color: '#ff7579'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Compressor OFF"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.stop_compressor() }
                }
            }

            Rectangle {
                color: 'red'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 2
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "Purge"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.purge() }
                }
            }

            Rectangle {
                color: 'lightgreen'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 3
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "All valves ON"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.all_valves_on() }
                }
            }

            Rectangle {
                color: '#ff7579'
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.columnSpan: 3
                Layout.rowSpan: 1
                Label {
                    color: 'black'
                    text: "All valves OFF"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { zmqClient.all_valves_off() }
                }
            }

            Repeater {
                model:12
                Rectangle {
                    color: 'lightgreen'
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.columnSpan: 1
                    Layout.rowSpan: 1
                    Label {
                        color: 'black'
                        text: "EV " + (index + 1)
                        font.pixelSize: 30
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: { zmqClient.valve_on(index + 1) }
                    }
                }
            }

            Repeater {
                model:12
                Rectangle {
                    color: '#ff7579'
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.columnSpan: 1
                    Layout.rowSpan: 1
                    Label {
                        color: 'black'
                        text: "EV " + (index + 1)
                        font.pixelSize: 30
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: { zmqClient.valve_off(index + 1) }
                    }
                }
            }
        }
    }
}
