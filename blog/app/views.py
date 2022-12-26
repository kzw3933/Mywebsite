import random

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
import datetime
from app.models import *
from faker import Faker
import math
from django import forms
from django.core.exceptions import ValidationError

# Create your views here.
def index_test(request):
    name = 'jack'
    alist = ['a', 'b', 'c', 'd', 'e']
    adict = {'name': 'jack', 'age': 200, 'job': 'ghost'}
    def func():
        return "Hello world!"
    class Ghost:
        def play(self):
            return "play"
        def __str__(self):
            return "ghost"

    aobj = Ghost()
    aobj.name = "ghost"

    alongstr = "123456666622r3ferweagfascszdvxdcfvgsjdbjdzbsbuewyufbhjc"

    time_now = datetime.datetime.now()

    login = None
    ahref = '<a src="http://www.baidu.com">百度</a>'

    # return render(request, 'index_test.html', {'name': name, 'alist': alist, 'adict':adict, 'func': func, 'aobj':aobj})
    return render(request, 'index_test.html', locals())


def post(request):
    post_path = reverse('app:index')
    return redirect(post_path)

def home(request, year):
    return HttpResponse("home")

def test(request):
    return render(request, 'test.html')

def register(request):
    # 创建对象
    # student = Student(name="kzw",age=21,addr="HeNan")
    # student.save()
    # print(student)

    student = Student.objects.create(name="kzw", age=21, gender="男")
    print(student)

    return HttpResponse("添加成功")

def bregister(request):
    # 批量创建对象
    faker = Faker('zh_CN')
    # for i in range(20):
    #     student = Student(name=faker.name(), age=random.randint(18, 23), gender=random.choice('男女'))
    #     student.save()
    #     print(student)

    student_list = []
    for i in range(1000):
        student_list.append(Student(name=faker.name(), age=random.randint(18, 23), gender=random.choice('男女'), addr=faker.address()))
    Student.objects.bulk_create(student_list)

    return HttpResponse("批量添加成功")

def lookup(request):

    # 查询所有
    student_all = Student.objects.all()

    # 条件查询
    student_list = Student.objects.filter(age=21)
    first_student = student_list.first()

    a_student = Student.objects.get(age=22)

    # 多条件查询
    student_list = Student.objects.filter(age=22, gender="男")

    # 对象的用法
    student_object = Student.objects.get(nid=5)
    print(student_object.name, student_object.age, student_object.addr)

    # query_set对象的用法
    exists = Student.objects.filter(age=22).exists()
    print(exists)

    student_all = Student.objects.all().order_by('age')

    # 统计
    student_count = Student.objects.filter(age=22).count()
    student_count = Student.objects.exclude(age=22).count()

    student_dict = Student.objects.filter(age=22).values('name', 'age')
    student_tuple = Student.objects.filter(age=22).values_list('name', 'age')
    print(student_dict)
    print(student_tuple)

    # 模糊查询
    student_list = Student.objects.filter(age__gt=21)
    print(Student.objects.filter(age__range=[19, 21]))
    print(Student.objects.filter(age__in=[18,19,21]))

    print(Student.objects.filter(name__contains='伟'))
    print(Student.objects.filter(name__startswith='k'))
    print(Student.objects.filter(name__isnull=True))

    return HttpResponse("查询成功")

def remove(request):

    # delete_info = Student.objects.filter(age__range=[12,21]).delete()
    # print(delete_info)
    Student.objects.all().delete()

    return HttpResponse("删除成功")

def update(request):
    update_info = Student.objects.filter(nid_in=[1,8]).update(gender='男')
    print(update_info)
    return HttpResponse("更新成功")


def asso_add(request):

    # 一对一添加
    student_info = StudentInfo.objects.create(like="羽毛球", blood="AB", email="1237932921@qq.com")
    # 关联
    Student.objects.create(student_info_id = student_info.nid, name="大王", age=21, addr="HeNan")

    # 一对多添加
    student_class = Class.objects.create(title="3年A班")
    Student.objects.create(student_class=student_class, name="王五", age=13, addr="HeNan")

    # 多对多添加
    class_obj = Class.objects.get(title="3年A班")
    # class_obj.teacher.add(1,2,3)
    # teacher1 = Teacher.objects.get(nid=1)
    # teacher2 = Teacher.objects.get(nid=2)
    # teacher3 = Teacher.objects.get(nid=3)
    # class_obj.teacher.add(teacher1, teacher2, teacher3)
    teacher_list = Teacher.objects.filter(nid__range=[1,3])
    class_obj.teacher.add(*teacher_list)

    teacher_obj = Teacher.objects.get(name="张老师")
    teacher_obj.class_set.add(1,2,3)

    return HttpResponse("添加成功")



