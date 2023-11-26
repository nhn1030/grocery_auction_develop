from django.shortcuts import render

# Create your views here.

##TODO static file (Settings folder 구성)
##TODO /request -> response render base.html (FIGMA base.html -> 왼쪽 툴바, 상단 메뉴바)
##TODO formfield djangoForm or vanilla html 기획
##TODO (심화) -> 유효성 검증 


def test(request):
    return render(request,'base.html',{})


# MVT 

# //**html**// html 
# <form>  
# django.model.form <a Textfield> <b Datefield> <c>

# //**view**// backend
# Seller.save(name=a,price=b,date=c)
# User.save(name=a,price=b,date=c)
# Buyer.save(name=a,price=b,date=c)

# DUE 12.7 
# ------
# //**view**//
# Product
# sub = Product.objects.filter(name_text__startswith ='서울')
# sub2 = sub.get(price<=input_price)
# render render(request,'base.html',sub2)


# /**html**//
# {% for i in sub2 %}
# {i.name}
# {i.price}
# {i.date}

# DUE 12.20 
