function drawChart() {
var context = document.getElementById("scoreHistory").getContext("2d");

var data = 
{
    labels: ["1","2","3","4","5","6","7","8","9"],
    datasets:
    [
        {
            label: "player1",
            fillcolor: "rgba(0,100,100,0.5)",
            strokecolor: "rgba(0,0,0,1)",
            pointcolor: "rgba(100,100,100,1)",
            pointstrokecolor: "#f00",
            pointhighlightfill: "#fff",
            pointhighlightstroke: "rgba(0,100,0,1)",
            data: [1,2,3,3,3,4,4,5,5]
        },
        {
            label: "player2",
            fillcolor: "rgba(100,100,0,0.5)",
            strokecolor: "rgba(0,0,0,1)",
            pointcolor: "rgba(100,100,100,1)",
            pointstrokecolor: "#f00",
            pointhighlightfill: "#fff",
            pointhighlightstroke: "rgba(0,100,0,1)",
            data: [1,2,3,3,3,4,4,5,5]
        }
    ]
}
var options = {}

var scoreChart = new Chart(context).Line(data, options);
}
