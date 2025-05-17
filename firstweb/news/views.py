from django.shortcuts import render,redirect
from .forms import NewsForm
from django.views.generic import DetailView, DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import News

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'post'

class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'anons', 'text']
    template_name = 'news/update_news.html'
    success_url = reverse_lazy('news_list')

class NewsDelete(DeleteView):
    model = News
    template_name = 'news/deletenews.html'


def news_home(request):
    news= News.objects.all()
    return render (request,'news/news_home.html',{'news': news})

def create(request):
    error=''
    if request.method == 'POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            error = "Заполните форму правильно,пожалуйста"
    form = NewsForm()

    context = {
        "form":form,
        'error': error
    }


    return render (request,"news/create.html",context)
