from django.shortcuts import get_object_or_404, render
from .models import MainContent

def index(request):
    # -는 역순 정렬, 가장 최신 콘텐츠를 상단에 노출시키기 위함
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list' : content_list}
    # render : content_list의 데이터를 product/content_list.html 파일에 적용 후 HTML을 리턴
    return render(request, 'product/content_list.html', context)

def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk = content_id)
    context = {'content_list' : content_list}
    return render(request, 'product/content_detail.html', context)