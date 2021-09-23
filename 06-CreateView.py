
# views.py
class AddBookView(CreateView):
    model = Books
    fields = ['title']
    # 此时，form_class 已经不需要了，可以添加上面的fields, 因为此时并不对所有属性进行修改，所以只列出field中一个对象，
    # 在下面的get_initial函数中，对initial中的title部分进行修改。
    # form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        # initial 代表的是template中，form里面，title里显示的初始值，不需要在html中定义。
        initial['title'] = 'Enter Title'
        return initial





# forms
# forms.py  与FormView 中定义的form相同
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