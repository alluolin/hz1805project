from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    email = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='邮箱')
    address = models.CharField(
        max_length=251,
        verbose_name='地址',
        null=True)
    phone = models.CharField(
        max_length=13,
        verbose_name='手机号',
        unique=True)
    icon = models.ImageField(
        upload_to="icon",
        null=True)

class BaseData(models.Model):
    img = models.CharField(max_length=201)
    name = models.CharField(max_length=40)
    trackid = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Wheel(BaseData):

    class Meta:
        db_table = "axf_wheel"


class Nav(BaseData):

    class Meta:
        db_table = "axf_nav"
class MustBuy(BaseData):

    class Meta:
        db_table = "axf_mustbuy"

# insert into axf_mainshow(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3) values("21782","优选水果","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg","103532","爱鲜蜂","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q","103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q","103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");

class Shop(BaseData):

    class Meta:
        db_table = "axf_shop"


class Mainshow(BaseData):
    categoryid = models.CharField(
        max_length=100
    )
    brandname = models.CharField(
        max_length=100
    )

    img1 = models.CharField(
        max_length=255
    )
    childcid1 = models.CharField(
        max_length=100
    )
    productid1 = models.CharField(
        max_length=100
    )
    longname1 = models.CharField(
        max_length=100
    )
    price1 = models.CharField(
        max_length=100
    )
    marketprice1 = models.CharField(
        max_length=100
    )

    img2 = models.CharField(
        max_length=255
    )
    childcid2 = models.CharField(
        max_length=100
    )
    productid2 = models.CharField(
        max_length=100
    )
    longname2 = models.CharField(
        max_length=100
    )
    price2 = models.CharField(
        max_length=100
    )
    marketprice2 = models.CharField(
        max_length=100
    )
    img3 = models.CharField(
        max_length=255
    )
    childcid3 = models.CharField(
        max_length=100
    )
    productid3 = models.CharField(
        max_length=100
    )
    longname3 = models.CharField(
        max_length=100
    )
    price3 = models.CharField(
        max_length=100
    )
    marketprice3 = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = "axf_mainshow"

# insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);

class FoodTypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=30)
    childtypenames = models.CharField(max_length=255)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'

# insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);

class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=255
    )
    productname = models.CharField(
        max_length=130
    )
    productlongname = models.CharField(
        max_length=190
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.IntegerField()
    specifics = models.CharField(
        max_length=40
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    marketprice = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    categoryid = models.IntegerField(

    )
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=30
    )
    dealerid = models.CharField(
        max_length=30
    )
    storenums = models.IntegerField(
        verbose_name="库存"
    )
    productnum = models.IntegerField(
        verbose_name="销量"
    )
    class Meta:
        db_table = "axf_goods"

class Cart(models.Model):
    user = models.ForeignKey(MyUser)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)
    crteate_time = models.DateTimeField(auto_now_add=True)
    upload_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=True)
    class Meta:
        verbose_name = "购物车"
        index_together = ['user','goods']


class MineBtns(models.Model):
    btn = models.CharField(max_length=30)
    class_name = models.CharField(max_length=100)
    bref_url = models.CharField(max_length=255,null=True)
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否正在使用"
    )
    class Meta:
        verbose_name = "我的页面的下一排按钮"
    




