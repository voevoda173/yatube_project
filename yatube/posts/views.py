from django.http import HttpResponse


def index(request):
    return HttpResponse('YATUBE - Главная страница')

def group_posts(request, slug):
    return HttpResponse(f' YARUBE - Группа {slug}')