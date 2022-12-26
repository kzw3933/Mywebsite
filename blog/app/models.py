from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from django.db.models.signals import pre_delete   ## 删除文件
from django.dispatch.dispatcher import receiver   ## 删除文件

# Create your models here.

"""
主体表结构
UserInfo        用户信息表
Avatar          用户头像表
Article         文章表
Project         项目分类表
Comment         评论表
Cover           文章封面表
Tag             标签表
History         回忆录表
Mood            心情表
MoodComment     心情评论表
Nav             网站导航表
NavTag          网站标签表
Menu            站点背景菜单表
MenuImg         站点背景表
Advert          广告表
Feedback        反馈信息表
"""

# 用户信息
class UserInfo(AbstractUser):

    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=16, verbose_name='昵称', null=True, blank=True)
    avatar_url = models.URLField(verbose_name='用户头像', null=True, blank=True)
    telephone = models.CharField(max_length=12, verbose_name='手机号', null=True, blank=True)
    integral = models.IntegerField(verbose_name='用户积分', default=20)
    token = models.CharField(max_length=64, verbose_name='id', help_text='其他平台的唯一登录id', null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name='ip地址', default='127.0.0.1')
    addr = models.TextField(verbose_name='用户地址信息', null=True, blank=True)
    sign_choices = (
        (0, '用户名注册'),
        (1, 'QQ注册'),
        (2, 'gitee注册'),
        (3, '手机号注册'),
        (4, '邮箱注册')
    )
    sign_type = models.IntegerField(verbose_name='注册方式', choices=sign_choices, default=0)
    account_choices = (
        (0, '账号正常'),
        (1, '账号异常'),
        (2, '账号被封禁')
    )

    account_status = models.IntegerField(verbose_name='账号状态', choices=account_choices, default=0)
    avatar = models.ForeignKey(
        to='Avatar',
        to_field='nid',
        on_delete=models.SET_NULL,
        verbose_name='用户头像',
        null=True,
        blank=True
    )
    collects = models.ManyToManyField(
        to='Article',
        verbose_name='收藏文章',
        blank=True
    )
    nav = models.ManyToManyField(
        to='Nav',
        verbose_name='收藏的网站',
        blank=True
    )

    class Meta:
        verbose_name_plural = '用户'

