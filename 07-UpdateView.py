
# CreateView: Adds new objects/data to a database table
# UpdateView: Retrieve specific object/data. Add/Update the database

class BaseUpdateView(ModelFormMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)