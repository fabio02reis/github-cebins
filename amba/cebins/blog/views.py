from django.db import models
from django.views.generic import DateDetailView, ListView
# DateDetailView(EXIBE UM POST), ListView(EXIBE VÁRIOS POSTS)
from django.views.generic import DetailView, ListView
# Importando classe criada no model(Post)
from .models import Post


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post   


