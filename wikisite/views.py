from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View
from .forms import EditArticleForm,CreateArticleForm
from .models import Article
from django.urls import reverse_lazy
from django.db.models import F,Q
from django.core.paginator import Paginator


class IndexView(ListView):
    model = Article
    template_name='index.html'
    context_object_name = 'articles'
    paginate_by = 2


    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Главная страница'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleView(DetailView):
    model=Article
    context_object_name='article'
    template_name='article_detail.html'

    def post(self,request,pk):
        art = Article.objects.get(pk=int(pk))
        art.is_published=True
        art.save()
        current_arts = Article.objects.filter(Q(number=art.number)&~Q(pk=art.pk))
        # print(current_arts)
        for i in current_arts:
            i.is_published=False
            i.save()

        return redirect(art.get_absolute_url())
        
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Статья: ' + self.get_object().title
        context['versions'] = Article.objects.filter(Q(number=self.get_object().number),~Q(pk=self.get_object().pk))
        return context



class CreateArticleView(CreateView):
    form_class = CreateArticleForm
    model=Article
    template_name='article_edit.html'
    success_url=reverse_lazy('index')


class EditArticle(View):

    def get(self,request,*args,**kwargs):
        form = EditArticleForm(request.POST or None)
        title = 'Изменить запись'
        context= {
        'title':title,
        'form':form,
        }
        return render(request,'article_edit.html',context)


    def post(self,request,pk):

        art=Article.objects.get(pk=pk)
        art.is_published=False
        art.save()

        form = EditArticleForm(request.POST or None )
        if form.is_valid():
            article=form.save(commit=False)
            article.is_published = True
            article.version=art.version+1
            article.number=art.number
            article.save()

            return HttpResponseRedirect('/')