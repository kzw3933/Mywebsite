from django.db import models

# Create your models here.

class Teacher(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="教师姓名", max_length=8)
    age = models.IntegerField(verbose_name="教师年龄")



class Class(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="班级名称", max_length=12)

    teacher = models.ManyToManyField(
        to="teacher"
    )


class Student(models.Model):
    objects = models.Manager() ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8, verbose_name="学生姓名")
    age = models.IntegerField(verbose_name="学生年龄")
    gender = models.CharField(max_length=1, verbose_name="学生性别", default="男")
    addr = models.CharField(max_length=32, verbose_name="学生地址", null=True, blank=True)

    student_info = models.OneToOneField(
        to="StudentInfo",
        to_field="nid",
        on_delete=models.CASCADE,
        null=True,
    )

    student_class = models.ForeignKey(
        to="Class",
        to_field="nid",
        on_delete=models.SET_NULL,
        null=True,
    )

    # class Meta:
    #     unique_together = [('name', 'age', 'gender'),]
    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    like = models.CharField(max_length=8, verbose_name="学生爱好")
    blood = models.CharField(max_length=8, verbose_name="学生血型")
    email = models.CharField(max_length=32, verbose_name="学生邮箱")
    create_time = models.DateField(verbose_name="学生报名时间", auto_now=True)


class UserInfo(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    name = models.CharField(verbose_name="用户名", max_length=16)
    pwd = models.CharField(verbose_name="密码", max_length=32)





