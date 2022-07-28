# list comprehension
nums = [3, 6, 9, 12, 56, 46, 78, 97, 102, 135]

# square numbers
squares = [num ** 2 for num in range(6)]
print(squares)

# filtering evens
evens = [num for num in nums if num % 2 == 0]
print(evens)

with open('file1.txt') as file1:
    data1 = file1.readlines()


with open('file2.txt') as file2:
    data2 = file2.readlines()

union = [int(num) for num in data1 if num in data2]
print(union)

# dictionary comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence = sentence.split(' ')
result = {word:len(word) for word in sentence}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def temp_to_f(temp):

    return (temp * 9/5) + 32

weather_f = {day:temp_to_f(temp) for day, temp in weather_c.items()}

print(weather_f)

# iterating over pandas dataframe
import pandas

student_dict = {
    "student": ['Alan', 'Bob', 'Clive'],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for k, v in student_data_frame.items():
    print(k)

for index, row in student_data_frame.iterrows():
    print(index)

for index, row in student_data_frame.iterrows():
    if row.student == 'Alan':
        print(row.score)


