# This is a simple gradebook project based off a prompt and guidelines from Codecademy.
# Created by John Adam Gordon Whited

# Declaring and initializing 3 lists. One for last semesters grades and two for the current semester.
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

# This is to test my ability of using the .append() function to add to preexisting lists.
subjects.append('computer science')
grades.append(100)

# This is to combine the separate lists of subjects and grades.
gradebook = list(zip(subjects, grades))

# This is to test my ability to append() a zipped list of two preexisting list.
gradebook.append(('visual arts', 93))

# Printing the two separate grade lists for Winter 2019 and Spring 2020. This includes headers and formatting lines for code/console readability
print("The grades for Winter 2019 Semester")
print(last_semester_gradebook)
print(" ")
print("The grades for Spring 2020 Semester")
print(gradebook)
print(" ")

# Combining both the previous and current semester gradebooks into one full list containing all grades. This includes a print() header line for formatting.
full_gradebook = gradebook + last_semester_gradebook
print("The full Gradebook")
print(full_gradebook)

#End of Project. 4/1/2020


