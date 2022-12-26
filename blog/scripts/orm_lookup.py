import os


if __name__ == '__main__':
    # 加载django项目的配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

    # 导入django并启动django项目
    import django
    django.setup()

    from app.models import *

    # 对象查询
    # 一对一
    # 正向
    res = Student.objects.get(nid=12).student_info.email
    print(res)

    # 反向
    student_info = StudentInfo.objects.get(email="3099097649@qq.com")
    print(student_info.student.name)

    # 一对多
    # 正向
    res = Student.objects.get(nid=12).student_class.title
    print(res)

    # 反向
    class_obj = Class.objects.get(title="3年A班")
    student_list = class_obj.student_set.all()
    print(student_list)

    # 多对多
    # 正向
    res = Class.objects.get(nid=1).teacher.all()
    print(res)

    # 反向
    teacher_obj = Teacher.objects.get(name="张老师")
    class_list = teacher_obj.class_set.all()
    print(class_list)

    # 应用
    class_obj = Class.objects.get(title="3年A班")
    student_list = class_obj.student_set.all().values('name')
    print(student_list)

    class_obj = Class.objects.get(title="3年A班")
    student_list = class_obj.student_set.all()
    print(student_list.filter(age__gt=20, gender='女').values('name'))

    # 基于双下划线的查询
    class_obj = Class.objects.get(title="3年A班")
    student_list = class_obj.student_set.all()
    res = student_list.filter(age__gt=21).values('name')
    print(res)

    # 反向
    Class.objects.filter(title="3年A班", student__age__gt=21).values('student__name')

    # 应用
    print(Student.objects.filter(name='大明').values('student_info__email'))
    print(StudentInfo.objects.filter(student__name='大明').values('email'))
    print(Class.objects.all().values('title'))

    print(Class.objects.filter(title='3年A班').values('student__name'))
    print(Student.objects.filter(student_class__title='3年A班').values('name'))


    from django.db.models import Count, Max, Min, Avg, F, Q
    # 聚合查询
    print(Student.objects.all().count())

    # 统计学生的平均年龄
    print(Student.objects.aggregate(Avg('age'))) ## 作用于QuerySet对象,返回字典
    print(Student.objects.aggregate(age_avg=Avg('age'))) ## 改变默认名称
    print(Student.objects.filter(age__gt=21).aggregate(Avg('age'), Max('age'), Min('age'), Count('age')))

    print(Class.objects.filter(title="3年A班").values('teacher__age').aggregate('teacher__age'))

    # 分组查询
    # 统计男生、女生的人数
    print(Student.objects.values('gender').annotate(Count('nid')))

    # 统计每个班级的人数
    print(Student.objects.values('student_class__title').annotate(Count('student_class__title')))

    # # F查询
    # # 查询评论量比点赞量多的课程
    # print(Course.objects.filter(comment_count__gt=F('digg_count')))
    # # 自增操作
    # course_obj = Course.objects.get(nid=1)
    # course_obj.look_count += 1
    # course_obj.save()
    #
    # Course.objects.filter(nid=1).update(look_count=F('look_count')+1)

    # Q查询
    print(Student.objects.filter(age__gt=18, gender='女'))
    print(Student.objects.filter(Q(age__gt=26)|Q(gender='女')))











