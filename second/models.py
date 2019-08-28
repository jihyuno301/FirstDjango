from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()

    # 게시글 내용 생성될때의 시간
    created_at = models.DateField(auto_now_add=True)
    # 수정될 때마다 넣을 데이터
    updated_at = models.DateTimeField(auto_now=True)

    # num_start = models.IntegerField(), 숫자

