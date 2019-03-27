from django.contrib import admin
from product.models import tags,kind,product,user,cart,comment,homerecommend







admin.site.register(homerecommend)
admin.site.register(tags)
admin.site.register(kind)
admin.site.register(product)
admin.site.register(user)
admin.site.register(cart)
admin.site.register(comment)
# Register your models here.
