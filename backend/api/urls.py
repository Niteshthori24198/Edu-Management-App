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
    path('api/instructors', views.instructor_list, name='instructor-list'),
    path('api/instructors/<int:pk>', views.instructor_detail, name='instructor-detail'),
    path('api/instructors/create', views.instructor_create, name='instructor-create'),
    path('api/instructors/<int:pk>/update', views.instructor_update, name='instructor-update'),  
    path('api/instructors/<int:pk>/delete', views.instructor_delete, name='instructor-delete'),
    
    # DEPARTMENT CRUD
    path('api/department/create', views.department_create, name='department-create'),
    path("api/departments",views.department_list,name="department-list"),
    path('api/departments/update/<int:pk>/', views.department_update),
    path('api/departments/delete/<int:pk>/', views.department_delete),
    
    # COURSE CRUD
    path('api/courses', views.course_list, name='course-list'),
    path('api/courses/<int:pk>', views.course_detail, name='course-detail'),
    path('api/courses/create', views.course_create, name='course-create'),
    path('api/courses/<int:pk>/update', views.course_update, name='course-update'),
    path('api/courses/<int:pk>/delete', views.course_delete, name='course-delete'),
]
