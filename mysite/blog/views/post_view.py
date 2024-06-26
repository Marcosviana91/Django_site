from django.views import generic
from blog.models import Post

# Create your views here.

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"