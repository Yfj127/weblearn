from django.db import models

# Create your models here.

class Goods(models.Model):
	goods_name = models.CharField(max_length=64)    # 数据库字段  goods.goods_name
	goods_number = models.IntegerField()
	goods_price = models.FloatField()


