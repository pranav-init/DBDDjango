from django.shortcuts import render,redirect
from .forms import NiceForm
from .models import Nice,Figure,Note
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
# def fun(Title):
#         #return int(Title[:4].replace('.',''))
#         return Title

class IndexView(ListView):
    model = Nice
    template_name = "homedupe.html"
    context_object_name = "posts"
    ordering = ['id']

class PageView(DetailView):
    model = Nice
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Nice.objects.all()
        context['images'] = Figure.objects.all()
        return context





# def home(request):
#     posts = Nice.objects.all()
    
#     paginator = Paginator(posts,1)

#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1
#     try:
#         posts = paginator.page(page)
#     except(EmptyPage,InvalidPage):
#         posts = paginator.page(paginator.num_pages)    
    
#     return render(request,'home.html',context={'posts':posts})

def create(request):
    
    notes = Note.objects.order_by('-id')
    
    if request.method=='POST':
        form = NiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/22/')
    else:
        form = NiceForm()

    return render(request,'create.html',context={'form':form,'notes':notes})