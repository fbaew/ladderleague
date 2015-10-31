function drawChart() {
var context = document.getElementById("demo").getContext("2d");

var data = 
{
    labels: ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"],
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
            data: [1,2,3,3,3,4,4,5,5]
        },
        {
            label: "player2",
            fillColor: "rgba(220,100,100,0.5)",
            strokeColor: "rgba(0,0,0,1)",
            pointColor: "rgba(100,100,100,1)",
            pointstrokeColor: "#f00",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(0,100,0,1)",
            data: [0,0,0,1,2,2,3,3,4]
        }
    ]
}
var options = {}

var scoreChart = new Chart(context).Line(data, options);
}
