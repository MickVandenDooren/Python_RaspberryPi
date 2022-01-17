import pygal

temp = []

file = open('weather.txt','r')
    
for line in file.read().splitlines():
    if line:
        temp.append(float(line))
file.close()

weather = pygal.Line()
weather.add('temp',temp)


weather.title = 'Weather'
weather.x_labels = range(1, len(temp) +1)

weather.render()