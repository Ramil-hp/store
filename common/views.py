class TitleMixin:
    title = None

    def get_context_data(self,**kwargs):
        # In order for the basic geth to work
        context = super(TitleMixin,self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
