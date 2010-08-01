from cms.plugin_base import CMSPluginBase
from example.samplesearch.models import Search
from django.core.context_processors import request
from example.samplesearch.forms import SearchForm

class CMSSearchPlugin(CMSPluginBase):
    name = _("Search")
    model = Search
    render_template = 'templates/search.html'

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.GET.get('q', None) is not None:
            form = SearchForm(request.GET)

        if form.is_valid():
            results = form.search()

            context.update({
                'form': form,
                'search': instance,
                'results': results,
                'q': request.GET['q'],
            })

            return context

        else:
            form = SearchForm()


        context.update({
            'search': instance,
            'form': form,
        })

        return context

