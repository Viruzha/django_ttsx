from django.shortcuts import render
from product.models import product,kind,homerecommend


def index(request):
    homrecomm=homerecommend.objects.all()
    allkinds=kind.objects.all()
    newproduct=product.objects.order_by('time')
    return render(request,'index.html',
    context={
        'listrecommand':homrecomm,
        'allkinds':allkinds,
        'newproduct':newproduct
        })




# Create your views here.
