#task 1: create a tuple containing 5 city names 
cities = ("hyderabad", "mumbai", "chennai", "delhi", "bangalore")

#task 2:write a function that takes a tuple as an argument and returns first and last elements of the tuple
def first_last(t):
    return (t[0], t[-1])
numbers = (5, 15, 25, 35)
print(first_last(numbers))

#task3:Create a tuple of tuples, where each inner tuple contains a student's name and their corresponding grade
students = (
    ("John", 85),
    ("Alice", 92),
    ("Nesha", 78),
    ("kumar", 95)
)
print(students)

#task4:Implement a function that takes the tuple of tuples from the previous task and returns a new tuple with the students' names sorted in alphabetical order
def get_sorted_names(students):
    return tuple(sorted(student[0] for student in students))
students = (
    ("Ravi", 89),
    ("Priya", 92),
    ("Arun", 80)
)
print(get_sorted_names(students))

#task5:Practice tuple unpacking by writing a function that takes a tuple of 3 elements and assigns each element to a separate variable, then prints out the values of these variables.
def unpack_tuple(t):
    a, b, c = t
    print("first value:", a)
    print("second value:", b)
    print("third value:", c)
unpack_tuple((10, 20, 30))


