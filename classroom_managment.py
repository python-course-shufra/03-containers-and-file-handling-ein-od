classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if email == None:
        email = name.lower()+'@example.com'

    student = {}
    student['name'] = name
    student['email'] = email
    student['grade'] = []
    classroom.append( student )


def get_index(name):
    index = -1
    for item in classroom:
        index += 1
        if item.get('name') == name:
            return index


def delete_student(name):
    """Delete a student from the classroom"""
    del classroom[get_index(name)]


def set_email(name, email):
    """Sets the email of the student"""
    classroom[get_index(name)]['email'] = email


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    classroom[get_index(name)]['grades'].append((profession, grade))

def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """

    count_grades_of_profession = 0
    sum_grades_of_profession = 0
    student_grades = classroom[get_index(name)]['grades']
    for grade in student_grades:
        if grade[0] == profession:
            count_grades_of_profession += 1
            sum_grades_of_profession += grade[1]
    return sum_grades_of_profession / count_grades_of_profession 

def get_professions(name):
    """Returns a list of unique professions that student has grades in"""

    student_grades = classroom[get_index(name)]['grades']
    student_professions = set()
    for grade in student_grades:
        student_professions.add(grade[0])
    return list(student_professions)
print(get_professions('Charlie'))