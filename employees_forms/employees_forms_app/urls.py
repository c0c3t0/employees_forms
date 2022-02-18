from django.urls import path

from employees_forms.employees_forms_app.views import create_employee, edit_employee

urlpatterns = (
    path('create/', create_employee, name='create employee'),
    path('edit/<int:pk>/', edit_employee, name='edit employee'),
)
