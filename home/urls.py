from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello),
    path("about/", views.checkAbout),
    path("cart/", views.checkCart),
    path("signup/", views.signup),
    path("signin/", views.signin),
    path("login/", views.login),
    path("productsList/",views.productsList),
    path("SubproductsList/",views.subproductsList),
    path("SubproductsCat/", views.subProductCat),
    path("addToCart/",views.addToCart),
    path("forget/", views.forget),
    path("return/", views.returnsOrder),

]
