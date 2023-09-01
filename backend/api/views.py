from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .models import Instructor
from .models import Department
from .models import Course
from .serializers import StudentSerializer
from .serializers import InstructorSerializer
from .serializers import DepartmentSerializer
from .serializers import CourseSerializer
# Create your views here.


@api_view(['GET'])
def index(request):
    return Response({
        'message': 'Welcome to the Student Portal API',
        'status': status.HTTP_200_OK
    })
    
# STUDENT CRUD
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({
        'message': 'List of all students',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })

@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
    except Student.DoesNotExist:
        return Response({
            'message': 'Student does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    return Response({
        'message': 'Student details',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })
    
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Student created successfully',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })
    return Response({
        'message': 'Student not created',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })

@api_view(['PUT'])
def student_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({
            'message': 'Student does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Student updated successfully',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
    return Response({
        'message': 'Student not updated',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })
    
@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({
            'message': 'Student does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    student.delete()
    return Response({
        'message': 'Student deleted successfully',
        'status': status.HTTP_200_OK
    })
    
    
# INSTRUCTOR CRUD

@api_view(['GET'])
def instructor_list(request):
    instructors = Instructor.objects.all()
    serializer = InstructorSerializer(instructors, many=True)
    return Response({
        'message': 'List of all instructors',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })

@api_view(['GET'])
def instructor_detail(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
        serializer = InstructorSerializer(instructor)
    except Instructor.DoesNotExist:
        return Response({
            'message': 'Instructor does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    return Response({
        'message': 'Instructor details',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })

@api_view(['POST'])
def instructor_create(request):
    serializer = InstructorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Instructor created successfully',
            'status': status.HTTP_201_CREATED,
            "data": serializer.data
        })
    return Response({
        'message': 'Instructor not created',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })

@api_view(['PUT'])
def instructor_update(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except Instructor.DoesNotExist:
        return Response({
            'message': 'Instructor does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    serializer = InstructorSerializer(instructor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Instructor updated successfully',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
    return Response({
        'message': 'Instructor not updated',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })

@api_view(['DELETE'])
def instructor_delete(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except Instructor.DoesNotExist:
        return Response({
            'message': 'Instructor does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    instructor.delete()
    return Response({
        'message': 'Instructor deleted successfully',
        'status': status.HTTP_200_OK
    })


# DEPARTMENT CRUD

@api_view(['POST'])
def department_create(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Department created successfully',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })
    return Response({
        'message': 'Department not created',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })

@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response({
        'message': 'List of all departments',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })
    
@api_view(['PUT'])
def department_update(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({
            'message': 'Department does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    serializer = DepartmentSerializer(department, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Department updated successfully',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
    return Response({
        'message': 'Department not updated',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })

@api_view(['DELETE'])
def department_delete(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({
            'message': 'Department does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    department.delete()
    return Response({
        'message': 'Department deleted successfully',
        'status': status.HTTP_200_OK
    })
    
# COURSE CRUD

@api_view(['POST'])
def course_create(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Course created successfully',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })
    return Response({
        'message': 'Course not created',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })
    
@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response({
        'message': 'List of all courses',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })
    
@api_view(['GET'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
    except Course.DoesNotExist:
        return Response({
            'message': 'Course does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    return Response({
        'message': 'Course details',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })
    
@api_view(['PUT'])
def course_update(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({
            'message': 'Course does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Course updated successfully',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
    return Response({
        'message': 'Course not updated',
        'status': status.HTTP_400_BAD_REQUEST,
        'data': serializer.errors
    })
    
@api_view(['DELETE'])
def course_delete(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({
            'message': 'Course does not exist',
            'status': status.HTTP_404_NOT_FOUND
        })
    course.delete()
    return Response({
        'message': 'Course deleted successfully',
        'status': status.HTTP_200_OK
    })
    

