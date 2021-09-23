urlpatterns = [
    path('add/', AddBookView.as_view(), name='add')
]

# views.py
class AddBookView(FormView):

    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'

    # form_valid 对输入的值的类型，进行判断，并返回错误信息，
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




# forms
# 此处调用的是ModelForm,而非forms.Form
class AddForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'genre', 'author', 'isbn')

        # a widget is Django's representation of an HTML input element
        # attrs:A dictionary containing HTML attributes to be set on the rendered widget.
        # 也就是能够在页面中添加bootstrap的属性。
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'auth': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }


# template
# add.html
# 此处，form直接输出，无法进行样式的设计，所以，在form中通过小工具，widget的attrs，可以进行样式设计
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>