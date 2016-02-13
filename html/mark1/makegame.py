import random
scores = [["0"],["0"]]
while int(scores[0][-1]) < 21 and int(scores[1][-1]) < 21:
    rand = int(random.random()*2)
    scores[rand].append(str(int(scores[rand][-1])+1))
    scores[rand-1].append(scores[rand-1][-1])

labels = []
labels = [str(x) for x in range(len(scores[0]))]

print('function drawChart() {')
print('var game1 = document.getElementById("game1").getContext("2d");')
print('var game2 = document.getElementById("game2").getContext("2d");')
print('var data =')
print('{')
print('    labels: {},'.format(labels))
print('    datasets:')
print('    [')
print('        {')
print('            label: "player1",')
print('            fillColor: "rgba(0,220,100,0.2)",')
print('            strokeColor: "rgba(0,220,100,1)",')
print('            pointColor: "rgba(100,100,100,1)",')
print('            pointstrokeColor: "#abc",')
print('            pointHighlightFill: "#fff",')
print('            pointHighlightStroke: "rgba(0,100,0,1)",')

tmp = []
for i in scores[0]:
    tmp.append(int(i))
print('            data: {}'.format(tmp))

print('        },')


print('        {')
print('            label: "player2",')
print('            fillColor: "rgba(100,100,100,0.5)",')
print('            strokeColor: "rgba(220,100,100,1)",')
print('            pointColor: "rgba(100,100,100,1)",')
print('            pointstrokeColor: "#abc",')
print('            pointHighlightFill: "#fff",')
print('            pointHighlightStroke: "rgba(0,100,0,1)",')
tmp = []
for i in scores[1]:
    tmp.append(int(i))
print('            data: {}'.format(tmp))

print('        }')
print('    ]')
print('}')
print('var options = {}')
print('var game1Chart = new Chart(game1).Line(data,options);')
print('var game2Chart = new Chart(game2).Line(data,options);')
print('}')
