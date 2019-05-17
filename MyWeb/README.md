urls  全局路由
wsgj  python应用程序或框架的接口

MVC   model   View   Controller    模型  视图  控制器
MTV   模型  模板   视图
admin  是自动话后台管理工具  

全局urls  以及应用类urls  最好是分开  django2.0 以上url 好像变成了 path （查查）
全局
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('MySite.urls')),
]

局部  
urlpatterns = [
    url(r'^$', views.index),
]

实现调用百度翻译的接口  MySite/trans.py   url---> view---trans    
http://127.0.0.1:8000/trans/?words=富强民主文明和谐自由平等公正法治爱国敬业诚信友善&from_lang=zh&to_lang=en  

模板标签语言： 首先创建templates  在setting.py 文件里面配置好
    {{ 变量名 }}   由视图函数传递
    {% include '模板名.html' %}
    模板复用（模板继承）---通用模板  {% block 唯一名 %}默认{% endblock %}
    子模版  {% extends '通用模板名' %}
            {% block 唯一名 %}修改的内容{% endblock %}      唯一名在子模版中只能出现一次

获取对应需要的参数，找到url，找到函数，把参数传递给函数，返回给html
url(r'^news_list/(\d+)', views.news_list),
def news_list(request,choose):
	new_type = {'1': '经济', '2': '教育'}
	return render(request, 'news_list.html', context={'new_type': new_type[choose]})

--------
内置标签和过滤器（按要求对数据进行处理）  { 标签|过滤器(函数,传参用:|过滤器)}    
{{ letters|wordcount }}<br>
{{ letters|join:',' }}<br>

模板循环和条件判断  语法和py类似
{ for .. in .....}
    { forloop.first/counter} # 首项/编号1开始
    .....
{ endfor }

{ if... }
....
{ else }
...
{ endif }

------
数据库的相关内容 orm  关系数据库管理模型  类  相当于表  属性 相当于字段  创建类时得继承models，Model
迁移数据库  python manage.py makemigrations (记录变更)     python manage.py migrate  （大概操作 初始化的时候找到注册的应用，创建数据库）
如果在数据库里面有数据存在，临时增加字段会出现两种可能性  一是增加 默认值  二是直接退出。或者在创建的时候直接default

存数据  
python manage.py shell
1 类名.objects.create(字段='..',字段='..')
2 p = 类名(字段1='..',字段2='..')   p.save()
3 p = 类名()  p.字段1='..' ....     p.save()

查  类名.objects.all()/values()

------导入数据  data.txt  and data_con.py  但是这里导入文件时出错，最后在 shell环境下完成导入（没有解决）
配置相关文件 编写index.html  通过提交的地址找到url 对应的函数，按要求取数据