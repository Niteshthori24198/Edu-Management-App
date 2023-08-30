from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .models import Instructor
from .serializers import StudentSerializer
from .serializers import InstructorSerializer
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
            'data': serializer.data
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
