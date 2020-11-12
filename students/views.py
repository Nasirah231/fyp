from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Student

# Create your views here.
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {"students": students})

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = '__all__'
    success_message = "New student successfully added."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentCreateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
        return form 

class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['others'].widget = widgets.Textarea(attrs= {'rows': 2})
        return form
