from django.urls import path
from . import views

urlpatterns = [
    path('studentsmarks/', views.students_list),
    path('studentsmarks/<int:id>', views.students),
    path('employees/', views.employees),

]