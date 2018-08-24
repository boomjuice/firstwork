from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.


def index(request):
    slide_list = BxSlide.objects.filter(status=1).values('img', 'href')
    news_list = News.objects.filter(status=1).values('weight', 'title', 'detail')
    activity_list = SchoolActivity.objects.filter(status=1).values('name', 'title', 'photo', 'leader', 'weight')
    course = Course.objects.filter(status=1).values('name', 'summary', 'icon')
    students = StudentInfo.objects.filter(status=1).values('name', 'salary', 'company',
                                                           'pic', 'studentmoreinfo__detail', 'weight')
    jobs = Job.objects.values('name', 'salary')
    context = {
        'slide_list': slide_list,
        'news_list': news_list,
        'activity_list': activity_list,
        'course': course,
        'students': students,
        'jobs': jobs

    }

    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def student(request):
    return render(request, 'student.html')


def video(request, *args, **kwargs):
    condition = {}
    for k, v in kwargs.items():
        # 将获取的id 放进列表
        temp = int(v)
        kwargs[k] = temp

    direction_id = kwargs.get('direction_id')
    classification_id = kwargs.get('classification_id')
    level_id = kwargs.get('level_id')

    direction_list = Direction.objects.all()
    # list 有 name 和 Classification [] 多对多

    if direction_id == 0:
        class_list = Classification.objects.all()
        if classification_id == 0:
            pass
        else:
            condition['classification_id'] = classification_id
    else:
        direction_obj = Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()
        vlist = direction_obj.classification.all().values_list('id')
        if not vlist:
            classification_id_list = []
        else:
            classification_id_list = list(zip(*vlist))[0]

        if classification_id == 0:
            condition['classification_id__in'] = classification_id_list
        else:
            if classification_id in classification_id_list:
                condition['classification_id'] = classification_id
            else:
                kwargs['classification_id'] = 0
                condition['classification_id__in'] = classification_id_list

    if level_id == 0:
        pass
    else:
        condition['level_id'] = level_id

    level_list = Level.objects.all()

    video_list = Video.objects.filter(**condition)
    context = {
        'class_list': class_list,
        'level_list': level_list,
        'kwargs': kwargs,
        'video_list': video_list,
        'direction_list': direction_list,
    }
    return render(request, 'video.html', context=context)


def get_student(request):
        nid = request.GET.get('nid')
        img_list = StudentInfo.objects.filter(weight__lt=10).filter(id__gt=nid).values('id', 'pic',)
        img_list = list(img_list)
        ret = {
            'status': True,
            'data': img_list,
        }
        return JsonResponse(ret)
