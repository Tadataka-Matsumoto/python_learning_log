from django.shortcuts import render, redirect#redirect追加(p224)
from django.contrib.auth.decorators import login_required#デコレーター追加(p246)
from django.http import Http404#各トピックの侵入を防止するため追加(p252)

# Create your views here.

from .models import Topic, Entry#pTopic追加(p213),Entry追加(p232)
from .forms import TopicForm, EntryForm#p224でTopicForm、p229でEntryForm追加

def index(request):
    """学習ノートのホームページ(p207)"""
    return render(request, 'learning_logs/index.html')

@login_required#アクセス権追加(p246)
def topics(request):
    """すべてのトピックを表示する(p212)"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')#アクセスできる人を限定のためコード変更(p251)
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required#アクセス権追加(p247)
def topic(request, topic_id):
    """1つのトピックとそれについてのすべての記事を表示(p216)"""
    topic = Topic.objects.get(id=topic_id)

    #トピックが現在のユーザーが所持するものであることを確認する(p252)
    if topic.owner != request.user:
        raise Http404   

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required#アクセス権追加(p247)
def new_topic(request):
    """新規トピックを追加する(p224)"""
    if request.method != 'POST':
        #データは送信されていないので空のフォームを生成する
        form = TopicForm()
    else:
        #POSTでデータが送信されたのでこれを処理する
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)#p229のnew_entryと同じ要領(p253)
            new_topic.owner = request.user#p253
            new_topic.save()#p253
            # form.save()#p224での内容をコメントアウト(p253)
            return redirect('learning_logs:topics')

    #空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required#アクセス権追加(p247)
def new_entry(request, topic_id):
    """特定のトピックに新規記事を追加する(p229)"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #データは送信されないので空のフォームを生成する
        form = EntryForm()
    else:
        #POSTでデータが送信されたのでこれを処理する
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)#新しい記事オブジェクトを生成してnew_entryに代入するがdbに保存しない(p229)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    #空または無効のフォームを表示する
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required#アクセス権追加(p247)
def edit_entry(request, entry_id):
    """既存の記事を編集する(p232)"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    #トピックが現在のユーザーが所持するものであることを確認する(p252)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初回リクエスト時は現在の記事の内容がフォームに埋め込まれている
        form = EntryForm(instance=entry)
    else:
        #POSTでデータが送信されたのでこれを処理する
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)



