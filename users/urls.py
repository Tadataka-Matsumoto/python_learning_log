"""users用URLパターンの定義(p237)"""

from django.urls import path, include

from . import views#追加です(p242)

app_name='users'

urlpatterns = [
    #デフォルトの認証URLを取り込む(p237)
    path('', include('django.contrib.auth.urls')),#p237
    #ユーザー登録ページ(p242)
    path('register/', views.register, name='register'),
]

