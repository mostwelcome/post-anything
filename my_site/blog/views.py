from django.views.generic import TemplateView, DetailView, FormView

from .forms import PostForms
from .models import Post


class HomePageView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context


class PostDetailedView(DetailView):
    template_name = 'blog/detail.html'
    print('here')
    model = Post


class AddPostView(FormView):
    template_name = 'blog/new_post.html'
    form_class = PostForms
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data['image'])
        new_post = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        return super().form_valid(form)
