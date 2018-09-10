# Create your views here.
from django.http import HttpResponse


def verpdf(request,archivo):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=/u01/home/julian/analiticas/analiticas/%s' % archivo
    return response