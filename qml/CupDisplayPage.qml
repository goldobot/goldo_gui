import QtQuick 2.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Page {
    property var list_left : [2,2,1,-1]
    property var list_right : [1,0,1,2]
    function getLeftCup(index){
        //switch (zmqClient.list_left[index]){
        switch (list_left[index]){
            case -1:
                return "../res/no_cup.png"
            case 0:
                return "../res/unknown_cup.png"
            case 1:
                return "../res/red_cup.png"
            case 2:
                return "../res/green_cup.png"
        }
    }

    function getRightCup(index){
        //switch (zmqClient.list_right[index]){
        switch (list_right[index]){
            case -1:
                return "../res/no_cup.png"
            case 0:
                return "../res/unknown_cup.png"
            case 1:
                return "../res/red_cup.png"
            case 2:
                return "../res/green_cup.png"
        }
    }

    GridLayout {
        id: gridLayout
        anchors.fill: parent
        columnSpacing: 0
        rowSpacing: 0
        rows: 10
        columns: 2  
        
        Image {
            source: getLeftCup(3)
        } 
        Image {
            source: getRightCup(3)
        }    
        Image {
            source: getLeftCup(2)
        } 
        Image {
            source: getRightCup(2)
        }
        Image {
            source: getLeftCup(1)
        } 
        Image {
            source: getRightCup(1)
        }
        Image {
            source: getLeftCup(0)
        } 
        Image {
            source: getRightCup(0)
        }    
    }
}
