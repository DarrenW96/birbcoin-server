from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        template = loader.get_template('register.html')
        context = {'form': form }
        return HttpResponse(template.render(context, request))
