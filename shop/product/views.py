import base64
import datetime
from django.shortcuts import render
from product.models import product, kind, homerecommend, user, recentview, tags
from django.db.models import Q
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
def index(request):
    # 使用cookie进行类session通信
    def renderr(userid):
        homrecomm = homerecommend.objects.all()
        allkinds = kind.objects.all()
        newproduct = product.objects.order_by('time')
        # print(newproduct[0].id)
        topsell = product.objects.order_by('sellcount')[:3]
        recentviews = recentview.objects.filter(
            vuser__usessionid=userid).order_by('-vtime')[:3]
        return render(request, 'index.html',
                      context={
                          'listrecommand': homrecomm,
                          'allkinds': allkinds,
                          'newproducts': newproduct,
                          'topseller': topsell,
                          'recentviews': recentviews,
                          'topnew': newproduct[:3]
                      }
                      )
    if request.COOKIES.get('usession'):
        userid = request.COOKIES.get('usession')
    else:
        userid = str(base64.b64encode(
            ('vistor'+str(datetime.datetime.now())).encode('utf8')), encoding='utf8')  # 游客访问
        request.session['usession'] = userid
        user.objects.create(usessionid=userid, uname='vistor', uVistor=True)
        response = renderr(userid)
        response.set_cookie('usession', userid,max_age=3600*24)#cookie仅存活１天
        return response

    recentviews = recentview.objects.filter(
        vuser__usessionid=userid).order_by('-vtime')[:3]
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    return renderr(userid)


def SinglePage(request, i):
    sproduct = product.objects.get(id=i)
    inproducts = product.objects.all().order_by('?')[:4]
    newproduct = product.objects.all().order_by('time')[:5]
    tags = sproduct.tag.all()
    kindproducts = product.objects.filter(kind=sproduct.kind).order_by('?')[:3]
    userid = request.COOKIES.get('usession')
    userid=user.objects.get(usessionid=userid)
    vr=recentview.objects.filter(Q(vproduct_id=i)&Q(vuser_id=userid.id))
    allkinds = kind.objects.all()
    # print(vr)
    if  len(vr)==0:
        recentview.objects.create(vproduct_id=i, vuser_id=userid.id)
    else:
        vr[0].vproduct_id=i#更新访问时间
        vr[0].save()
    return render(request, 'single-product.html', context={
        'product': sproduct,
        'allkinds': allkinds,
        'inproducts': inproducts,
        'newproducts': newproduct,
        'tags': tags,
        'kindproducts': kindproducts
    })


def search(request):
    pass

def addtocart(request,i):
    pass

def allproducts(request):
    allproducts=product.objects.all()
    allkinds = kind.objects.all()
    return render(request,'shop.html',context={
        'allproducts':allproducts,
        'allkinds':allkinds
    })
# Create your views here.
