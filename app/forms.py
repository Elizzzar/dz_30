from .models import Article, Video, Comment
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('__all__')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)