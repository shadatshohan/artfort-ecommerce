from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Tags
from math import ceil

# Create your views here.
def home(request):
	allProd=[]
	catprod=Product.objects.values('id','category')
	cats={item['category'] for item in catprod}
	cats=list(cats)
	cats.insert(0,'upper')
	catsnew=list(dict.fromkeys(cats))
	print(catsnew)
	for cat in catsnew:
		prod=Product.objects.filter(category=cat)
		n=len(prod)
		nSlides=(n//4)+ceil((n/4)-(n//4))
		allProd.append([prod,range(1,nSlides),nSlides])
	params={'allProd':allProd}
	return render(request,'ecommerce/home.html',params)