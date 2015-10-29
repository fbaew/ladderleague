function drawChart() {
var context = document.getElementById("scoreHistory").getContext("2d");
var data =
{
    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    datasets:
    [
        {
            label: "player1",
            fillColor: "rgba(0,220,100,0.2)",
            strokeColor: "rgba(0,220,100,1)",
            pointColor: "rgba(100,100,100,1)",
            pointstrokeColor: "#abc",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(0,100,0,1)",
            data: [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 10, 11, 12, 13, 13, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 17, 17]
        },
        {
            label: "player2",
            fillColor: "rgba(220,100,100,0.5)",
            strokeColor: "rgba(220,100,100,1)",
            pointColor: "rgba(100,100,100,1)",
            pointstrokeColor: "#abc",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(0,100,0,1)",
            data: [0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 15, 16, 17, 18, 19, 19, 20, 20, 21]
        }
    ]
}
var options = {}
var scoreChart = new Chart(context).Line(data,options);
}
