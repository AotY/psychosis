from django.shortcuts import render
from django.http import HttpResponse
from common.mymako import render_mako_context

# Create your views here.

def index(request):
    return render_mako_context(request, 'index.html', {})


# 孤独症；儿童孤独症；孤独性
def autism(request):
    return render_mako_context(request, 'autism.html', {})


# 精神分裂症
def schizophrenia(request):
    return render_mako_context(request, 'schizophrenia.html', {})

# 忧郁症
def depression(request):
    return render_mako_context(request, 'depression.html', {})

# 关注
def concern(request):
    return render_mako_context(request, 'concern.html', {})

# 护理
def care(request):
    return render_mako_context(request, 'care.html', {})
