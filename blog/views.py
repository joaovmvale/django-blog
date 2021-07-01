from django.views.generic import DetailView, ListView #List -> Lista varios | Detail -> Lista um

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post