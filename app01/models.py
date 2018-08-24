from django.db import models


class BxSlide(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    status = models.IntegerField(choices=status_choice, default=1)
    img = models.ImageField(upload_to='static/img/lbt/')
    name = models.CharField(max_length=20, unique=True)
    href = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "BxSlide"
        verbose_name_plural = '首页轮播'

    def __str__(self):
        return self.name


class Course(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重', default=0)
    icon = models.ImageField(verbose_name='图标', upload_to='static/img/icon/', null=True, blank=True)
    name = models.CharField(verbose_name='名称', max_length=32, unique=True)
    summary = models.TextField(verbose_name='简介', default="summary")

    class Meta:
        db_table = 'Course'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重', default=0)
    name = models.CharField(max_length=10, verbose_name='姓名', unique=True)
    salary = models.IntegerField(verbose_name='薪资')
    pic = models.ImageField(verbose_name='头像', upload_to='static/img/student_img/')
    company = models.CharField(max_length=50, verbose_name='就业单位')

    class Meta:
        db_table = 'StudentInfo'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.name


class StudentMoreInfo(models.Model):
    name = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='年龄')
    detail = models.TextField(verbose_name='个人简介')

    class Meta:
        db_table = 'StudentMoreInfo'
        verbose_name_plural = '学生详情'

    def __str__(self):
        return self.name.name


class News(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重', default=0)
    title = models.CharField(verbose_name='标题', max_length=32)
    detail = models.TextField(verbose_name='简介', null=True)
    text = models.TextField(verbose_name='公告信息')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'News'
        verbose_name_plural = '最新公告'

    def __str__(self):
        return self.title


class SchoolActivity(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重', default=0)
    name = models.CharField(verbose_name='活动名称', max_length=32)
    leader = models.CharField(verbose_name='负责人', max_length=20)
    title = models.TextField(verbose_name='简介', max_length='30')
    detail = models.TextField(verbose_name='活动详情')
    photo = models.ImageField(verbose_name='活动照片', upload_to='static/img/school_img/')

    class Meta:
        db_table = 'SchoolActivity'
        verbose_name_plural = '校园活动'

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=20, verbose_name='职位')
    salary = models.IntegerField(verbose_name='薪资')
    skill = models.TextField(verbose_name='能力要求')

    class Meta:
        db_table = 'JobFound'
        verbose_name_plural = '招聘信息'

    def __str__(self):
        return self.name


class Direction(models.Model):
    weight = models.IntegerField(verbose_name='权重', default=0)
    name = models.CharField(verbose_name='名称', max_length=32)
    classification = models.ManyToManyField('Classification')

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '视频方向'

    def __str__(self):
        return self.name


class Classification(models.Model):
    weight = models.IntegerField(verbose_name='权重', default=0)
    name = models.CharField(verbose_name='名称', max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '视频分类'

    def __str__(self):
        return self.name


class Level(models.Model):
    title = models.CharField(verbose_name='级别', max_length=32)

    class Meta:
        verbose_name_plural = '级别'
        db_table = 'Level'

    def __str__(self):
        return self.title


class Video(models.Model):
    status_choice = (
        (1, '下线'),
        (2, '上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    level = models.ForeignKey('Level')
    weight = models.IntegerField(verbose_name='权重', default=0)
    classification = models.ForeignKey('Classification', null=True, blank=True)
    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=32)
    img = models.ImageField(verbose_name='图片', upload_to='static/img/video/')
    href = models.CharField(verbose_name='视频地址', max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: 'Video'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.title
