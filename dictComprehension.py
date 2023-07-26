import random

names = ['andrew', 'peter', 'diana', 'anna', 'Pavel', 'Artem']

students = {student: random.randint(20, 100) for student in names}
print(students)
passed_students = {student: score for (student, score) in students.items() if score >= 50}
print(passed_students)

# to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "The surprising list of actors who were up to play Ken in ‘Barbie’"

result = {word: len(word) for word in sentence.split()}

print(result)

# create a dictionary called weather_f that takes each temperature in degrees Celcius and converts it into degrees Farenheight.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 19,
    "Saturday": 21,
    "Sunday": 17
}

weather_f = {day: (temp_c*9/5 + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)