# squirrel census
import pandas
colors = ['Gray', 'Cinnamon', 'Black']

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')



def count_colors(color):
    count = 0
    for fur_color in data['Primary Fur Color']:
        if fur_color == color:
            count +=1
    return count

color_count = {
    'Fur Color': colors,
    'Count': [count_colors(color) for color in colors]
}

data = pandas.DataFrame(color_count)
print(data)
data.to_csv('squirrel_count.csv')
