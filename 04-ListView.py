# url
urlpatterns = [
    path('/', BookListView.as_view(), name='book-list'),
    path('g/<str:genre>', GenereView.as_view(), name='genre'),
]


# views.py

class IndexView(ListViews):
    # 只需要两行，就可以在home.html中显示数据了,达到和templateView同样的效果
    model = Books
    template_name = "home.html"

    # 如果定义了name，则在html 中默认不适object_list,而变成了books
    context_object_name = 'books'

    # 在同一页面看多少内容
    paginate_by = 4

    # 添加queryset,会在页面上只显示两个项目，和上面的paginate显示四个冲突，但是只会显示两个
    queryset = Books.objects.all()[:2]

    # override　father class method
    def get_queryset(self):
        # 如果此出发这么写，上面的querset = Books.objects.all()[:2]就不能用了
        return Books.objects.all()[:2]

# 新建一个类，来将书分类
class GenreView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):

        # 此处通过找到url中传进来的genre来找到对应的含有genre的book
        # 另外， icontains 可以避免英文字母大小写问题
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))



class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'


# home.html
{% for book in object_list %}   # 默认的是object_list
    <a href={% url 'books:book-detai' slug=book.slug %}>
    {{book.title|truncatechars:50}}
    {{book.genre}}
    {{book.isbn}}
    </a> 
{% endfor %}


# paginator 显示内容进行分页的时候
{% for contact in page_obj %}
    {# Each "contact" is a Contact model object. #}
    {{ contact.full_name|upper }}<br>
    ...
{% endfor %}

<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}
 
        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
