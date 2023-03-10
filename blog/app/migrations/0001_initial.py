# Generated by Django 4.1.4 on 2022-12-23 00:13

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nickname",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="??????"
                    ),
                ),
                (
                    "avatar_url",
                    models.URLField(blank=True, null=True, verbose_name="????????????"),
                ),
                (
                    "telephone",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="?????????"
                    ),
                ),
                ("integral", models.IntegerField(default=20, verbose_name="????????????")),
                (
                    "token",
                    models.CharField(
                        blank=True,
                        help_text="???????????????????????????id",
                        max_length=64,
                        null=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "ip",
                    models.GenericIPAddressField(
                        default="127.0.0.1", verbose_name="ip??????"
                    ),
                ),
                (
                    "addr",
                    models.TextField(blank=True, null=True, verbose_name="??????????????????"),
                ),
                (
                    "sign_type",
                    models.IntegerField(
                        choices=[
                            (0, "???????????????"),
                            (1, "QQ??????"),
                            (2, "gitee??????"),
                            (3, "???????????????"),
                            (4, "????????????"),
                        ],
                        default=0,
                        verbose_name="????????????",
                    ),
                ),
                (
                    "account_status",
                    models.IntegerField(
                        choices=[(0, "????????????"), (1, "????????????"), (2, "???????????????")],
                        default=0,
                        verbose_name="????????????",
                    ),
                ),
            ],
            options={"verbose_name_plural": "??????",},
        ),
        migrations.CreateModel(
            name="Advert",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(max_length=32, null=True, verbose_name="?????????"),
                ),
                ("href", models.URLField(verbose_name="????????????")),
                (
                    "img",
                    models.FileField(
                        help_text="??????",
                        null=True,
                        upload_to="advert/",
                        verbose_name="????????????",
                    ),
                ),
                (
                    "img_list",
                    models.TextField(
                        blank=True,
                        help_text="??????????????????????????????,???;??????????????????",
                        null=True,
                        verbose_name="?????????",
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="?????????"
                    ),
                ),
                (
                    "abstract",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="????????????"
                    ),
                ),
            ],
            options={"verbose_name_plural": "??????",},
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="??????"
                    ),
                ),
                (
                    "abstract",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="????????????"
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="????????????"),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="??????????????????"
                    ),
                ),
                (
                    "change_date",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="??????????????????"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "?????????"), (1, "?????????")], verbose_name="??????????????????"
                    ),
                ),
                ("recommend", models.BooleanField(default=True, verbose_name="???????????????")),
                ("look_count", models.IntegerField(default=0, verbose_name="???????????????")),
                ("comment_count", models.IntegerField(default=0, verbose_name="???????????????")),
                ("digg_count", models.IntegerField(default=0, verbose_name="???????????????")),
                (
                    "collects_count",
                    models.IntegerField(default=0, verbose_name="???????????????"),
                ),
                (
                    "category",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "??????"), (2, "??????"), (3, "????????????")],
                        null=True,
                        verbose_name="????????????",
                    ),
                ),
                (
                    "pwd",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="????????????"
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="??????"
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="??????"
                    ),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="????????????")),
                ("words", models.IntegerField(default=0, verbose_name="????????????")),
            ],
            options={"verbose_name_plural": "??????",},
        ),
        migrations.CreateModel(
            name="Avatar",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("url", models.FileField(upload_to="avatars/", verbose_name="??????????????????")),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Cover",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "url",
                    models.FileField(upload_to="article_img/", verbose_name="??????????????????"),
                ),
                (
                    "dominant_hue",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="???????????????"
                    ),
                ),
                (
                    "is_dark",
                    models.BooleanField(blank=True, null=True, verbose_name="??????????????????"),
                ),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, verbose_name="??????")),
                ("content", models.TextField(verbose_name="????????????")),
                ("status", models.BooleanField(default=False, verbose_name="????????????")),
                (
                    "processing_content",
                    models.TextField(blank=True, null=True, verbose_name="???????????????"),
                ),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="History",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32, verbose_name="?????????")),
                ("content", models.TextField(verbose_name="????????????")),
                ("create_date", models.DateTimeField(null=True, verbose_name="????????????")),
                (
                    "drawing",
                    models.TextField(blank=True, null=True, verbose_name="?????????"),
                ),
            ],
            options={"verbose_name_plural": "?????????",},
        ),
        migrations.CreateModel(
            name="MenuImg",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("url", models.FileField(upload_to="site_bg/", verbose_name="????????????")),
                (
                    "dominant_hue",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="???????????????"
                    ),
                ),
                (
                    "is_dark",
                    models.BooleanField(blank=True, null=True, verbose_name="??????????????????"),
                ),
            ],
            options={"verbose_name_plural": "???????????????",},
        ),
        migrations.CreateModel(
            name="Mood",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=16, verbose_name="?????????")),
                (
                    "ip",
                    models.GenericIPAddressField(
                        default="127.0.0.1", verbose_name="ip??????"
                    ),
                ),
                ("addr", models.TextField(null=True, verbose_name="??????????????????")),
                (
                    "create_date",
                    models.DateTimeField(auto_now=True, verbose_name="????????????"),
                ),
                ("content", models.TextField(verbose_name="????????????")),
                (
                    "drawing",
                    models.TextField(blank=True, null=True, verbose_name="?????????"),
                ),
                ("comment_count", models.IntegerField(default=0, verbose_name="?????????")),
                ("digg_count", models.IntegerField(default=0, verbose_name="?????????")),
                (
                    "avatar",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.avatar",
                        verbose_name="?????????????????????",
                    ),
                ),
            ],
            options={"verbose_name_plural": "??????",},
        ),
        migrations.CreateModel(
            name="NavTag",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=16, verbose_name="?????????")),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=16, verbose_name="?????????")),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="??????"
                    ),
                ),
                (
                    "article",
                    models.ManyToManyField(to="app.article", verbose_name="??????"),
                ),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Nav",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32, verbose_name="????????????")),
                (
                    "abstract",
                    models.CharField(max_length=128, null=True, verbose_name="????????????"),
                ),
                ("href", models.URLField(verbose_name="????????????")),
                (
                    "icon_href",
                    models.URLField(
                        blank=True, help_text="????????????", null=True, verbose_name="????????????"
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(auto_now=True, verbose_name="????????????"),
                ),
                (
                    "collects_count",
                    models.IntegerField(default=0, verbose_name="???????????????"),
                ),
                ("digg_count", models.IntegerField(default=0, verbose_name="?????????")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "?????????"), (1, "?????????"), (2, "?????????")],
                        default=0,
                        verbose_name="????????????",
                    ),
                ),
                ("tag", models.ManyToManyField(to="app.navtag", verbose_name="????????????")),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="MoodComment",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "commentor",
                    models.CharField(max_length=16, null=True, verbose_name="?????????"),
                ),
                ("content", models.TextField(verbose_name="????????????")),
                ("digg_count", models.IntegerField(default=0, verbose_name="?????????")),
                (
                    "ip",
                    models.GenericIPAddressField(
                        default="127.0.0.1", verbose_name="ip??????"
                    ),
                ),
                ("addr", models.TextField(null=True, verbose_name="??????????????????")),
                (
                    "create_date",
                    models.DateTimeField(auto_now=True, verbose_name="????????????"),
                ),
                (
                    "avatar",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.avatar",
                        verbose_name="?????????????????????",
                    ),
                ),
                (
                    "mood",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.mood",
                        verbose_name="???????????????",
                    ),
                ),
            ],
            options={"verbose_name_plural": "????????????",},
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "menu_title",
                    models.CharField(max_length=16, null=True, verbose_name="?????????"),
                ),
                (
                    "menu_title_en",
                    models.CharField(max_length=32, null=True, verbose_name="???????????????"),
                ),
                (
                    "title",
                    models.CharField(max_length=32, null=True, verbose_name="slogan"),
                ),
                ("abstract", models.TextField(null=True, verbose_name="slogan??????")),
                (
                    "abstract_time",
                    models.IntegerField(default=8, verbose_name="slogan????????????"),
                ),
                (
                    "rotation",
                    models.BooleanField(default=True, verbose_name="????????????slogan??????"),
                ),
                (
                    "menu_rotation",
                    models.BooleanField(default=False, verbose_name="????????????banner???"),
                ),
                ("menu_time", models.IntegerField(default=8, verbose_name="?????????????????????")),
                (
                    "menu_url",
                    models.ManyToManyField(
                        help_text="????????????,??????????????????", to="app.menuimg", verbose_name="????????????"
                    ),
                ),
            ],
            options={"verbose_name_plural": "??????????????????",},
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("digg_count", models.IntegerField(default=0, verbose_name="?????????")),
                ("content", models.TextField(verbose_name="????????????")),
                (
                    "child_comment_count",
                    models.IntegerField(default=0, verbose_name="????????????"),
                ),
                ("drawing", models.TextField(blank=True, null=True, verbose_name="??????")),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="????????????"),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.article",
                        verbose_name="????????????",
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.comment",
                        verbose_name="??????????????????",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="?????????",
                    ),
                ),
            ],
            options={"verbose_name_plural": "??????",},
        ),
        migrations.AddField(
            model_name="article",
            name="cover",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.cover",
                verbose_name="????????????",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="tag",
            field=models.ManyToManyField(blank=True, to="app.tag", verbose_name="????????????"),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="avatar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.avatar",
                verbose_name="????????????",
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="collects",
            field=models.ManyToManyField(
                blank=True, to="app.article", verbose_name="????????????"
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="nav",
            field=models.ManyToManyField(
                blank=True, to="app.nav", verbose_name="???????????????"
            ),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
