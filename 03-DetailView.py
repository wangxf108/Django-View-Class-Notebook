# model.py

Class Books(models.Modle):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    anthor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    count = models.IntegerField(null=True, default=0)

# urls.py

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    # or you can find 'id' not 'slug'
    path ('<id:id>/', BookDetailView.as_view(), name='book-detail'),
]

# views.py
class IndexView(TemplateView):
    
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 将Books里面的内容，放到关键字books中，然后在html中调用books.titleなど
        context['books'] = Books.objects.all()
        return context


# home.html
{% for book in books %}
    # ****此处重点，将slug定义为book里的slug，然后从此页面中取得slug，
    # 在view中，用slug找到对应的book
    <a href={% url 'books:book-detai' slug=book.slug %}>
        # 【|】是个过滤器，truncatechars，截断字符，超过的部分用。。。代替
        {{book.title|truncatechars:50}}
        {{book.genre}}
        {{book.isbn}}
    </a>

{% endfor %}





# views.py
class BookDetailView(DetailView):
    # 指定数据库
    model = Books
    # 指定对应的页面
    template_name = 'book-detail.html'
    # 默认不指定的话，是object,在页面中object.title など
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context

# 接上面的view
# book-detail.html
{% extends "../base.html" %}
{% block content %}
    # 已经在view中指定了该页面中object的名字，为book
    {{book.title}}
    {{book.genre}}
    {{book.isbn}}
    {{time}}
{% endblock %}