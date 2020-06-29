from django.db.models import Count
from django.shortcuts import (render,
                                get_object_or_404,
                                redirect,
                                reverse,)
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required

from .forms import CommentForm,PostForm
from .models import Post, Category, Comment, Author


# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset



class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        featured = Post.objects.filter(featured=True)
        recent = Post.objects.order_by('-timestamp')[0:30]
        category_count = get_category_count()

        context = {
            'object_list': featured,
            'recent': recent,
            'category_count': category_count,

        }
        return render(request, "index.html", context)


class CanolaOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Canola Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class CoconutOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Coconut Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class CornOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Corn Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context


class CottonseedOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Cottonseed oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class OliveOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Olive Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class PalmOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Palm Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class PeanutOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Peanut Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class RapeseedOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Rapeseed Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context

class SunflowerOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Sunflower Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        
        context['category_count'] = category_count
        context['recent'] = recent
        return context




class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post-detail.html'
    context_object_name = 'post'
    form = CommentForm()

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['category_count'] = category_count
        context['recent'] = recent
        return context 

    def post(self, request,pk, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post 
                comment.save()
                
                return redirect(reverse("post-detail", kwargs={
                    'pk':post.pk
                }))
        else:
            form = CommentForm()

# class PostCategory(ListView):
#     model = Post
#     template_name = "posts/post-category.html"
    
#     def get_queryset(self):
#         category = get_object_or_404(Category, pk=self.kwargs['pk'])
#         return Post.objects.filter(categories=category)

#     def get_context_data(self,  **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = category
#         return context






