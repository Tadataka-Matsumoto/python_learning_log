"""learning_logsのURLパターンの定義(p206)"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #ホームページ(p206)
    path('', views.index, name='index'),#p206
    #すべてのトピックを表示するページ(p212)
    path('topics/', views.topics, name='topics'),#p212
    #個別トピックの詳細ページ(p216)
    path('topics/<int:topic_id>/', views.topic, name='topic'),#p216
    #新規トピックの追加ページ(p223)
    path('new_topic/', views.new_topic, name='new_topic'),#p223
    #新規記事の追加ページ(p227)
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #記事の編集ページ(p232)
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]




