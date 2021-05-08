'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from djongo import models
from django.conf import settings
from unixtimestampfield.fields import UnixTimeStampField
from SocialBookApp.models.usermodels import (App_User)
<<<<<<< HEAD
<<<<<<< HEAD
=======
# from SocialBookApp.models.bookmodels import (BookUserTree)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
from treenode.models import TreeNodeModel

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200,default="BookName")
    authname = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True,null=True)
    booktype =  models.CharField(max_length=200,default="Text")
    rate = models.FloatField(default=0.0)
    stars = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
<<<<<<< HEAD
    dp = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
=======
    dp = models.TextField()
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    desc = models.CharField(max_length=500, default="")
    

class TextBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    content = models.TextField()
    type = models.CharField(max_length=200)
    publist = UnixTimeStampField(auto_now=True, null=True)

class BookComments(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    comments = models.TextField()
    ratings = models.FloatField(default=5)
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)
<<<<<<< HEAD


=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

class OwnBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='Buyer')
    Own = models.CharField(max_length=200)
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='referrer')
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)

class profileTXTPost(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    post = models.TextField()
    header = models.CharField(max_length=50,null=True)
    types = models.CharField(max_length=50,null=True, blank=True)
    related = models.CharField(max_length=50,null=True, blank=True)
    url = models.CharField(max_length=200,null=True)
    dp = models.TextField(null=True, blank=True)
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    publist = UnixTimeStampField(auto_now=True,null=True)

    def save(self, *args, **kwargs):

        if self.dp == None and self.types != None and self.related != None:

            if  self.types == 'Book':
                list = Book.objects.get(id=self.related)
                self.dp = list.dp

            if  self.types == 'User':
                list = App_User.objects.get(id=self.related)
                self.dp = list.dp

            if  self.types == 'Post':
                list = profileTXTPost.objects.get(id=self.related)
                self.dp = list.dp

        elif self.dp != None:
            self.dp = self.dp

        else:
            self.dp = ""

        return super(profileTXTPost, self).save(*args, **kwargs)

class TXTPostComments(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    post = models.ForeignKey(profileTXTPost, on_delete=models.CASCADE)
    comments = models.TextField()
    likes = models.IntegerField(default=0)
    publist = UnixTimeStampField(auto_now=True,null=True)

class BookWishlist(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True, null=True)

<<<<<<< HEAD
=======
class BookTreeDB(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    Tree = models.IntegerField(default=0)

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
class BookTreeConnect(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    Tree = models.IntegerField(default=0)

class BookNewsFeed(models.Model):

    Author = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='youself')
    Buyer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='bookBuyer')
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='feedreferrer')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class FriendNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendfriend')
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class CommentsNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='commentyou')
    Author = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='Auth')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    Bookcomments = models.ForeignKey(BookComments, on_delete=models.CASCADE)
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

<<<<<<< HEAD
class TXTPostCommentsNewsFeed(models.Model):
    Postuser = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='Postuser')
    PostWriter = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='PostWriter')
    post = models.ForeignKey(profileTXTPost, on_delete=models.CASCADE)
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True, null=True)

class BookTickerNewsFeed(models.Model):

    Author = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='Authjson')
    Buyer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='BuyerJson')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='BookJson' )
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class BookUserTree(TreeNodeModel):

    
    
    treenode_display_field = 'UserName'
    
=======
class BookUserTree(TreeNodeModel):

    # the field used to display the model instance
    # default value 'pk'
    treenode_display_field = 'UserName'
    #
    # name = models.CharField(max_length=50)

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
<<<<<<< HEAD
    UserName = models.CharField(max_length=200)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'BookUserTree'
        verbose_name_plural = 'BookUserTrees'

    def save(self, *args, **kwargs):
        list = App_User.objects.get(id=self.user.id)
        self.UserName = list.username
<<<<<<< HEAD
        return super(BookUserTree, self).save(*args, **kwargs)
=======
        return super(BookUserTree, self).save(*args, **kwargs)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
    Own = models.CharField(max_length=200)
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='referrer')
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)

class BookWishlist(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True, null=True)

class BookTreeConnect(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    Tree = models.IntegerField(default=0)

class BookNewsFeed(models.Model):

    Author = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='youself')
    Buyer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='bookBuyer')
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='feedreferrer')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class FriendNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendfriend')
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class CommentsNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='commentyou')
    Author = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='Auth')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    Bookcomments = models.ForeignKey(BookComments, on_delete=models.CASCADE)
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class BookUserTree(TreeNodeModel):

    
    
    treenode_display_field = 'UserName'
    
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=200)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'BookUserTree'
        verbose_name_plural = 'BookUserTrees'

    def save(self, *args, **kwargs):
        list = App_User.objects.get(id=self.user.id)
        self.UserName = list.username
        return super(BookUserTree, self).save(*args, **kwargs)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
