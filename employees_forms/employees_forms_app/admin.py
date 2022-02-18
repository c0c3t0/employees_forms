from django.contrib import admin

from employees_forms.employees_forms_app.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
