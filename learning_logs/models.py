from django.db import models
from django.contrib.auth.models import User#ユーザーに対する外部キーの関連を追加のため(p248)

# Create your models here.
class Topic(models.Model):#(p193)
    """ユーザーが学んでいるトピックを表す(p193)"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)#Userを外部キーとして関連付けた(p248)

    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.text

class Entry(models.Model):
    """トピックに関して学んだ具体的なこと(p199)"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#topicを外部キーとして関連付けた(p199)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """モデルの文字列表現を返す(p199)"""
        return f"{self.text[:25]}..."

