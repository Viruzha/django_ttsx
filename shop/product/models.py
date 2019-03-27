from django.db import models

class tags(models.Model):
    # 标签名称
    
    tagname=models.CharField(u'标签名称',max_length=10)
    def __str__(self):
        return self.tagname

class kind(models.Model):
    '''商品种类类'''
    kname=models.CharField(u'种类名称',max_length=20)
    klogo=models.ImageField(u'种类logo图片',upload_to='kind/')
    def __str__(self):
        return self.kname



class product(models.Model):
    '''商品类'''
    # 商品名称
    name=models.CharField(u'商品名称',max_length=20)
    #商品价格
    price=models.DecimalField(u'商品原价',max_digits=10,decimal_places=2)
    # 商品折扣价格
    discprice=models.DecimalField(u'商品折扣价',max_digits=10,decimal_places=2)
    # 商品种类
    kind=models.ForeignKey(kind,on_delete='CASCADE')
    picture=models.ImageField(u'商品图片',upload_to='product/%Y/%M/')
    # 商品销售量
    sellcount=models.IntegerField(u'商品销量',default=0)
    # 商品浏览数
    viewcount=models.IntegerField(u'商品浏览量',default=0)
    # 商品上架时间
    time=models.DateTimeField(u'商品上架时间',auto_now_add=True)
    # 商品描述信息
    desc=models.TextField(u'商品描述')
    # 商品评论
    # comment
    # 商品在库数量
    pnumber=models.IntegerField(u'商品在库数量')
    # 商品星级,通过用户的评论得出默认为0
    star=models.IntegerField(u'商品星级',default=0)
    # 商品标签
    tag=models.ManyToManyField(tags)
    # 商品是否为首页推荐
    # homerecommend=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class homerecommend(models.Model):
    '''首页推荐商品类(因为推荐的图片与正常图片尺寸不一)'''
    hproduct=models.ForeignKey(product,on_delete='CASCADE')
    #带绿色
    hcomment1=models.CharField(u'绿推荐词1',max_length=4)
    hcomment2=models.CharField(u'绿推荐词2',max_length=4)
    # 不带绿色
    hcomment3=models.CharField(u'推荐词3',max_length=4)
    # 推荐图片
    himage=models.ImageField(u'推荐图片',upload_to='recommend/')
    def __str__(self):
        return self.hproduct.name

class user(models.Model):
    '''用户信息类'''
    # 用户头像图片
    uhead=models.ImageField(u'用户头像',upload_to='user/')
    # 用户姓名
    uname=models.CharField(u'用户昵称',max_length=15)
    # 用户邮箱
    ueaddress=models.CharField(u'用户邮箱',max_length=50)
    # 用户密码
    upassword=models.CharField(u'用户密码',max_length=16)
    # 用户上次登录时间
    uLastLoginTime=models.DateTimeField(u'用户上次登录时间',auto_now=True)
    # 用户生日
    uBrithday=models.DateTimeField(u'用户生日时间')
    # 用户购物车
    # ucart
    def __str__(self):
        return self.uname

class cart(models.Model):
    '''购物车类'''
    # 购物车中商品名
    cproduct=models.ForeignKey(product,on_delete='CASCADE')
    # 添加时间
    ctime=models.DateTimeField(auto_now_add=True)
    # 该商品由哪个用户添加
    cuser=models.ForeignKey(user,on_delete='CASCADE')
    # 该商品添加了多少个
    ccount=models.IntegerField(u'商品个数')
    # 是否已经购买
    pay=models.BooleanField(default=False)


class comment(models.Model):
    '''商品评论类'''
    # 评论用户
    cuser=models.ForeignKey(user,on_delete='CASCADE')
    # 评论星级
    cstar=models.IntegerField(u'评论星级')
    # 评论时间
    ctime=models.DateTimeField(u'评论时间',auto_now_add=True)
    # 评论商品
    cproduct=models.ForeignKey(product,on_delete='CASCADE')
    # 评论赞成数
    rate=models.IntegerField(u'评论赞成数')
    # 评论内容
    context=models.TextField(u'评论内容')
# Create your models here.



class recentview(models.Model):
    '''用户最近浏览项'''
    # 浏览用户
    vuser=models.ForeignKey(user,on_delete='CASCADE')
    # 浏览商品
    vproduct=models.ForeignKey(product,on_delete='CASCADE')
    # 浏览时间
    vtime=models.DateTimeField(u'浏览时间',auto_now_add=True)