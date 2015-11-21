function drawWins() {
var game1 = document.getElementById("winRecord").getContext("2d");
var data =
{
    labels: ["Wins","Losses"],
    datasets:
    [
        {
            label: "regulationGames",
            fillColor: "rgba(0,220,100,0.2)",
            strokeColor: "rgba(0,220,100,1)",
            pointColor: "rgba(100,100,100,1)",
            pointstrokeColor: "#abc",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(0,100,0,1)",
            data: [10,3]
        },
        {
            label: "casualSets",
            fillColor: "rgba(0,100,220,0.2)",
            strokeColor: "rgba(0,220,100,1)",
            pointColor: "rgba(100,100,100,1)",
            pointstrokeColor: "#abc",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(0,100,0,1)",
            data: [25,12]
        },
    ]
}
var options = {}
var game1Chart = new Chart(game1).Bar(data,options);
}
