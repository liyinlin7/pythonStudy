from django.contrib import admin

# Register your models here. 在这里注册你的模型。

from .models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)