def asso_lookup(request):

    # 一对一查询
    student_obj = Student.objects.get(nid=9)
    print(student_obj.student_info.email)

    # 正向查询
    student_dict = Student.objects.filter(nid=9).values('name', 'student_info__email')
    print(student_dict)

    # 一对多查询
    student_obj = Student.objects.get(nid=10)
    print(student_obj.name, student_obj.student_class.title)

    # 多对多查询

    # 正向查询
    class_obj = Class.objects.get(title="3年A班")
    teacher_dict = class_obj.teacher.all().values('name', 'age')
    print(teacher_dict)

    # 反向查询
    teacher_obj = Teacher.objects.get(name="张老师")
    class_dict = teacher_obj.class_set.all().values('title')
    print(class_dict)

    return HttpResponse("查询成功")

def asso_delete(request):
    # 级联删除
    StudentInfo.objects.filter(blood="AB").delete()

    return HttpResponse("删除成功")

def form_add(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        age = request.POST.get('age')
        Teacher.objects.create(name=name, age=age)
    return render(request, 'form_add.html')


def pages(request):
    p = int(request.GET.get('page'))

    page_count = 100
    counts = Student.objects.all().count()


    alist = [i for i in range(1, math.ceil(counts/page_count)+1)]

    student_list = Student.objects.all()[p*100-100:p*100]

    return render(request, 'page.html', locals())


def django_pages(request):

    from django.core.paginator import Paginator

    p = int(request.GET.get('page'))
    student_list = Student.objects.all()

    paginator = Paginator(student_list, 100)
    counts = paginator.num_pages

    if p == 1 or p==2:
        page_list = [1, 2, 3, '...', counts]
    elif p == 3:
        page_list = [1, 2, 3, 4, '...', counts]
    elif p in range(4, counts-2):
        page_list = [1, '...', p-1, p, p+1, '...', counts]
    elif p == counts-2:
        page_list = [1, '...', p-1, p+1, p+1, p+2]
    elif p == counts-1:
        page_list = [1, '...', p - 1, p, p + 1]
    elif p == counts:
        page_list = [1, '...', p - 1, p]
    else:
        page_list = [1, 2, 3, '...', counts]


    # page_list = paginator.page_range
    # print(page_list)

    student_list = paginator.page(p)

    return render(request, 'page.html', locals())


class AddStudentForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=8, error_messages={'required': '姓名不能为空', 'invalid': '请输入正确的名字'})
    age = forms.IntegerField(max_value=120, min_value=18, error_messages={'required': '年龄不能为空', 'invalid': '请输入正确的年龄'})
    gender = forms.CharField()
    addr = forms.CharField(max_length=32, error_messages={'required': '地址不能为空', 'invalid': '请输入正确的地址'})

    # 自定义校验
    def clean_addr(self):
        addr:str = self.changed_data
        if addr.startswith('北京市'):
            return self.cleaned_data['addr']

        raise ValidationError('只招收北京市的学生')


def student_signin(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data
            Student.objects.create(**data)
            return HttpResponse("注册成功")
        print(form.errors)
    return render(request, 'student_signin.html', locals())


class SSOUserForm(forms.Form):
    name = forms.CharField()
    pwd = forms.CharField()

def SSO(request):
    if request.method == "POST":
        data = request.POST
        form = SSOUserForm(data)
        if form.is_valid():
            userinfo_obj = UserInfo.objects.get(name=data.get('name'), pwd=data.get('pwd'))
            rep = redirect(reverse('app:index'))
            rep.set_cookie('is_login', True, max_age=10000)
            return rep
    return render(request, "SSO.html", locals())

def logout(request):
    # rep = redirect(reverse('app:login'))
    #
    # rep.delete_cookie('is_login')
    #
    # return rep

    return redirect(reverse('app:login'))



def login(request):
    # GET请求获取表单参数
    # username = request.GET.get('username')
    # password = request.GET.get('pwd')

    # POST请求获取表单参数
    # username = request.POST.get('username')
    # password = request.POST.get('pwd')
    #
    # if username == 'jack' and password == '123456':
    #     return redirect('../index')
    # return render(request, 'login.html')

    if request.method == "POST":
        form = SSOUserForm(request.POST)
        if form.is_valid():
            request.session['is_login'] = True
            request.session['username'] = form.cleaned_data.get('name')
            request.session.set_expiry(1000)
            return redirect(reverse('app:index'))

    return render(request, 'login.html', locals())


def index(request):
    # is_login = request.COOKIES.get('is_login')
    # if is_login:
    #     return render(request, 'index.html', locals())
    # else:
    #     return HttpResponse('404')
    is_login = request.session.get('is_login')
    username = request.session.get('username')


    return render(request, 'index.html', locals())












