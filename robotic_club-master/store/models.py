from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Item_discription(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=40,default="initial")
    text = models.TextField()
    amount = models.IntegerField(default=1)
    photo1 = models.ImageField(upload_to='images/', blank=True)
    photo2 = models.ImageField(upload_to='images/', blank=True)

    def requested(self,amt):
        if self.amount >= amt:
            self.amount = self.amount-amt

            print("got request")
            self.save()
            return True
        else:
            return False

    def add_(self,amt):
        self.amount = self.amount + amt


class Request_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    requesting_user = models.CharField(max_length=50,default='initial')
    product_name = models.CharField(max_length=40,default="initial")
    first = models.CharField(max_length=50,default='initial')
    last = models.CharField(max_length=50,default='initial')
    amount = models.IntegerField(default=1)
    dis_id = models.IntegerField(null=True)


class Cart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    requesting_user = models.CharField(max_length=50,default='initial')
    first = models.CharField(max_length=50,default='initial')
    last = models.CharField(max_length=50,default='initial')
    amount = models.IntegerField(default=1)
    dis_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=40,default="initial")
    photo1 = models.ImageField(upload_to='images/',blank = True)



    