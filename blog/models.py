from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    likes = models.PositiveIntegerField(default=0)

    def total_likes(self):
        return self.likes.count()   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_abstract(self):
        return ' '.join(self.text.split()[0:50]) + ' ...'

    @models.permalink
    def get_absolute_url(self):
        return ('post-detail',[self.id])

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.DO_NOTHING,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
