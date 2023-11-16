from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from app.forms import ArticleForm, VideoForm, CommentForm
from app.models import Article, Video, Comment
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.

class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
    success_url = reverse_lazy('List_all')

class VideoCreate(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'add_video.html'
    success_url = reverse_lazy('List_all')

class List_all(ListView):
    model = Article
    template_name = 'List_all.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_object = article
            comment.save()
            return redirect('article', pk=article.pk)
        else:
            return render(request, self.template_name, {'article': article, 'comment_form': form})


class VideoDetail(DetailView):
    model = Video
    template_name = 'video.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        video = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_object = video
            comment.save()
            return redirect('video', pk=video.pk)
        else:
            return render(request, self.template_name, {'video': video, 'comment_form': form})
        

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'article_delete'
    success_url = reverse_lazy('List_all')

class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video_detail.html'
    context_object_name = 'video_delete'
    success_url = reverse_lazy('List_all')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('List_all')

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'video_update.html'
    success_url = reverse_lazy('List_all')
