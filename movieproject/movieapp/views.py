from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


'''# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "index.html", context)
    
'''

class Movielistview(ListView):
    model = Movie
    template_name = "index.html"
    context_object_name = "movies"

'''
def detail(request, movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
'''
class Moviedetailview(DetailView):
    model=Movie
    template_name="detail.html"
    context_object_name="movie"

'''
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect("/")

    return render(request,'add.html')
'''
class Movieaddview(CreateView):
    model = Movie
    template_name = "add.html"
    fields = ['name','desc','year','img']
    success_url = reverse_lazy('movieapp:index')

class Movieupdateview(UpdateView):
    model=Movie
    template_name="add.html"
    fields=['name','desc','year','img']
    success_url=reverse_lazy('movieapp:index')

class Moviedeleteview(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('movieapp:index')

'''   
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
'''

'''def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')'''
