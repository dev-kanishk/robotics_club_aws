from django.db import models
from django.conf import settings



class Tokens(models.Model):

	token_code = models.CharField(max_length = 7)



class UserProfile(models.Model):
	user = models.CharField(max_length=50)
	roll_no = models.CharField(max_length=10)
	mobile_no = models.CharField(max_length=10)
	is_mentor = models.BooleanField(default=True)
	token_got = models.CharField(max_length=7,help_text="Will be provided by club mentors")
	branch = models.CharField(max_length=40,default="old")

class Notification(models.Model):
	 user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	 subject = models.CharField(max_length = 100, blank = False)
	 text = models.TextField(blank=False)
	 read = models.BooleanField(default=False)
	 send_by = models.CharField(max_length= 100, default = "admin", blank = False)
	 unique_code = models.IntegerField( default = -1, blank = False)
