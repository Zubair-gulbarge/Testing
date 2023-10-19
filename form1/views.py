# appname/views.py
from django.shortcuts import render
from .forms import MyForm

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Do something with the data (e.g., save to a database)
    else:
        form = MyForm()

    return render(request, 'form_template.html', {'form': form})
