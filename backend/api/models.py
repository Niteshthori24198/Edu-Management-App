from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

MAJOR_CHOICES = [
    ('Computer Science', 'Computer Science'),
    ('Engineering', 'Engineering'),
    ('Business', 'Business')
    # Add more choices as needed
]

class Student(models.Model):
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    major = models.CharField(max_length=100, choices=MAJOR_CHOICES)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)  
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    # You might want to add additional fields here

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Submission(models.Model):
    SUBMISSION_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Late', 'Late'),
        ('Graded', 'Graded')
    ]

    submission_date = models.DateField()
    status = models.CharField(max_length=20, choices=SUBMISSION_STATUS_CHOICES)
    remarks = models.TextField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
