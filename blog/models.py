from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #Add last_edited_date to model
    #modify templates to display created_date & last_edited_date
    #see https://github.com/trailhawks/lawrencetrailhawks/blob/master/blog/models.py#l34
    #for guidance

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #provides count of comments that have been approved
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