# 用户头像
class Avatar(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    url = models.FileField(verbose_name='用户头像地址', upload_to='avatars/')

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name_plural = '用户头像'


# 删除头像
@receiver(pre_delete, sender=Avatar)
def avatar_delete(instance, **kwargs):
    instance.url.delete(False)


# 文章
class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32, null=True, blank=True)
    abstract = models.CharField(verbose_name='文章简介', max_length=128, null=True, blank=True)
    content = models.TextField(verbose_name='文章内容', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='文章发布日期', auto_now_add=True, null=True)
    change_date = models.DateTimeField(verbose_name='文章修改日期', auto_now=True, null=True)
    status_choices = (
        (0, '未发布'),
        (1, '已发布')
    )
    status = models.IntegerField(verbose_name='文章保存状态', choices=status_choices)
    recommend = models.BooleanField(verbose_name='是否上推荐', default=True)
    cover = models.ForeignKey(
        to='Cover',
        to_field = 'nid',
        on_delete = models.SET_NULL,
        verbose_name='文章封面',
        null=True,
        blank=True
    )
    look_count = models.IntegerField(verbose_name='文章阅读量', default=0)
    comment_count = models.IntegerField(verbose_name='文章评论量', default=0)
    digg_count = models.IntegerField(verbose_name='文章点赞量', default=0)
    collects_count = models.IntegerField(verbose_name='文章收藏数', default=0)
    category_choices = (
        (1, '前端'),
        (2, '后端'),
        (3, '项目相关')
    )
    category = models.IntegerField(verbose_name='文章类型', choices=category_choices, null=True, blank=True)
    tag = models.ManyToManyField(
        to='Tag',
        verbose_name='文章标签',
        blank=True
    )
    pwd = models.CharField(verbose_name='文章密码', max_length=32, null=True, blank=True)
    author = models.CharField(verbose_name='作者', max_length=16, null=True, blank=True)
    source = models.CharField(verbose_name='来源', max_length=32, null=True, blank=True)

    link = models.URLField(verbose_name='文章链接', null=True, blank=True)
    words = models.IntegerField(verbose_name='文章字数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章'


# 项目分类
class Project(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32, null=True, blank=True)
    article = models.ManyToManyField(
        to='Article',
        verbose_name='文章'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '项目相关'

# 评论
class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    digg_count = models.IntegerField(verbose_name='点赞数', default=0)
    article = models.ForeignKey(
        to='Article',
        to_field='nid',
        verbose_name='评论文章',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to='UserInfo',
        to_field='nid',
        verbose_name='评论者',
        on_delete=models.CASCADE,
        null=True
    )

    content = models.TextField(verbose_name='评论内容')
    child_comment_count = models.IntegerField(verbose_name='子评论数', default=0)
    drawing = models.TextField(verbose_name='配图', null=True, blank=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self',
        verbose_name='是否是父评论',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = '评论'

# 文章封面
class Cover(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    url = models.FileField(verbose_name='文章封面地址', upload_to='article_img/')
    dominant_hue = models.CharField(verbose_name='封面主色调', max_length=16, null=True, blank=True)
    is_dark = models.BooleanField(verbose_name='是否是深色系', null=True, blank=True)

    def __str__(self):

        return str(self.url)

    class Meta:
        verbose_name_plural = '文章封面'

@receiver(pre_delete, sender=Cover)
def cover_delete(instance, **kwargs):
    instance.url.delete(False)

# 标签
class Tag(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名', max_length=16)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章标签'

# 回忆录
class History(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='事件名', max_length=32)
    content = models.TextField(verbose_name='事件内容')
    create_date = models.DateTimeField(verbose_name='创建时间', null=True)
    drawing = models.TextField(verbose_name='配图组', null=True, blank=True)

    class Meta:
        verbose_name_plural = '回忆录'

# 心情
class Mood(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='发布人', max_length=16)
    ip = models.GenericIPAddressField(verbose_name='ip地址', default='127.0.0.1')
    addr = models.TextField(verbose_name='用户地址信息', null=True)
    create_date = models.DateTimeField(verbose_name='发布时间', auto_now=True)
    content = models.TextField(verbose_name='心情内容')
    drawing = models.TextField(verbose_name='配图组', null=True, blank=True)
    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    digg_count = models.IntegerField(verbose_name='点赞数', default=0)
    avatar = models.ForeignKey(
        to='Avatar',
        to_field='nid',
        verbose_name='心情的发布头像',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '心情'

# 心情评论
class MoodComment(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    avatar = models.ForeignKey(
        to='Avatar',
        to_field='nid',
        verbose_name='心情的发布头像',
        null=True,
        on_delete=models.SET_NULL
    )
    commentor = models.CharField(verbose_name='评论人', max_length=16, null=True)
    content = models.TextField(verbose_name='评论内容')
    digg_count = models.IntegerField(verbose_name='点赞数', default=0)
    ip = models.GenericIPAddressField(verbose_name='ip地址', default='127.0.0.1')
    addr = models.TextField(verbose_name='用户地址信息', null=True)
    mood = models.ForeignKey(
        to='Mood',
        to_field='nid',
        verbose_name='评论的心情',
        null=True,
        on_delete=models.SET_NULL
    )
    create_date = models.DateTimeField(verbose_name='评论时间', auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = '心情评论'


# 网站导航
class Nav(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='网站标题', max_length=32)
    abstract = models.CharField(verbose_name='网站简介', max_length=128, null=True)
    href = models.URLField(verbose_name='网站链接')
    icon_href = models.URLField(
        verbose_name='图标链接',
        help_text='在线链接',
        null=True,
        blank=True
    )
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    collects_count = models.IntegerField(verbose_name='文章收藏数', default=0)
    digg_count = models.IntegerField(verbose_name='点赞数', default=0)

    status_choice = (
        (0, '待审核'),
        (1, '已通过'),
        (2, '被驳回')
    )

    status = models.IntegerField(verbose_name='导航状态', choices=status_choice, default=0)

    def color_state(self):
        if self.status == 0:
            assign_state_name = '待审核'
            color_code = '#ec921e'
        elif self.status == 1:
            assign_state_name = '已通过'
            color_code = 'green'
        else:
            assign_state_name = '被驳回'
            color_code = 'red'

        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            assign_state_name
        )

    color_state.short_description = '导航状态'
    tag = models.ManyToManyField(
        to='NavTag',
        verbose_name='网站标签'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '网站导航'

# 网站标签
class NavTag(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名', max_length=16)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '网站标签'


# 站点背景菜单
class Menu(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    menu_title = models.CharField(verbose_name='菜单名', max_length=16, null=True)
    menu_title_en = models.CharField(verbose_name='菜单英文名', max_length=32, null=True)
    title = models.CharField(verbose_name='slogan', max_length=32, null=True)
    abstract = models.TextField(verbose_name='slogan介绍', null=True)
    abstract_time = models.IntegerField(verbose_name='slogan切换时间', default=8)
    rotation = models.BooleanField(verbose_name='是否轮播slogan介绍', default=True)
    menu_url = models.ManyToManyField(
        to="MenuImg",
        verbose_name='菜单图片',
        help_text='可以多选,多选就会轮播'
    )
    menu_rotation = models.BooleanField(verbose_name='是否轮播banner图', default=False)
    menu_time = models.IntegerField(verbose_name='背景图切换时间', default=8)

    class Meta:
        verbose_name_plural = '站点背景菜单'


# 站点背景图
class MenuImg(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    url = models.FileField(verbose_name='图片地址', upload_to='site_bg/')
    dominant_hue = models.CharField(verbose_name='封面主色调', max_length=16, null=True, blank=True)
    is_dark = models.BooleanField(verbose_name='是否是深色系', null=True, blank=True)

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name_plural = '站点背景图'

# 广告
class Advert(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='产品名', max_length=32, null=True)
    href = models.URLField(verbose_name='跳转链接')
    img = models.FileField(verbose_name='图片地址', null=True, help_text='单图', upload_to='advert/')
    img_list = models.TextField(verbose_name='图片组', null=True, blank=True, help_text='上传图片请用线上地址,用;隔开多张图片')
    author = models.CharField(verbose_name='广告主', max_length=32, null=True, blank=True)
    abstract = models.CharField(verbose_name='产品简介', max_length=128, null=True, blank=True)

    class Meta:
        verbose_name_plural = '广告'

# 反馈信息
class Feedback(models.Model):
    objects = models.Manager()  ## 避免后续IDE找不到objects属性
    nid = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='邮箱')
    content = models.TextField(verbose_name='反馈信息')
    status = models.BooleanField(verbose_name='是否处理', default=False)
    processing_content = models.TextField(verbose_name='回复的内容', null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = '用户反馈'













