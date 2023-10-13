from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('<h1>Redirected</h1>')
        else:
            form = AuthenticationForm()
        return render(request, 'todo_app/base.html', {'form': form})

