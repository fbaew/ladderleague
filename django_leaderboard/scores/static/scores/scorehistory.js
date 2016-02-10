function drawSet() {
var game1 = document.getElementById("game1").getContext("2d");
var game2 = document.getElementById("game2").getContext("2d");
var data =
{
    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
    datasets:
    [
        {
            label: "player1",
            fillColor: "rgba(0,220,100,0)",
            strokeColor: "rgba(0,220,100,1)",
            pointColor: "rgba(100,100,100,0)",
            pointstrokeColor: "rgba(100,100,100,0)",
            pointHighlightFill: "rgba(100,100,100,0)",
            pointHighlightStroke: "rgba(0,100,0,0)",
            data: [0, 0, 1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 11, 11]
        },
        {
            label: "player2",
            fillColor: "rgba(100,100,100,0)",
            strokeColor: "rgba(220,100,100,1)",
            pointColor: "rgba(100,100,100,0)",
            pointstrokeColor: "rgba(100,100,100,0)",
            pointHighlightFill: "rgba(100,100,100,0)",
            pointHighlightStroke: "rgba(0,100,0,0)",
            data: [0, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13, 13, 14, 15, 16, 17, 17, 18, 19, 19, 19, 20, 20, 21]
        }
    ]
}
var options = {}
var game1Chart = new Chart(game1).Line(data,options);
var game2Chart = new Chart(game2).Line(data,options);
}
