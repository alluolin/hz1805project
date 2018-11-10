from django.conf.urls import url

from axfxx1806 import views
from axfxx1806.views import home, cart, mine, market_with_params, RegisterAPI, LoginAPI, LogoutAPI, confirm

urlpatterns = [
    url(r'^index/',views.index),
    url(r"^home/", home, name="home"),
    # url(r"^mark]\et$", market, name="market"),
    url(r"^cart/", cart, name="cart"),
    url(r"^mine/", mine, name="mine"),
    url(r"^market_with_params/(\d+)/(\d+)/(\d+)", market_with_params, name="market_params"),
    url(r"^register/",RegisterAPI.as_view(),name="register"),
    url(r"^login/",LoginAPI.as_view(),name="login"),
    url(r"^logout/",LogoutAPI.as_view(),name="logout"),
    url(r"^confirm/(.*)",confirm),
]