from django.shortcuts import render
from django.http import HttpResponse

from home.services import ProductDetails, cartInfo, cartInformation, cartLen, cartcalculate, check, loginValidation, productSelected, subPud, subsubProd

# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello world")
    # pass this max upto 8 elements
    cardinfo = cartInformation()
    items = cartLen()
    return render(request, 'homepage/home.html', {'cardData': cardinfo, 'items': items})

# def user(request):
#     data = request.POST.get('name')
#     return render(request, 'home.html', {'name': data})

def checkAbout(request):
    cardinfo = ["1","2","3","4","5","6"]
    return render(request, 'pages/about.html', {'cardData': cardinfo})

def checkCart(request):
    cartData = cartInfo()
    total = cartcalculate(cartData)
    return render(request, 'shopping/cart.html', {'cartInfo': cartData, "total": total})

 
def signup(request):
    return render(request, 'authentication/signup.html')

def productsList(request):
    try:
        name = productSelected(request.GET.get("id"))
        information = ProductDetails(request.GET.get("id"))
    except:
        print("Error")
        return HttpResponse("Failed")

    # return HttpResponse(information)
    return render(request, "shopping/products.html", {'products': information, 'name':name})

def subproductsList(request):
    name = request.GET.get("id")
    items = subPud(name)
    return render(request, "shopping/subproducts.html", {'products': items, 'name':name})

def subProductCat(request):
    name = request.GET.get("id")
    items = subsubProd(name)
    return render(request, "shopping/subproductscat.html", {'products': items, 'name':name})

def addToCart(request):
    if check(request.POST.get('name'), request.POST.get('product')):
        cartData = cartInfo()
        total = cartcalculate(cartData)
        return render(request, "shopping/cart.html", {'cartInfo': cartData, "total":total})
    else:
        return HttpResponse("Failed")
    # name = request.POST.get('product')
    # print(name)

def signin(request):
    return render(request, 'authentication/signin.html')

def login(request):
    print("working")
    user = request.POST.get('username')
    password = request.POST.get('password')
    if loginValidation(user,password):
        return HttpResponse("success")
    else:
        error_msg = "Please check the credentials"
        return render(request, 'authentication/signin.html', {'error': error_msg})


def forget(request):
    return render(request, 'authentication/fotgetPass.html')

def returnsOrder(request):
    return render(request, 'return.html')

def error_404_view(request, exception):
    return render(request, "errors/404.html")