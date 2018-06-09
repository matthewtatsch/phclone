from django.db import models
from django.contrib.auth.models import User

# Product class


class Product(models.Model):
    '''Product model'''

    title = models.CharField(max_length=30)
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # hunter
