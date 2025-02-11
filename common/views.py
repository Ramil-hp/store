class TitleMixin:
    title = None

    def get_context_data(self,**kwargs):
        # Для того чтобы работал основной гет
        context = super(TitleMixin,self).get_context_data(**kwargs)
        context['title'] = self.title
        return context