from django.shortcuts import render
from django.http import HttpResponse
from .trans import trans
from .models import Goods, User
import json

# Create your views here.

def index(request):
	return render(request,'index.html')

def translate(request):  #翻译
	from_lang = request.GET.get('from_lang')
	print(from_lang)
	to_lang = request.GET.get('to_lang')
	text = request.GET.get('words')
	return HttpResponse(trans(text, from_lang, to_lang))


def news_list(request, choose):
	new_type = {'1': '经济', '2': '教育'}
	new_titles = []
	if choose == '1':
		new_titles = [('12/5', '作者成为全国首富。'), ('12/4', '作者成为全省首富。'),('12/3', '作者成为全市首富。'), ('12/2', '作者成为镇里首富。'), ('12/1', '作者成为村里首富。')]
	return render(request, 'news_list.html', context={choose: new_type[choose], 'new_titles': new_titles})

def filter_test(request):
	return render(request, 'filter.html', context={'letters': 'abc', 'number': 1})

def search_all(request):
	goods_list = Goods.objects.all()
	return render(request, 'search_result.html', context={'goods_list': goods_list})

def search_name(request):
	goods_name = request.GET.get('goods_name')
	goods_list = Goods.objects.filter(goods_name=goods_name)  # 完全匹配
	# goods_list = Goods.objects.get(goods_name=goods_name)# 查询满足条件的一个结果（查询到多个结果时异常）
	# goods_list = Goods.objects.filter(goods_name__contains=goods_name)  # 模糊匹配搜索关键字
	return render(request, 'search_result.html', context={'goods_list': goods_list})

def search_price(request):
	min_price = request.GET.get('min_price')
	max_price = request.GET.get('max_price')

	goods_list = Goods.objects.filter(goods_price__gt=min_price,goods_price__lt=max_price)
	# goods_list = Goods.objects.filter(Q(goods_price=0.5) | Q(goods_price=2.4)) # 满足任何一个条件
	return render(request, 'search_result.html', context={'goods_list':goods_list})

def searchsort(request):
    sort = {'all_asc': Goods.objects.order_by('goods_price'),  # 查询全部结果后升序排列
            'all_desc': Goods.objects.order_by('-goods_price'),  # 查询全部结果后降序排列
            'result_asc': Goods.objects.filter(goods_price__lt='5').order_by('goods_price')  # 对小于5查询结果排序
            }
    return render(request, 'search_result.html', {'goods_list': sort[request.GET.get('sort')]})

def reg(request):
	return render(request, 'register.html')

def check(request):
	user_name = request.GET.get('user_name')
	user = User.objects.filter(user_name=user_name)
	if user:
		status = 100
	else:
		status = 200
	return HttpResponse(status)

def register(request):
	user_name = request.GET.get('user_name')
	password = request.GET.get('password')
	try:
		user = User(user_name=user_name, password=password)
		user.save()
		status = 200
	except:
		status = 100
	return HttpResponse(json.dumps({'status':status}))

def change(request):
	return render(request, 'change.html')

def changepass(request):
	user_name = request.GET.get('user_name')
	pass_word = request.GET.get('password')
	user = User.objects.get(user_name=user_name)
	try:
		user.password = pass_word
		print(user.password, user.user_name)
		user.save()
		status = 200
	except:
		status = 100

	return HttpResponse(json.dumps({'status': status}))

