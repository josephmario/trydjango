from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('posts:post_detail', kwargs={'id':self.id})
        # return '/posts/detail/%s/' %(self.id)

class History(models.Model):
    order = models.CharField(max_length=120)
    status = models.CharField(max_length=500, blank=True, null=True)
    status_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}: {1}'.format(self.status, self.status_updated_at)
