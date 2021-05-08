'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
import os
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
<<<<<<< HEAD
<<<<<<< HEAD
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed,TXTPostCommentsNewsFeed,profileTXTPost,TXTPostComments,BookTickerNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment)
from django.contrib.auth.models import User
from SocialBookApp.serializers.serializers import (BookSerializer,BookSerializerI,BookSerializerII,BookTreeDBSerializer,App_UserSerializer,App_UserSerializerII,App_UserSerializerforPUT,UserSerializer,friendlistSerializer,profileTXTPostSerializer,App_UserSerializerI,profileTXTPostSerializerI,TXTPostCommentsSerializer,TXTPostCommentsSerializerI,profileCommentSerializer,TextBookSerializer,TextBookSerializerI,BookCommentsSerializer,OwnBookSerializer,OwnBookSerializerI,WishlistSerializer,profileCommentSerializerI,BookCommentsSerializerI,WishlistSerializerI,BookNewsFeedSerializer,FriendNewsFeedSerializer,FriendNewsFeedSerializerI,BookNewsFeedSerializerI,CommentsNewsFeedSerializerI,CommentsNewsFeedSerializer,TXTPostCommentsNewsFeedSerializer,TXTPostCommentsNewsFeedSerializerI, BookTickerNewsFeedSerializer, BookTickerNewsFeedSerializerI  )
=======
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileTXTPost,TXTPostComments,profileComment)
from django.contrib.auth.models import User
from SocialBookApp.serializers.serializers import (BookSerializer,BookSerializerI,BookSerializerII,BookTreeDBSerializer,App_UserSerializer,App_UserSerializerII,UserSerializer,friendlistSerializer,profileTXTPostSerializer,App_UserSerializerI,profileTXTPostSerializerI,TXTPostCommentsSerializer,TXTPostCommentsSerializerI,profileCommentSerializer,TextBookSerializer,TextBookSerializerI,BookCommentsSerializer,OwnBookSerializer,OwnBookSerializerI,WishlistSerializer,profileCommentSerializerI,BookCommentsSerializerI,WishlistSerializerI,BookNewsFeedSerializer,FriendNewsFeedSerializer,FriendNewsFeedSerializerI,BookNewsFeedSerializerI,CommentsNewsFeedSerializerI,CommentsNewsFeedSerializer  )
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileTXTPost,TXTPostComments,profileComment)
from django.contrib.auth.models import User
from SocialBookApp.serializers.serializers import (BookSerializer,BookSerializerI,BookSerializerII,BookTreeDBSerializer,App_UserSerializer,App_UserSerializerII,App_UserSerializerforPUT,UserSerializer,friendlistSerializer,profileTXTPostSerializer,App_UserSerializerI,profileTXTPostSerializerI,TXTPostCommentsSerializer,TXTPostCommentsSerializerI,profileCommentSerializer,TextBookSerializer,TextBookSerializerI,BookCommentsSerializer,OwnBookSerializer,OwnBookSerializerI,WishlistSerializer,profileCommentSerializerI,BookCommentsSerializerI,WishlistSerializerI,BookNewsFeedSerializer,FriendNewsFeedSerializer,FriendNewsFeedSerializerI,BookNewsFeedSerializerI,CommentsNewsFeedSerializerI,CommentsNewsFeedSerializer  )
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
from rest_framework.response import Response
import logging
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json
from rest_framework.authtoken.models import (Token)
from SocialBookApp.views.process import (smtpsender)
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from django.db.models import Q
<<<<<<< HEAD
import PyPDF2
import slate3k as slate
from django.core import serializers
from django.conf import settings
import base64
import os
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
from django.forms.models import model_to_dict
from itertools import chain
from django.core import serializers
import slate3k as slate
<<<<<<< HEAD
from django.core.exceptions import ObjectDoesNotExist
import base64
from django.conf import settings
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765


logger = logging.getLogger("book.task")

class BookVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def list_Book(self, request):
        try:
            book_list = Book.objects.all()
            serializer = BookSerializerI(book_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            for i in serializer.data:
                logger.info(i)
                list = App_User.objects.get(id=i['authname'])
                serializer1 = App_UserSerializerII(list)
                i['authJSON'] = serializer1.data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def create_Book(self, request):
        try:
            serializer = BookSerializerI(data=request.data)
            if serializer.is_valid():
                serializer.save()
                own={}
                own["Book"]=serializer.data['id']
                own["user"] = serializer.data['authname']
                own["Own"] = "yes"
                own["referrer"] = serializer.data['authname']
                serializerw = OwnBookSerializer(data=own)
                if serializerw.is_valid():
                    serializerw.save()
                list = Book.objects.get(id=serializer.data['id'])
                list1 = App_User.objects.get(id=serializer.data['authname'])
                treeobj = BookUserTree(Book=list,user=list1)
                treeobj.save()
                tree = {}
                tree["Book"] = serializer.data['id']
                list8 = BookUserTree.objects.get(Book_id=serializer.data['id'])
                tree["Tree"] = list8.id
                serializer1 = BookTreeDBSerializer(data=tree)
                if serializer1.is_valid():
                    serializer1.save()
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Book(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = Book.objects.get(id=pk)
            serializer = BookSerializerI(list)
            list = App_User.objects.get(id=serializer.data['authname'])
            serializer1 = App_UserSerializerII(list)
            logger.info(serializer1.data)
            datas = serializer.data.copy()
            datas['authJSON'] = serializer1.data
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            dbi = BookComments.objects.filter(Q(Book_id=int(pk)))
            logger.info("hi")
            logger.info(dbi)
            serializer5 = BookCommentsSerializer(dbi, many=True)
            comments = serializer5.data.copy()
            for i in comments:
<<<<<<< HEAD
<<<<<<< HEAD
                list11 = App_User.objects.get(id=i['user'])
=======
                logger.info("i")
                logger.info(i["user"])
                logger.info(i)
                list11 = App_User.objects.get(id=int(i["user"]))
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
                list11 = App_User.objects.get(id=i['user'])
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                serializer11 = App_UserSerializerII(list11)
                i["AuthJSON"] = serializer11.data

            datas['CommentJSON'] = comments
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_Book(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Book.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Book(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = Book.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = Book.objects.get(id=pk)
                serializer = BookSerializerI(list)

                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class UserVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer


    def list_User(self, request):
        try:
            App_User_list = App_User.objects.all()
            serializer = App_UserSerializer(App_User_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



    def get_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializer(list)
            auth = Token.objects.get(user=pk)
            datas = serializer.data.copy()
            datas["token"] = auth.key
            logger.info(auth.key)
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def delete_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = App_User.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_User(self, request, *args, **kwargs):
        try:
            serializer = App_UserSerializerforPUT(data=request.data)
            pk = self.kwargs['pk']
            item = App_User.objects.get(id=pk)
            logger.info("in views")
            if serializer.is_valid():
                logger.info("valid")
                serializer.update(item, serializer.data)
            else:
                return Response(serializer.errors, status=200)
            pk = self.kwargs['pk']
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializer(list)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



@api_view(['GET'])
<<<<<<< HEAD
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
=======
@permission_classes((AllowAny, ))
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
def activate_User(request):
    try:
        pk = request.query_params.get('pk')
        list = App_User.objects.get(user=int(pk))
        list.active = True
        list.save()
<<<<<<< HEAD
        return redirect ("http://acerelocations-frontend.s3-website.us-east-2.amazonaws.com/verified-message/"+pk)
=======
        return redirect ("http://localhost:3000/Verified-message/")
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)

<<<<<<< HEAD
=======

>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def activate_Tree(request):
    try:
        pks = request.query_params.get('pk')
        user = request.query_params.get('user')

        datas = BookTreeConnect.objects.get(Book=int(pks))
        serializer = BookTreeDBSerializer(datas)
        pk = BookUserTree.objects.get(id=int(serializer.data["Tree"]))
<<<<<<< HEAD
        logger.info(pk.get_tree())
        logger.info(activate_Treelist(pk.get_descendants_tree(),pks))
        logger.info(json.dumps(activate_Treelist(pk.get_descendants_tree(),pks)))
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        list1 = Book.objects.get(id=int(pk.Book_id))
        serializer1 = BookSerializerII(list1)
        list2 = App_User.objects.get(id=serializer1.data['authname'])
        serializer11 = App_UserSerializerII(list2)
<<<<<<< HEAD
        logger.info(serializer11.data)

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        res = {}
        res["Book"]=serializer1.data
        res["AuthJSON"] = serializer11.data
        res["BookTree"] = json.loads(json.dumps(activate_Treelist(pk.get_descendants_tree(),pks)))
        return Response(res, status=200)
<<<<<<< HEAD

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


def activate_Treelist(tree,num):

    for i in tree:
        logger.info(i['node'].tn_children_count)

        logger.info(str(i['node']).split("— ")[-1])
        list = App_User.objects.get(username=str(i['node']).split("— ")[-1])
        serializer = App_UserSerializerII(list)
        i['node']= serializer.data
        logger.info(num)

        activate_Treelist(i['tree'],num)
    return tree


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def activate_Tree(request):
    try:
        pks = request.query_params.get('pk')
        user = request.query_params.get('user')

        datas = BookTreeConnect.objects.get(Book=int(pks))
        serializer = BookTreeDBSerializer(datas)
        pk = BookUserTree.objects.get(id=int(serializer.data["Tree"]))
        list1 = Book.objects.get(id=int(pk.Book_id))
        serializer1 = BookSerializerII(list1)
        list2 = App_User.objects.get(id=serializer1.data['authname'])
        serializer11 = App_UserSerializerII(list2)
        res = {}
        res["Book"]=serializer1.data
        res["name"] = serializer11.data['username']
        res["attributes"]=serializer11.data
        res["children"] = json.loads(json.dumps(activate_Treelist(pk.get_descendants_tree(),pks)))
        return Response(res, status=200)
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


def activate_Treelist(tree,num):

    for i in tree:
        list = App_User.objects.get(username=str(i['node']).split(" ")[-1])
        serializer = App_UserSerializerII(list)
<<<<<<< HEAD
        i['node'] = serializer.data
        i['name']= serializer.data['username']
        i['attributes'] = serializer.data
        i['children']=i['tree']
=======
        i['node']= serializer.data
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        activate_Treelist(i['tree'],num)
    return tree


@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_User(request):
    try:
        validated_data ={}
        validated_data['username'] = request.data['username'].lower()
        validated_data['email'] = request.data['email'].lower()

        User_list = User.objects.all()
        for i in User_list:
            if i.username == validated_data['username']:
                return Response("Username already exist",status=404)
            if i.email == validated_data['email']:
                return Response("Email already exit",status=404)
    
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=200)
        logger.info(serializer.data["username"])

        list = User.objects.get(username=serializer.data["username"])
        datas = request.data.copy()
        datas["user"] =list.id
        try:
            Token.objects.create(user=list)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)
        logger.info("ji")
        auth = Token.objects.get(user=list.id)
        serializer = App_UserSerializer(data=datas)
        logger.info("jay")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data.copy()
            datas["token"] = auth.key
            datas["message"] = "A verification mail will be sent to mail id to activate your account."
            logger.info(auth.key)
            logger.info(auth.key)
            smtpsender(datas,list.id)
            return Response(datas, status=200)
        else:
            return Response(serializer.errors, status=200)
        return Response(serializer.errors, status=200)


        # return Response(serializer.errors, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)

class friendlistVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = friendlist.objects.all()
    serializer_class = friendlistSerializer

    def create_relationship(self, request):
        try:
            serializer = friendlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data.copy()
                datas['comments'] = datas['relationship']
                serializer1 = FriendNewsFeedSerializer(data=datas)
                if serializer1.is_valid():
                    serializer1.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_relationship(self, request, *args, **kwargs):
        try:
<<<<<<< HEAD
            
            
            dbi = friendlist.objects.filter(Q(friend_id=int(request.data['user'])) & Q(relationship="addfriend") & Q(user_id=int(request.data['friend']))  )
            logger.info(dbi)
            logger.info("ll")
            if not dbi:
                return Response("No related Query Exit", status=200)
            logger.info(dbi[0].user)
             
            item1 = friendlist.objects.get(id=dbi[0].id)
            logger.info(item1)
            logger.info("hi")
            arr ={}
            arr['id']=item1.id
            arr['user']= item1.user.id
            arr['friend']=item1.friend.id
            arr['relationship']="friends"
            serializer = friendlistSerializer(data=arr)
=======
            serializer = friendlistSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = friendlist.objects.get(id=pk)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            if serializer.is_valid():
                datas = serializer.data.copy()
                if datas['relationship'] == 'friends':
                    list = App_User.objects.get(id=datas["user"])
                    list.friends = list.friends + 1
                    list.save()
                    list = App_User.objects.get(id=datas["friend"])
                    list.friends = list.friends + 1
                    list.save()
<<<<<<< HEAD
<<<<<<< HEAD
                serializer.update(item1, serializer.data)
=======
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
                serializer.update(item, serializer.data)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                datas1 = serializer.data.copy()
                datas1['comments'] = datas1['relationship']
                serializer1 = FriendNewsFeedSerializer(data=datas1)
                if serializer1.is_valid():
                    serializer1.save()
<<<<<<< HEAD
<<<<<<< HEAD
=======
                serializer.update(item, serializer.data)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_friendlist(self, request,*args, **kwargs):
<<<<<<< HEAD
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends"))
            logger.info("hi")
            logger.info(dbi)
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    logger.info("hi")
                    logger.info(i.friend)
                    list = App_User.objects.get(id=i.friend_id)
                    logger.info(list)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
                if i.friend_id == int(pk):
                    logger.info("hi")
                    logger.info(i.user)
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
            # serializer = friendlistSerializer(dbi, many=True)
            logger.info(dbi)
            logger.info("dbi")
            logger.info(arr)
            serializer = App_UserSerializer("arr", many=True)
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profile(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializerI(list)
            # auth = Token.objects.get(user=pk)
            datas = serializer.data.copy()
            # datas["token"] = auth.key
            # logger.info(auth.key)
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_acceptfriendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(friend_id=int(pk)) & Q(relationship="addfriend") )
            logger.info("hi")
            logger.info(dbi)
            serializer = friendlistSerializer(dbi, many=True)
            datas = serializer.data.copy()
            arr = []
            for i in datas:
<<<<<<< HEAD
                list = App_User.objects.get(id=i["user"])
                logger.info(list)
                serializerF = App_UserSerializerI(list)
                arr.append(serializerF.data)
=======

                list = App_User.objects.get(id=i["friend"])
                logger.info(list)
                serializerF = App_UserSerializerI(list)
                arr.append(serializerF.data)

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_allUsers(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
<<<<<<< HEAD
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends") | Q(user_id=int(pk)) & Q(relationship="addfriend") | Q(friend_id=int(pk)) & Q(relationship="addfriend"))
=======
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends"))
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    list = App_User.objects.get(id=i.friend_id)
<<<<<<< HEAD
=======
                    logger.info(list)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data['id'])
                if i.friend_id == int(pk):
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data['id'])
            App_User_list = App_User.objects.all()
            serializerF = App_UserSerializerI(App_User_list, many=True)
            list = App_User.objects.get(id=pk)
=======
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends"))
            logger.info("hi")
            logger.info(dbi)
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    logger.info("hi")
                    logger.info(i.friend)
                    list = App_User.objects.get(id=i.friend_id)
                    logger.info(list)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
                if i.friend_id == int(pk):
                    logger.info("hi")
                    logger.info(i.user)
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
            # serializer = friendlistSerializer(dbi, many=True)
            logger.info(dbi)
            logger.info("dbi")
            logger.info(arr)
            serializer = App_UserSerializer("arr", many=True)
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profile(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializerI(list)
            # auth = Token.objects.get(user=pk)
            datas = serializer.data.copy()
            # datas["token"] = auth.key
            # logger.info(auth.key)
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_acceptfriendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(friend_id=int(pk)) & Q(relationship="addfriend") )
            logger.info("hi")
            logger.info(dbi)
            serializer = friendlistSerializer(dbi, many=True)
            datas = serializer.data.copy()
            arr = []
            for i in datas:
                list = App_User.objects.get(id=i["friend"])
                logger.info(list)
                serializerF = App_UserSerializerI(list)
                arr.append(serializerF.data)
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_allUsers(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends") | Q(user_id=int(pk)) & Q(relationship="addfriend") | Q(friend_id=int(pk)) & Q(relationship="addfriend"))
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    list = App_User.objects.get(id=i.friend_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data['id'])
                if i.friend_id == int(pk):
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data['id'])
            App_User_list = App_User.objects.all()
            serializerF = App_UserSerializerI(App_User_list, many=True)
            list = App_User.objects.get(id=pk)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            serializerU = App_UserSerializer(list)
            arr.append(serializerU.data['id'])
            datas = serializerF.data.copy()
            findatas =[]
            for i in datas:
                if i['id'] not in arr:
                    findatas.append(i)
            return Response(findatas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_allUserstype(self, request,*args, **kwargs):
        try:
            App_User_list = App_User.objects.all()
            pk = request.query_params.get('type')

            dbi = App_User.objects.filter(Q(usertype=(pk)))

            serializer = App_UserSerializerI(dbi, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_notfriendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas = []
            datas =[]
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="addfriend")  )
            logger.info("hi")
            logger.info(dbi)
            serializer = friendlistSerializer(dbi, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def Unfriend(self, request,*args, **kwargs):
        try:
<<<<<<< HEAD
            pk = request.query_params.get('pk')
            friend = request.query_params.get('friend')
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") & Q(friend_id=int(friend)) | Q(user_id=int(friend)) & Q(relationship="friends") & Q(friend_id=int(pk)) )
            serializer = friendlistSerializer(dbi[0])

            item = friendlist.objects.get(id=serializer.data['id'])
=======
            pk = self.kwargs['pk']
            item = friendlist.objects.get(id=pk)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            item.delete()
            return Response(json.loads('{"response" : "Unfriend or Ignored successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def list_friendlist(self, request):
        try:
            friendlist_list = friendlist.objects.all()
            serializer = friendlistSerializer(friendlist_list, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class profileTXTPostVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = profileTXTPost.objects.all()
    serializer_class = profileTXTPostSerializer


    def create_profileTXTPost(self, request):
        try:
<<<<<<< HEAD
            validated_data ={}
            validated_data['related'] = request.data['related']
            validated_data['types'] = request.data['types']
            logger.info(type(request.data['related']))
            if (validated_data['related'] != "" and validated_data['types'] == "") or (validated_data['related'] == "" and validated_data['types'] != ""):
                logger.info("Error")
                
                return Response("Both related and Types Must have value if needed", status=200)
            if validated_data['types'] == "Book":
                try:
                    list1 = Book.objects.get(id=int(validated_data['related']))
                    
                except ObjectDoesNotExist:
                    logger.info("Error")
                    
                    return Response("No Related Book Available", status=200)
                
            if validated_data['types'] == "User":
                try:
                    list1 = App_User.objects.get(id=int(validated_data['related']))

                except ObjectDoesNotExist:
                    logger.info("Error")
                    
                    return Response("No Related User Found", status=200)

            if validated_data['types'] == "Post":
                try:
                    list1 = profileTXTPost.objects.get(id=int(validated_data['related']))

                except ObjectDoesNotExist:
                    logger.info("Error")
                    
                    return Response("No Related Post Found", status=200)

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            serializer = profileTXTPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_profile_post(self, request):
        try:
            pk = request.query_params.get('pk')
            dbi = profileTXTPost.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = profileTXTPostSerializer(dbi, many=True)
            datas = serializer.data.copy()
            postarr = []
            for i in datas:
                listPU = App_User.objects.get(id=i['user'])
                serializerPU = App_UserSerializerII(listPU)
                i['authJSON'] = serializerPU.data
<<<<<<< HEAD
            
            datasS = datas.copy()

            for i in datasS:
                logger.info(i)
                dbi = TXTPostComments.objects.filter(Q(post=(i["id"])))
                serializerC = TXTPostCommentsSerializer(dbi, many=True)
                dataC = serializerC.data.copy()
                for j in dataC:
                    listU = App_User.objects.get(id=j["user"])
                    serializerUS = App_UserSerializerII(listU)
                    j['userJSON'] = serializerUS.data
                i["CommentsJSON"] = dataC

            return Response(datasS, status=200)
=======

            return Response(datas, status=200)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_home_post(self, request):

        try:
            pk = request.query_params.get('pk')
            datas = []
            dbi = friendlist.objects.filter(
                Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends"))
            logger.info("hi")
            logger.info(dbi)
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    logger.info("hi")
                    logger.info(i.friend)
                    list = App_User.objects.get(id=i.friend_id)
                    logger.info(list)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
                if i.friend_id == int(pk):
                    logger.info("hi")
                    logger.info(i.user)
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
            # serializer = friendlistSerializer(dbi, many=True)
            logger.info(dbi)
            logger.info("dbi")
            logger.info(arr)
            postarr = []
            dbi = profileTXTPost.objects.filter(Q(user_id=int(pk)))
            logger.info("hi")
            logger.info(dbi)
            logger.info("hii")
            serializer = profileTXTPostSerializer(dbi, many=True)
            for i in serializer.data:
                postarr.append(i)
            for i in arr:
                dbi = profileTXTPost.objects.filter(Q(user_id=int(i["id"])))
                logger.info("hii")
                logger.info(dbi)
                serializer1 = profileTXTPostSerializer(dbi, many=True)
                for j in serializer1.data:
                    postarr.append(j)

            logger.info(postarr)
            for i in postarr:
                listPU = App_User.objects.get(id=i['user'])
                serializerPU = App_UserSerializerII(listPU)
                i['authJSON'] = serializerPU.data
<<<<<<< HEAD

            datasH = postarr.copy()
            for i in datasH:
                dbi = TXTPostComments.objects.filter(Q(post=(i["id"])))
                serializerC = TXTPostCommentsSerializer(dbi, many=True)
                dataC = serializerC.data.copy()
                for j in dataC:
                    listU = App_User.objects.get(id=j["user"])
                    serializerUS = App_UserSerializerI(listU)
                    j['userJSON'] = serializerUS.data
                i["CommentsJSON"] = dataC

            datasH = sorted(datasH, key=lambda k: k['publist'])
=======
            postarr = sorted(postarr, key=lambda k: k['publist'])
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            return Response(postarr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def delete_Post(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = profileTXTPost.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Post deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
    def update_Like(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
                                        
            item = profileTXTPost.objects.get(id=pk)
            item.likes = item.likes + 1
            item.save()
            return Response(json.loads('{"response" : "Post updated successfully."}'), status=200)
=======
    def update_Post(self, request, *args, **kwargs):
        try:
            serializer = profileTXTPostSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = profileTXTPost.objects.get(id=pk)
            logger.info(item)
            if serializer.is_valid():
                logger.info("hi")
                serializer.update(item, serializer.data)
            else:
                return Response(serializer.errors, status=200)

            list = profileTXTPost.objects.get(id=pk)
            serializer = profileTXTPostSerializer(list)
            return Response(serializer.data, status=200)

>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
    def update_Post(self, request, *args, **kwargs):
        try:
            serializer = profileTXTPostSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = profileTXTPost.objects.get(id=pk)
            logger.info(item)
=======
class TXTPostCommentsVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TXTPostComments.objects.all()
    serializer_class = TXTPostCommentsSerializer


    def list_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            serializer = TXTPostCommentsSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_Spec_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            pk = request.query_params.get('pk')
            dbi = TXTPostComments.objects.filter(
                Q(post_id=int(pk)))
            serializer1 = TXTPostCommentsSerializer(dbi, many=True)
            return Response(serializer1.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_TXTPostComments(self, request):
        try:
            serializer = TXTPostCommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data.copy()
                list = profileTXTPost.objects.get(id=datas["post"])
                list.comments = list.comments + 1
                list.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = TXTPostComments.objects.get(id=pk)
            serializer = TXTPostCommentsSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = TXTPostComments.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_TXTPostComments(self, request, *args, **kwargs):
        try:
            serializer = TXTPostCommentsSerializerI(data=request.data)
            pk = self.kwargs['pk']
            logger.info("hi")
            item = TXTPostComments.objects.get(id=pk)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            if serializer.is_valid():
                logger.info("hi")
                serializer.update(item, serializer.data)
<<<<<<< HEAD
            else:
                return Response(serializer.errors, status=200)

            list = profileTXTPost.objects.get(id=pk)
            serializer = profileTXTPostSerializer(list)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class TXTPostCommentsVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TXTPostComments.objects.all()
    serializer_class = TXTPostCommentsSerializer


    def list_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            serializer = TXTPostCommentsSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_Spec_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            pk = request.query_params.get('pk')
            dbi = TXTPostComments.objects.filter(
                Q(post_id=int(pk)))
            serializer1 = TXTPostCommentsSerializer(dbi, many=True)
            return Response(serializer1.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_TXTPostComments(self, request):
        try:
            serializer = TXTPostCommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data.copy()
                list = profileTXTPost.objects.get(id=datas["post"])
                list.comments = list.comments + 1
                list.save()

                Bndata = {}
                list11 = App_User.objects.get(id=serializer.data['user'])
                serializerU = App_UserSerializer(list11)
                Bndata['Postuser'] = serializerU.data['id']
                Bndata['post'] = serializer.data['id']
                Bndata['PostWriter'] = list.user.id
                Bndata['comments'] = "PostCommented"
                serializerBn = TXTPostCommentsNewsFeedSerializer(data=Bndata)
                if serializerBn.is_valid():
                    serializerBn.save()
=======
                pk = self.kwargs['pk']
                list = TXTPostComments.objects.get(id=pk)
                serializer = TXTPostCommentsSerializer(list)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = TXTPostComments.objects.get(id=pk)
            serializer = TXTPostCommentsSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = TXTPostComments.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
    def update_TXTPostComments(self, request, *args, **kwargs):
        try:
            serializer = TXTPostCommentsSerializerI(data=request.data)
            pk = self.kwargs['pk']
            logger.info("hi")
            item = TXTPostComments.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = TXTPostComments.objects.get(id=pk)
                serializer = TXTPostCommentsSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765


class profileCommentVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = profileComment.objects.all()
    serializer_class = profileCommentSerializer

    def list_profileComment(self, request):
        try:
            book_list = profileComment.objects.all()
            serializer = profileCommentSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_profileComment(self, request):
        try:
            serializer = profileCommentSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profileComment(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = profileComment.objects.get(id=pk)
            serializer = profileCommentSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profileCommentbyuser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = profileComment.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = profileCommentSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_profileComment(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = profileComment.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_profileComment(self, request, *args, **kwargs):
        try:
            serializer = profileCommentSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = profileComment.objects.get(id=pk)
            logger.info('hi')
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = profileComment.objects.get(id=pk)
                serializer = profileCommentSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class TextBookVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TextBook.objects.all()
    serializer_class = TextBookSerializer

    def list_TextBook(self, request):
        try:
            book_list = TextBook.objects.all()
            serializer = TextBookSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_TextBook(self, request):
        try:
            serializer = TextBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_TextBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = TextBook.objects.get(Book=pk)
            serializer = TextBookSerializer(list)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            extracted_text=""
            f = open('home/book//Bookstagram/Bookstore/harry.txt', 'r')
            #    extracted_text = slate.PDF(f)
            datas = serializer.data.copy()
            datas['content']= str(f.read())
            return Response(datas, status=200)
<<<<<<< HEAD
=======
            # image_data = "S:/ASE/mygit/"+"\Bookstore\harry-potter-book-1.pdf"
            f = open("S:\ASE\\mygit\\Bookstagram\\Bookstore\\harry-potter-book-1.pdf", "rb")
            contents =""
            # with open("S:\ASE\\mygit\\Bookstagram\\Bookstore\\harry-potter-book-1.pdf", 'rb') as f:
            #     contents = f.read()

            pdfReader = PyPDF2.PdfFileReader(f)
            data = ""
            #
            pageObj = pdfReader.getPage(22)
            data = pageObj.extractText()
            # for i in range(1,pdfReader.numPages):
            #     pageObj = pdfReader.getPage(i)
            #     data = data + pageObj.extractText()
            # f.close()
            with open('S:\ASE\\mygit\\Bookstagram\\Bookstore\\harry.pdf', 'rb') as f:
                extracted_text = slate.PDF(f)

            return Response(extracted_text, status=200)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_TextBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = TextBook.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "TextBook deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_TextBook(self, request, *args, **kwargs):
        try:
            serializer = TextBookSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = TextBook.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = TextBook.objects.get(id=pk)
                serializer = TextBookSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class BookCommentsVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookComments.objects.all()
    serializer_class = BookCommentsSerializer

    def list_BookComments(self, request):
        try:
            book_list = BookComments.objects.all()
            serializer = BookCommentsSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_BookComments(self, request):
        try:
            serializer = BookCommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                Bndata = {}
                list = Book.objects.get(id=serializer.data['Book'])
                serializer4 = BookSerializerI(list)
                Bndata['Author'] = serializer4.data['authname']
                Bndata['Book'] = serializer.data['Book']
                Bndata['user'] = serializer.data['user']
                Bndata['Bookcomments'] = serializer.data['id']
                Bndata['comments'] = "Commented"
<<<<<<< HEAD
<<<<<<< HEAD
                logger.info("BC")
=======
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
                logger.info("BC")
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                serializerBn = CommentsNewsFeedSerializer(data=Bndata)
                if serializerBn.is_valid():
                    serializerBn.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookComments(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = BookComments.objects.get(id=pk)
            serializer = BookCommentsSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookCommentsyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookComments.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = BookCommentsSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookCommentsbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookComments.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = BookCommentsSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_BookComments(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = BookComments.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_BookComments(self, request, *args, **kwargs):
        try:
            serializer = BookCommentsSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = BookComments.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = BookComments.objects.get(id=pk)
                serializer = BookCommentsSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
=======

>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
def iterate_Treelist(tree,user,buyer,book):

    list2 = App_User.objects.get(id=user)
    serializer = App_UserSerializerII(list2)
    listB = App_User.objects.get(id=buyer)
    list1 = Book.objects.get(id=book)
    for i in tree:
<<<<<<< HEAD
        list = App_User.objects.get(username=str(i['node']).split("— ")[-1])
=======
        list = App_User.objects.get(username=str(i['node']).split(" ")[-1])
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        serializer3 = App_UserSerializerII(list)
        if serializer3.data['id'] == serializer.data['id']:
            pk = BookUserTree.objects.get(id=int(i['node'].id))
            treeobj = BookUserTree(Book=list1, user=listB, tn_parent=pk)
            treeobj.save()
            return
        iterate_Treelist(i['tree'],user,buyer,book)
    return tree

<<<<<<< HEAD
def alreadyChilden(buyer,pk):

    if pk.get_children() ==[]:
        return True
    else:
        userarr = []
        userarr = pk.get_children()
        for i in userarr:

            if (i.user.id == buyer):
                return False
    return True

def iterate_Treelist(tree,user,buyer,book):

    list2 = App_User.objects.get(id=user)
    serializer = App_UserSerializerII(list2)
    listB = App_User.objects.get(id=buyer)
    serializerBB = App_UserSerializerII(listB)
    list1 = Book.objects.get(id=book)
    for i in tree:
        list = App_User.objects.get(username=str(i['node']).split(" ")[-1])
        serializer3 = App_UserSerializerII(list)
        if serializer3.data['id'] == serializer.data['id']:
            pk = BookUserTree.objects.get(id=int(i['node'].id))
            if alreadyChilden(serializerBB.data['id'],pk):
                treeobj = BookUserTree(Book=list1, user=listB, tn_parent=pk)
                treeobj.save()
                return
        iterate_Treelist(i['tree'],user,buyer,book)
    return tree

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

class OwnBookVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OwnBook.objects.all()
    serializer_class = OwnBookSerializer

    def list_OwnBook(self, request):
        try:
            book_list = OwnBook.objects.all()
            serializer = OwnBookSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
    def Check_OwnBook(self, request):
        try:
            pk = request.query_params.get('pk')
            book = request.query_params.get('book')
            book_list = OwnBook.objects.all()
            dbi = OwnBook.objects.filter(Q(user_id=int(pk)) & Q(Book_id=int(book)) )
            response={}
            serializer4 = OwnBookSerializerI(dbi, many=True)

            if (len(serializer4.data) == 0):
                response["Own"] = False
                return Response(response, status=200)
            response["Own"] = True
            return Response(response, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    def create_OwnBook(self, request):
        try:
            serializer = OwnBookSerializer(data=request.data)
            if serializer.is_valid():
<<<<<<< HEAD

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                serializer.save()
                list = Book.objects.get(id=serializer.data['Book'])
                serializer4 = BookSerializerI(list)
                list1 = App_User.objects.get(id=serializer.data['user'])
                serializerU = App_UserSerializerII(list1)
                datas = BookTreeConnect.objects.get(Book=int(list.id))
                serializer1 = BookTreeDBSerializer(datas)
                pk = BookUserTree.objects.get(id=int(serializer1.data["Tree"]))
                if serializer.data['referrer'] == serializer4.data['authname']:
                    treeobj = BookUserTree(Book=list, user=list1, tn_parent=pk)
                    treeobj.save()
                    Bndata = {}
                    Bndata['Author'] = serializer4.data['authname']
                    Bndata['Buyer'] = serializer.data['user']
                    Bndata['Book'] = serializer.data['Book']
                    Bndata['comments'] = "Bought"
                    serializerBn = BookNewsFeedSerializer(data=Bndata)
                    if serializerBn.is_valid():
                        serializerBn.save()
                else:
                    Bndata = {}
                    Bndata['Author'] = serializer4.data['authname']
                    Bndata['Buyer'] = serializer.data['user']
                    Bndata['Book'] = serializer.data['Book']
                    Bndata['comments'] = "referred"
                    serializerBn = BookNewsFeedSerializer(data=Bndata)
                    if serializerBn.is_valid():
                        serializerBn.save()
                    iterate_Treelist(pk.get_descendants_tree(), serializer.data['referrer'], serializerU.data['id'], serializer4.data['id'])

<<<<<<< HEAD
<<<<<<< HEAD
                Tndata = {}
                Tndata['Buyer'] = serializer.data['user']
                Tndata['Author'] = serializer4.data['authname']
                Tndata['Book'] = serializer.data['Book']
                Tndata['comments'] = "Book Bought Ticker"
                serializerTn = BookTickerNewsFeedSerializer(data=Tndata)
                if serializerTn.is_valid():
                    serializerTn.save()
                
=======
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = OwnBook.objects.get(id=pk)
            serializer = OwnBookSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBookyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = OwnBook.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
            logger.info("data")
            logger.info(serializer.data)
            for i in serializer.data:
                logger.info("hi")
                logger.info(i)
                list = ""
                list = Book.objects.get(id=i['Book'])
                logger.info(list)
                serializer1 = []
                serializer1 = BookSerializer(list)
                logger.info(serializer1.data)
                i["bookJSON"] = serializer1.data
<<<<<<< HEAD
            unique = {each['Book']: each for each in serializer.data}.values()
            return Response(unique, status=200)
=======
            for i in serializer.data:
                logger.info(i['Book'])
                list = Book.objects.get(id=i['Book'])
                serializer1 = BookSerializerI(list)
                i["bookJSON"] = serializer1.data
            return Response(serializer.data, status=200)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
            return Response(serializer.data, status=200)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBookbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = OwnBook.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)
        

    def get_OwnBookbybookUser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            user = request.query_params.get('user')
            dbi = OwnBook.objects.filter(Q(Book_id=int(pk)) & Q(user_id=int(user)))
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_OwnBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = OwnBook.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book owned record deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_OwnBook(self, request, *args, **kwargs):
        try:
            serializer = OwnBookSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = OwnBook.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = OwnBook.objects.get(id=pk)
                serializer = OwnBookSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class WishlistVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookWishlist.objects.all()
    serializer_class = WishlistSerializer

    def list_Wishlist(self, request):
        try:
            book_list = BookWishlist.objects.all()
            serializer = WishlistSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_Wishlist(self, request):
        try:
            serializer = WishlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlist(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = BookWishlist.objects.get(id=pk)
            serializer = WishlistSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlistyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookWishlist.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlistbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookWishlist.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_WishlistbybookUser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            user = request.query_params.get('user')
            dbi = BookWishlist.objects.filter(Q(Book_id=int(pk)) & Q(user_id=int(user)))
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_Wishlist(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = BookWishlist.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book removed from Wishlist."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Wishlist(self, request, *args, **kwargs):
        try:
            serializer = WishlistSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = BookWishlist.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = BookWishlist.objects.get(id=pk)
                serializer = WishlistSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

<<<<<<< HEAD
@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def list_Newsfeed(request):
    try:
        arr = []
        pks = request.query_params.get('pk')
        dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends") )
        return Response(arr, status=200)

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


class NewsfeedVeiwSet(ModelViewSet):

<<<<<<< HEAD
class NewsfeedVeiwSet(ModelViewSet):
=======
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookNewsFeed.objects.all()
    serializer_class = BookNewsFeedSerializer


    def list_Feed(self, request):
        try:
            App_User_list = FriendNewsFeed.objects.all()
            serializer = FriendNewsFeedSerializer(App_User_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_UserFeed(self, request,*args, **kwargs):
        try:
            arr = []
            pks = request.query_params.get('pk')
            dbi = FriendNewsFeed.objects.filter(Q(user_id=int(pks)) | Q(friend_id=int(pks)) )
            serializer = FriendNewsFeedSerializerI(dbi, many=True)
            for i in serializer.data:
                list = FriendNewsFeed.objects.get(id=int(i["id"]))
                logger.info(list)
                serializerF = FriendNewsFeedSerializerI(list)
                datas = serializerF.data.copy()
                user = App_User.objects.get(id=datas['user'])
                serializerU = App_UserSerializerII(user)
                datas["userJSON"] = serializerU.data
                friend = App_User.objects.get(id=datas['friend'])
                serializerf = App_UserSerializerII(friend)
                datas["friendJSON"] = serializerf.data
                arr.append(datas)
            dbj = BookNewsFeed.objects.filter(Q(Author_id=int(pks)) | Q(Buyer_id=int(pks)) )
            for i in dbj:
                list = BookNewsFeed.objects.get(id=i.id)
                serializerB = BookNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Author = App_User.objects.get(id=datas['Author'])
                serializerA = App_UserSerializerII(Author)
                datas["authorJSON"] = serializerA.data
                Buyer = App_User.objects.get(id=datas['Buyer'])
                serializerBy = App_UserSerializerII(Buyer)
                datas["buyerJSON"] = serializerBy.data
                book = Book.objects.get(id=datas['Book'])
                serializerBook = BookSerializerII(book)
                datas["bookJSON"] = serializerBook.data
                arr.append(datas)
            arr2=[]
            dbk = CommentsNewsFeed.objects.filter(Q(user_id=int(pks)))
            for i in dbk:
                list = CommentsNewsFeed.objects.get(id=i.id)
                serializerB = CommentsNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Author = App_User.objects.get(id=datas['Author'])
                serializerA = App_UserSerializerII(Author)
                datas["authorJSON"] = serializerA.data
                Buyer = App_User.objects.get(id=datas['user'])
                serializerBy = App_UserSerializerII(Buyer)
                datas["user"] = serializerBy.data
                book = Book.objects.get(id=datas['Book'])
                arr2.append(datas['Book'])
                serializerBook = BookSerializerII(book)
                datas["bookJSON"] = serializerBook.data
                bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                serializerBookcom = BookCommentsSerializerI(bookcom)
                datas["BookcommentsJSON"] = serializerBookcom.data
                arr.append(datas)

            Comments_list = CommentsNewsFeed.objects.all()
            serializerCC = CommentsNewsFeedSerializerI(Comments_list, many=True)
            datasCC = serializerCC.data.copy()

            for i in datasCC:

                if i["Author"] == int(pks):
                    logger.info("hi")
                    list = CommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = CommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Author = App_User.objects.get(id=datas['Author'])
                    serializerA = App_UserSerializerII(Author)
                    datas["authorJSON"] = serializerA.data
                    Buyer = App_User.objects.get(id=datas['user'])
                    serializerBy = App_UserSerializerII(Buyer)
                    datas["user"] = serializerBy.data
                    book = Book.objects.get(id=datas['Book'])
                    serializerBook = BookSerializerII(book)
                    datas["bookJSON"] = serializerBook.data
                    bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                    serializerBookcom = BookCommentsSerializerI(bookcom)
                    datas["BookcommentsJSON"] = serializerBookcom.data
                    arr.append(datas)
                if i["Book"] in arr2:
                    list = CommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = CommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Author = App_User.objects.get(id=datas['Author'])
                    serializerA = App_UserSerializerII(Author)
                    datas["authorJSON"] = serializerA.data
                    Buyer = App_User.objects.get(id=datas['user'])
                    serializerBy = App_UserSerializerII(Buyer)
                    datas["user"] = serializerBy.data
                    book = Book.objects.get(id=datas['Book'])
                    serializerBook = BookSerializerII(book)
                    datas["bookJSON"] = serializerBook.data
                    bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                    serializerBookcom = BookCommentsSerializerI(bookcom)
                    datas["BookcommentsJSON"] = serializerBookcom.data
                    arr.append(datas)





            # serializer1 = BookNewsFeedSerializerI(dbj, many=True)

            # arr.append(serializer.data)
            # arr.append(serializer1.data)
            arr = sorted(arr, key=lambda k: k['publist'])
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1

=======

class NewsfeedVeiwSet(ModelViewSet):

>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookNewsFeed.objects.all()
    serializer_class = BookNewsFeedSerializer


    def list_Feed(self, request):
        try:
            App_User_list = FriendNewsFeed.objects.all()
            serializer = FriendNewsFeedSerializer(App_User_list, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_UserFeed(self, request,*args, **kwargs):
        try:
            arr = []
            pks = request.query_params.get('pk')
            dbi = FriendNewsFeed.objects.filter(Q(user_id=int(pks)) | Q(friend_id=int(pks)) )
            serializer = FriendNewsFeedSerializerI(dbi, many=True)
            for i in serializer.data:
                list = FriendNewsFeed.objects.get(id=int(i["id"]))
                serializerF = FriendNewsFeedSerializerI(list)
                datas = serializerF.data.copy()
                user = App_User.objects.get(id=datas['user'])
                serializerU = App_UserSerializerII(user)
                datas['notify_type']="Friendship Notification"
                datas["userJSON"] = serializerU.data
                friend = App_User.objects.get(id=datas['friend'])
                serializerf = App_UserSerializerII(friend)
                datas["friendJSON"] = serializerf.data
                arr.append(datas)
            dbj = BookNewsFeed.objects.filter(Q(Author_id=int(pks)) | Q(Buyer_id=int(pks)) )
            for i in dbj:
                list = BookNewsFeed.objects.get(id=i.id)
                serializerB = BookNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Author = App_User.objects.get(id=datas['Author'])
                serializerA = App_UserSerializerII(Author)
                datas['notify_type'] = "Book Notification"
                datas["authorJSON"] = serializerA.data
                Buyer = App_User.objects.get(id=datas['Buyer'])
                serializerBy = App_UserSerializerII(Buyer)
                datas["buyerJSON"] = serializerBy.data
                book = Book.objects.get(id=datas['Book'])
                serializerBook = BookSerializerII(book)
                datas["bookJSON"] = serializerBook.data
                arr.append(datas)
            
            arr2=[]
            dbk = CommentsNewsFeed.objects.filter(Q(user_id=int(pks)))
            for i in dbk:
                list = CommentsNewsFeed.objects.get(id=i.id)
                serializerB = CommentsNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Author = App_User.objects.get(id=datas['Author'])
                serializerA = App_UserSerializerII(Author)
                datas["authorJSON"] = serializerA.data
                Buyer = App_User.objects.get(id=datas['user'])
                serializerBy = App_UserSerializerII(Buyer)
                datas["userJSON"] = serializerBy.data
                datas['notify_type']="BookComment Notification"
                book = Book.objects.get(id=datas['Book'])
                arr2.append(datas['Book'])
                serializerBook = BookSerializerII(book)
                datas["bookJSON"] = serializerBook.data
                bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                serializerBookcom = BookCommentsSerializerI(bookcom)
                datas["BookcommentsJSON"] = serializerBookcom.data
                arr.append(datas)

            Comments_list = CommentsNewsFeed.objects.all()
            serializerCC = CommentsNewsFeedSerializerI(Comments_list, many=True)
            datasCC = serializerCC.data.copy()

            for i in datasCC:

                if i["Author"] == int(pks):
                    list = CommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = CommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Author = App_User.objects.get(id=datas['Author'])
                    serializerA = App_UserSerializerII(Author)
                    datas["authorJSON"] = serializerA.data
                    Buyer = App_User.objects.get(id=datas['user'])
                    serializerBy = App_UserSerializerII(Buyer)
                    datas["userJSON"] = serializerBy.data
                    datas['notify_type']="BookComment Notification"
                    book = Book.objects.get(id=datas['Book'])
                    serializerBook = BookSerializerII(book)
                    datas["bookJSON"] = serializerBook.data
                    bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                    serializerBookcom = BookCommentsSerializerI(bookcom)
                    datas["BookcommentsJSON"] = serializerBookcom.data
                    arr.append(datas)

                if i["Book"] in arr2:
                    list = CommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = CommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Author = App_User.objects.get(id=datas['Author'])
                    serializerA = App_UserSerializerII(Author)
                    datas["authorJSON"] = serializerA.data
                    Buyer = App_User.objects.get(id=datas['user'])
                    serializerBy = App_UserSerializerII(Buyer)
                    datas["userJSON"] = serializerBy.data
                    datas['notify_type']="BookComment Notification"
                    book = Book.objects.get(id=datas['Book'])
                    serializerBook = BookSerializerII(book)
                    datas["bookJSON"] = serializerBook.data
                    bookcom = BookComments.objects.get(id=datas['Bookcomments'])
                    serializerBookcom = BookCommentsSerializerI(bookcom)
                    datas["BookcommentsJSON"] = serializerBookcom.data
                    arr.append(datas)
<<<<<<< HEAD

            dbl = TXTPostCommentsNewsFeed.objects.filter(Q(PostWriter_id=int(pks)))
            for i in dbl:
                list = TXTPostCommentsNewsFeed.objects.get(id=i.id)
                serializerB = TXTPostCommentsNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Postuser = App_User.objects.get(id=datas['Postuser'])
                serializerA = App_UserSerializerII(Postuser)
                datas["PostuserJSON"] = serializerA.data
                PostWriter = App_User.objects.get(id=datas['PostWriter'])
                serializerBy = App_UserSerializerII(PostWriter)
                datas["PostWriterJSON"] = serializerBy.data
                datas['notify_type']="PostComment Notification"
                post = profileTXTPost.objects.get(id=datas['post'])
                arr2.append(datas['post'])
                serializerBook = profileTXTPostSerializer(post)
                datas["post"] = serializerBook.data
                arr.append(datas)

            Comments_list = TXTPostCommentsNewsFeed.objects.all()
            serializerCC = TXTPostCommentsNewsFeedSerializerI(Comments_list, many=True)
            datasCC = serializerCC.data.copy()
            for i in datasCC:
                if i["Postuser"] == int(pks):
                    list = TXTPostCommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = TXTPostCommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Postuser = App_User.objects.get(id=datas['Postuser'])
                    serializerA = App_UserSerializerII(Postuser)
                    datas["PostuserJSON"] = serializerA.data
                    PostWriter = App_User.objects.get(id=datas['PostWriter'])
                    serializerBy = App_UserSerializerII(PostWriter)
                    datas["PostWriterJSON"] = serializerBy.data
                    post = profileTXTPost.objects.get(id=datas['post'])
                    arr2.append(datas['post'])
                    datas['notify_type']="PostComment Notification"
                    serializerBook = profileTXTPostSerializer(post)
                    datas["post"] = serializerBook.data
                    arr.append(datas)
                if i["post"] in arr2:
                    list = TXTPostCommentsNewsFeed.objects.get(id=int(i["id"]))
                    serializerB = TXTPostCommentsNewsFeedSerializerI(list)
                    datas = serializerB.data.copy()
                    Postuser = App_User.objects.get(id=datas['Postuser'])
                    serializerA = App_UserSerializerII(Postuser)
                    datas["PostuserJSON"] = serializerA.data
                    PostWriter = App_User.objects.get(id=datas['PostWriter'])
                    serializerBy = App_UserSerializerII(PostWriter)
                    datas["PostWriterJSON"] = serializerBy.data
                    post = profileTXTPost.objects.get(id=datas['post'])
                    arr2.append(datas['post'])
                    datas['notify_type']="PostComment Notification"
                    serializerBook = profileTXTPostSerializer(post)
                    datas["post"] = serializerBook.data
                    arr.append(datas)

            TickerNewsFeed_list = BookTickerNewsFeed.objects.all()
            serializerTT = BookTickerNewsFeedSerializerI(TickerNewsFeed_list, many=True)
            datasTT = serializerTT.data.copy()
            logger.info(datasTT)
            for i in datasTT:

                logger.info("hi")
                list = BookTickerNewsFeed.objects.get(id=int(i["id"]))
                logger.info(list)
                serializerB = BookTickerNewsFeedSerializerI(list)
                datas = serializerB.data.copy()
                Author = App_User.objects.get(id=datas['Author'])
                serializerA = App_UserSerializerII(Author)
                datas["authorJSON"] = serializerA.data
                Buyer = App_User.objects.get(id=datas['Buyer'])
                serializerBy = App_UserSerializerII(Buyer)
                datas["buyerJSON"] = serializerBy.data
                datas['notify_type']="Ticker Notification"
                book = Book.objects.get(id=datas['Book'])
                serializerBook = BookSerializerII(book)
                datas["bookJSON"] = serializerBook.data
                arr.append(datas)


            arr = sorted(arr, key=lambda k: k['publist'])
            arr.reverse()
            return Response(Reverse(arr),status=200)
=======
            arr = sorted(arr, key=lambda k: k['publist'])
            return Response(arr, status=200)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


<<<<<<< HEAD
def Reverse(lst):
    return [ele for ele in reversed(lst)]

@api_view(['POST'])
@permission_classes((AllowAny, ))
def Bookstagram_keepAlive(request):
    try:
        response = {}
        response["status"] = "I'm Inevitable"
        return Response(response, status=200)

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def Bookstagram_DBdump(request):
    try:
        response = {}
        response["status"] = "I'm Inevitable"
        file_dir = settings.DBBACKUP_STORAGE_OPTIONS["location"]
        file_list = os.listdir(file_dir)
        cont = ""
        with open( settings.DBBACKUP_STORAGE_OPTIONS["location"] + file_list[0]  , "rb") as image_file:
            cont = base64.b64encode(image_file.read())
        return Response(cont, status=200)
                                                
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)
=======





>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765










