from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') # relates to some other Model # Are all these methods?
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) # what does this mean?

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # Something you do with the class
        return self.title
