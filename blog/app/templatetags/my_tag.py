from django import template

register = template.Library()


# 自定义过滤器和标签
@register.filter
def multi(a, b):
    return a*b
@register.simple_tag
def add_t(a, b, c):
    return a + b + c

# inclusion_tag 自定义返回页面
@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    img_list = [
        "/static/my/img/site/能天使.png",
        "/static/my/img/site/德狗.jpg",
        "/static/my/img/site/阿米娅.jpeg",
        "/static/my/img/site/赫默.jpg",
        "/static/my/img/site/嵯峨.jpg"
    ]

    return {"img_list": img_list}



