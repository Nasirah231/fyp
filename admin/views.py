from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        
    context = {'form': form}
    return render(request, 'admin/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username: request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'admin/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#STUDENT

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
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
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
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
       # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

#STAFF


class StaffListView(ListView):
    model = Staff


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staffs/staff_detail.html"


class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Staff
    fields = '__all__'
    success_message = 'New staff successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffCreateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = Staff
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffDeleteView(DeleteView):
  model = Staff
  success_url = reverse_lazy('staff-list')
