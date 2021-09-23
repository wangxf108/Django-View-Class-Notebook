# view
# 当系统维护的时候，将用户的请求，转移到其他页面
from django.views import View

class PostPreLoadTaskView(RedirectView):
    post = get_object_or_404(Post, pk=kwargs['pk'])


    post = Post.objects.filter(pk=kwargs['pk'])
    post.update(count=F('count') + 1)

    return super().get_redirect_url(*args, **kwargs)

class SinglePostView(TemplateView):
    template_name = "ex4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context



