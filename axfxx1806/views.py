from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import View

from axfxx1806.models import Wheel, Nav, MustBuy, Shop, Mainshow, FoodTypes, Goods, MyUser, MineBtns
from axfxx1806.my_util import get_unique_str
from axfxx1806.tasks import send_verify_mail

from django.core.cache import caches

cache = caches['confirm']
def index(req):
    pass


def home(req):
    wheels = Wheel.objects.all()
    menus = Nav.objects.all()
    musts = MustBuy.objects.all()
    shops = Shop.objects.all()
    mainshows = Mainshow.objects.all()
    result = {
        "title":"首页",
        "wheels": wheels,
        "menus":menus,
        "musts":musts,
        'shop0':shops[0],
        'shop1_3':shops[1:3],
        'shop3_7':shops[3:7],
        'shop_last':shops[7:],
        'mainshows':mainshows,

    }

    return render(req,'home/home.html',result)

# def market(req):
#     return redirect(reverse("axf:market_params", args=("104749", )))

def market_with_params(req, type_id, sub_type_id, order_type):

    # 获取所有的一级分类
    # print(sub_type_id)
    types = FoodTypes.objects.all()
    # 获取二级分类
    current_cate = types.filter(typeid=type_id)[0]
    # current_cate = types.filter(typeid=type_id).first()
    # print(current_cate)
    childtypenames = current_cate.childtypenames.split("#")
    # print(childtypenames)
    sub_types = [i.split(":") for i in childtypenames]
    # print(sub_types)
    # 根据typeid 搜索商品信息
    goods = Goods.objects.filter(
        categoryid=int(type_id)
    )

    # 根据二级分类的id 查询商品的数据
    # 注意类型
    if sub_type_id == '0':
        pass
    else:
        goods = goods.filter(childcid=int(sub_type_id))

    # 排序
    """
    0  不排序
    1 价格
    2 销量
    """
    NO_SORT = 0
    PRICE_SORT = 1
    SALES_SORT = 2
    if int(order_type) == 0:
        pass
    elif int(order_type) == 1:
        goods = goods.order_by("price")
    else:
        goods = goods.order_by("productnum")

    result = {
        "title": "闪购",
        "types": types,
        "goods": goods,
        "current_type_id": type_id,
        "sub_types": sub_types,
        'current_sub_type_id':sub_type_id,
        'order_type':int(order_type),
    }
    return render(req, "market/market.html", result)
def cart(req):
    result = {
        "title":"购物车"
    }

    return render(req,'cart/cart.html',result)

@login_required(login_url="/axf/login/")
def mine(req):
    btns = MineBtns.objects.filter(is_used=True)
    user = req.user
    is_login = True
    if isinstance(user,AnonymousUser):
        is_login = False
    u_name = user.username if is_login else ""
    icon = 'http://'+req.get_host()+'/static/uploads/'+user.icon.url if is_login else ''

    result = {
        "title":"我的",
        " btns":btns,
        "is_login":is_login,
        'u_name':u_name,
        'icon':icon
    }
    return render(req, 'mine/mine.html', result)



class RegisterAPI(View):
    def get(self,req):
        return render(req,'user/register.html')

    def post(self,req):
        parans = req.POST
        icon = req.FILES.get("u_icon")
        name = parans.get("u_name")

        pwd = parans.get("u_pwd")
        confirm_pwd = parans.get("u_confirm_pwd")
        email = parans.get("email")

        if pwd and confirm_pwd and pwd == confirm_pwd:
            if MyUser.objects.filter(username = name).exists():
                return render(req,'user/register.html',{"help_msg":"该用户已存在"})
            else:
                user = MyUser.objects.create_user(
                    username = name,
                    password = pwd,
                    email = email,
                    is_active = False,
                    icon = icon
                )

                url = "http://"+req.get_host()+"/axf/confirm/"+get_unique_str()
                send_verify_mail.delay(url,user.id,email)
                return render(req,'user/login.html')





class LoginAPI(View):
    def get(self,req):
        return render(req,'user/login.html')
    def post(self,req):
#
        params = req.POST
        name = params.get("name")
        pwd = params.get("pwd")
        if not name or not pwd:
            data = {
                "code":2,
                'msg':"账号或者密码不能为空",
                "data":""
            }
            return JsonResponse(data)
        user = authenticate(username=name,password=pwd)
        if user:
            login(req,user)
            data = {
                'code':1,
                "msg":"ok",
                "data":"/axf/mine"

            }
            return JsonResponse(data)
        else:
            data = {
                'code':3,
                "msg":"账户或者密码错误",
                'data':''
            }
            return JsonResponse(data)

class LogoutAPI(View):
    def get(self,req):
        logout(req)
        return redirect(reverse("axf:mine"))

def confirm(req,uuid_str):
#     去缓存那东西，拿到的话修改
# is_active字段，没拿到返回验证失败
    user_id = cache.get(uuid_str)
    if user_id:
        user = MyUser.objects.get(pk = int(user_id))
        user.is_active = True
        user.save()
        return redirect(reverse("axf:login"))
    else:
        return HttpResponse("<h2>链接已失效</h2>")

