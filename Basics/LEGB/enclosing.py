# E - Enclosing Scope
# When a function is inside another function
# The inner function can access variables from the outer function

def school():
    subject = "Python"

    def student():
        student_name = "Koushik"
        print(f"{student_name} is studying {subject}")

    student()

school()