'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''

from django.contrib.auth.models import User
from djongo import models
from django.conf import settings
from fernet_fields import EncryptedTextField
from unixtimestampfield.fields import UnixTimeStampField
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765



class App_User(models.Model):

    user = models.ForeignKey(User, related_name='App_User',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=200,unique=True)
    usertype = models.CharField(max_length=200)
    password = EncryptedTextField(max_length=600)
    country = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)
    active = models.BooleanField(default=False)
    contact =  models.CharField(max_length=200,null=True)
    friends = models.IntegerField(default=0)
    wallet = models.IntegerField(default=500)
<<<<<<< HEAD
<<<<<<< HEAD
    dp = models.TextField(null=True, blank=True)
=======
    dp = models.TextField()
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
    dp = models.TextField()
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.email = self.email.lower()
<<<<<<< HEAD
<<<<<<< HEAD
        self.usertype = self.usertype.lower()
        return super(App_User, self).save(*args, **kwargs)
=======
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
        self.usertype = self.usertype.lower()
        return super(App_User, self).save(*args, **kwargs)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

        return super(App_User, self).save(*args, **kwargs)

class friendlist(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistfriend')
    relationship = models.CharField(max_length=200)

class profileComment(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentyou')
    chatter = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentfriend')
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True,editable=True)
    likes = models.IntegerField(default=0)

<<<<<<< HEAD
<<<<<<< HEAD
=======
class profileTXTPost(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    post = models.TextField()
=======
class profileTXTPost(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    post = models.TextField()
    header = models.CharField(max_length=50,null=True)
    types = models.CharField(max_length=50,null=True)
    related = models.CharField(max_length=50,null=True)
    url = models.CharField(max_length=200,null=True)
    dp = models.TextField()
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    publist = UnixTimeStampField(auto_now=True,null=True)

<<<<<<< HEAD



=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
class TXTPostComments(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    post = models.ForeignKey(profileTXTPost, on_delete=models.CASCADE)
    comments = models.TextField()
    likes = models.IntegerField(default=0)
    publist = UnixTimeStampField(auto_now=True,null=True)

<<<<<<< HEAD
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
