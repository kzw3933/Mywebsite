from django.urls import path, re_path, include
from app import views

urlpatterns = [
    path("index/", views.index, name='index'),
    path("login/", views.login, name='login'),
    path("post/", views.post, name='post'),
    path("home/<twoint:year>", views.home),    ## 匹配所有数字
    # path("home/<int:year>", views.home),    ## 匹配所有字母、数字、下划线
    # path("home/<int:year>", views.home),    ## 匹配非路径分隔符
    # path("home/<int:year>", views.home),    ## 匹配所有
    path("test/", views.test, name="test"),
    path("register/", views.register, name="register"),
    path("bregister/", views.bregister, name="bregister"),
    path("lookup/", views.lookup, name="lookup"),
    path("remove/", views.remove, name="remove"),
    path("update/", views.update, name="update"),
    path("asso_add/", views.asso_add, name="asso_add"),
    path("asso_lookup/", views.asso_lookup, name="asso_lookup"),
    path("as so_delete/", views.asso_delete, name="asso_delete"),
    path("form_add/", views.form_add, name="form_add"),
    path("pages/", views.pages, name="pages"),
    path("django_pages/", views.django_pages, name="django_pages"),
    path("student_signin/", views.student_signin, name="student_signin"),
    path("SSO/", views.SSO, name="SSO"),
    path("logout/", views.logout, name="logout"),
]