from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    # STUDENT CRUD
    path('api/students/', views.student_list, name='student-list'),
    path('api/students/<int:pk>/', views.student_detail, name='student-detail'),
    path('api/students/create/', views.student_create, name='student-create'),
    path('api/students/update/<int:pk>/', views.student_update, name='student-update'),
    path('api/students/delete/<int:pk>/', views.student_delete, name='student-delete'),
    
    # INSTRUCTOR CRUD
    path('api/instructors/', views.instructor_list, name='instructor-list'),
    path('api/instructors/<int:pk>/', views.instructor_detail, name='instructor-detail'),
    path('api/instructors/create', views.instructor_create, name='instructor-create'),
    path('api/instructors/update/<int:pk>/', views.instructor_update, name='instructor-update'),  
    path('api/instructors/delete/<int:pk>/', views.instructor_delete, name='instructor-delete'),
    
]
