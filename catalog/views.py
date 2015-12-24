from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
# from django.http import HttpResponse
# from django.template import loader

def index(request):
  template_name = 'catalog/index.html'
  data = {'range':range(10)}
  # template = loader.get_template(template_name)
  return render_to_response(template_name, data, context_instance=RequestContext(request))
  # return HttpResponse(template.render(request))
