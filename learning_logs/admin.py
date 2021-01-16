from django.contrib import admin

# Register your models here.

from .models import Topic, Entry#管理者(superuser)設定でTopic追加(p197), Entry追加(p201)

admin.site.register(Topic)#p197
admin.site.register(Entry)#p201

