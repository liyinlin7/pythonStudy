"""定义learning_logs的URL模式。"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    # 显示所有的主题。
    path('topics/', views.topics, name='topics'),
]
'''
    实际的URL模式是对函数path() 的调用，这个函数接受三个实参。
    第一个是一个字符串，帮助Django正确地路由（route）请求。收到请求的URL后，Django力图将请求路由给一个视图。
    为此，它搜索所有的URL模式，找到与当前请求匹配的那个。Django忽略项目的基础URL（http://localhost:8000/），因此空字符串（''）与基础URL匹配。
    其他URL都与这个模式不匹配。如果请求的URL与任何既有的URL模式都不匹配，Django将返回一个错误页面。
    第二个实参指定了要调用view.py中的哪个函数。请求的URL与前述正则表达式匹配时，Django将调用view.py中的函数index() （这个视图函数将在下一节编写）。
    第三个实参将这个URL模式的名称指定为index ，让我们能够在代码的其他地方引用它。每当需要ᨀ供到这个主页的链接时，都将使用这个名称，而不编写URL。
 '''