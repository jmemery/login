from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, 'logreg/index.html')


def register(request):
	result = User.objects.register(request.POST)

	if isinstance(result, list):
		for err in result:
			messages.add_message(request, messages.ERROR, err)
		return redirect('/')

	request.session['id'] = result.id
	request.session['name'] = result.first_name

	return redirect('/success')

def login(request):
	result = User.objects.login(request.POST)

	if isinstance(result, str):
		messages.add_message(request, messages.ERROR, result)
		return redirect('/')

	request.session['id'] = result.id
	request.session['name'] = result.first_name

	return redirect('/success')


def success(request):
	if not 'id' in request.session:
		return redirect('/')
	return render(request, 'logreg/success.html')

def logout(request):
	request.session.clear()
	return redirect('/')