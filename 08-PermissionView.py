from django.contrib.auth.mixins import PermissionRequiredMixin

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticate):
            return redirect_to_login(self.request.get_full_path(),
                                    self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            retrun redirect('/books')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class BookEditView(PermissionRequiredMixin, UpdateView):

    raise_exception = False
    permission_required = 'books.change_books'
    permission_denied_message = "aad or something"
    login_url = '/books/'
    redirect_field_name = 'next'

    model = Books
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'