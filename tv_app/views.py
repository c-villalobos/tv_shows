from django.shortcuts import render, HttpResponse, redirect
from .models import Show, Network

#shows = Show.objects.all()
#show = Show.objects.get(id=show_id)

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    
    if request.method == 'POST':
        print(request.POST)
        Show.objects.create(title=request.POST['title'], release_date=request.POST['release_date'], network=request.POST['network'], description=request.POST['description'])
        return redirect("/")
    
def details(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'details.html', context)

def edit(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    if request.method == 'GET':
        return render(request, 'edit.html', context)
    
    if request.method == 'POST':
        print(request.POST)
        show = Show.objects.get(id=show_id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.save()
        return redirect(f"/shows/{show_id}")

def delete(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    Show.objects.get(id=show_id).delete()
    return redirect("/")
