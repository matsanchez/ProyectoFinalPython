from django.views.generic import TemplateView


# Create your views here.
class AboutMeView(TemplateView):
    template_name = 'core/about.html'
