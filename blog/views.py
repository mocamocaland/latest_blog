from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model = Post

    def get_queryset(self):
        # return Post.objects.order_by('-created_at') 記事一覧を最新順で表示を行う
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(title=keyword) #titleで絞りたい場合
        return queryset
