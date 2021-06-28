from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show, Network

#shows = Show.objects.all()
#show = Show.objects.get(id=show_id)

# INDEX
def index(request):
    return redirect('/shows')

# SHOWS
def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

# NEW
def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    
    if request.method == 'POST':
        print(request.POST)
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/new")
        else:
            Show.objects.create(title=request.POST['title'], release_date=request.POST['release_date'], network=request.POST['network'], description=request.POST['description'])
            return redirect("/")

# DETAILS
def details(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'details.html', context)

# EDIT
def edit(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    if request.method == 'GET':
        return render(request, 'edit.html', context)
    
    if request.method == 'POST':
        print(request.POST)
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else:
            show = Show.objects.get(id=show_id)
            show.title=request.POST['title']
            show.network=request.POST['network']
            show.description=request.POST['description']
            show.release_date=request.POST['release_date']
            show.save()
            return redirect(f"/shows/{show_id}")

# DELETE
def delete(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    Show.objects.get(id=show_id).delete()
    return redirect("/")

#import pdb; pdb.set_trace()