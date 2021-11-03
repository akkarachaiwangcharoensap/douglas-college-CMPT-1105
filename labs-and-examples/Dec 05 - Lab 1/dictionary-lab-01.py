numberOfCourses = int(input("How many courses?"))

courses = {}

for index in range(numberOfCourses):
	keyInput = input("Enter a course number")
	valueInput = input("Enter a room for " + keyInput)
	courses[keyInput] = valueInput

print(courses)
