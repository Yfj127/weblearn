from MySite.models import Goods
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","MyWeb.settings")
django.setup()

with open('data.txt', 'r', encoding='utf8') as f:
	for line in f:
		lst = line.strip('\n').split(',')
		state = Goods.objects.create(goods_name=lst[0], goods_number=lst[1], goods_price=lst[2])
		print(state)