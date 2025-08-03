"""Question: Create a class named Course with attributes course_name and students
(a list of student names). Add methods to enroll a student, drop a student,
and list all students.
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what classes and methods you need
# - Start with a simple implementation
# - Test your code step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What attributes does the Course class need?
# - What methods should you implement for enrolling and dropping students?
# - How do you handle the case when trying to drop a student who isn't enrolled?
#
# Remember: Start simple and build up complexity gradually!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's solve this problem step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Define the Course class
# ===============================================================================

# Explanation:
# Let's start by creating our Course class. In Python, we use the 'class' keyword
# followed by the class name. Class names should follow PascalCase convention.

class Course:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Course class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method is called when we create a new instance of the class.
# It's where we initialize the object's attributes. The 'self' parameter refers to the instance being created.

class Course:
    def __init__(self, course_name):
        # We'll add attribute assignments next
        pass

# What we accomplished in this step:
# - Added the constructor method to initialize new instances


# Step 3: Initialize the attributes
# ===============================================================================

# Explanation:
# Now let's assign the parameters to instance attributes. We'll store the course name
# and initialize an empty list for students.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # Start with an empty list of students

# What we accomplished in this step:
# - Initialized the course_name attribute
# - Initialized an empty students list


# Step 4: Add the enroll_student method
# ===============================================================================

# Explanation:
# Now let's add the enroll_student method that adds a student to the course.
# This method will append the student name to our students list.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

# What we accomplished in this step:
# - Added the enroll_student method to add students to the course


# Step 5: Add the drop_student method
# ===============================================================================

# Explanation:
# Now let's add the drop_student method that removes a student from the course.
# We should check if the student is enrolled before trying to remove them.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def drop_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

# What we accomplished in this step:
# - Added the drop_student method with proper error checking


# Step 6: Add the list_students method
# ===============================================================================

# Explanation:
# Finally, let's add the list_students method that returns all enrolled students.
# This method simply returns the students list.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def drop_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def list_students(self):
        return self.students

# What we accomplished in this step:
# - Added the list_students method to view all enrolled students


# Step 7: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our Course class and test it to make sure everything works correctly.
# This demonstrates how to use the class we just created.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def drop_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def list_students(self):
        return self.students

# Test our class:
course = Course("Python Programming")
course.enroll_student("Alice")
course.enroll_student("Bob")
course.enroll_student("Charlie")
print("Students after enrollment:", course.list_students())

course.drop_student("Alice")
print("Students after dropping Alice:", course.list_students())

# What we accomplished in this step:
# - Created and tested our complete Course implementation


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications
#
# Remember: The best way to learn is by doing!
# ===============================================================================