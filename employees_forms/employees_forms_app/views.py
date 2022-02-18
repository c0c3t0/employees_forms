from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from employees_forms.employees_forms_app.models import Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Your name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control-lg'  # bootstrap
#             },
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=30,
#     )
#
#     age = forms.IntegerField(
#         # widget=forms.TextInput(
#             # attrs={'type': 'range'}),  # change default widget
#         validators=(
#             validate_positive,
#         )
#     )

class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError("This is a bot")

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(attrs={
                'readonly': 'readonly'
            })}


class EmployeeOrderByForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        ),
        # required=False,
    )


def home(request):
    return render(request, 'home.html')


def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('home')
    else:
        employee_form = EmployeeForm()

    employee_order_by_form = EmployeeOrderByForm(request.GET)
    employee_order_by_form.is_valid()
    order_by = employee_order_by_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_by_form': employee_order_by_form,
    }

    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)
