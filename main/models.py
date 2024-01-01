from django.db import models

# Create your models here.
class Notice(models.Model):
    title=models.CharField(max_length=100)
    likeCount=models.IntegerField(blank=True)
    viewCount=models.IntegerField(blank=True)
    contents=models.TextField(blank=True)

    def __str__(self):
        #return self.title
        return f'제목 : {self.title}, 좋아요수: {self.likeCount}, 조회수 : {self.viewCount}'