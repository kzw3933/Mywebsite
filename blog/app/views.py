from django.shortcuts import render

def index(request):
    img_list = [
        "/static/my/img/site/能天使.png",
        "/static/my/img/site/德狗.jpg",
        "/static/my/img/site/拉狗.jpeg",
        "/static/my/img/site/白咕咕.jpg",
        "/static/my/img/site/anomalous.jpeg",
        "/static/my/img/site/阿米娅.jpeg",
        "/static/my/img/site/陈.jpeg",
        "/static/my/img/site/赫默.jpg",
        "/static/my/img/site/铃兰.jpg",
        "/static/my/img/site/嵯峨.jpg"
    ]
    return render(request, 'index.html', {"img_list": img_list})