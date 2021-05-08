'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.conf.urls import url

<<<<<<< HEAD
<<<<<<< HEAD
from SocialBookApp.views.views import (BookVeiwSet,UserVeiwSet,activate_User,create_User,friendlistVeiwSet,profileTXTPostVeiwSet,TXTPostCommentsVeiwSet,profileCommentVeiwSet,TextBookVeiwSet,BookCommentsVeiwSet,OwnBookVeiwSet,WishlistVeiwSet,activate_Tree,WishlistVeiwSet,NewsfeedVeiwSet,Bookstagram_keepAlive,Bookstagram_DBdump  )
=======
from SocialBookApp.views.views import (BookVeiwSet,UserVeiwSet,activate_User,create_User,friendlistVeiwSet,profileTXTPostVeiwSet,TXTPostCommentsVeiwSet,profileCommentVeiwSet,TextBookVeiwSet,BookCommentsVeiwSet,OwnBookVeiwSet,WishlistVeiwSet,activate_Tree,WishlistVeiwSet,NewsfeedVeiwSet  )
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
from SocialBookApp.views.process import (LoginCheckSet)
=======
from SocialBookApp.views.views import (activate_Tree,BookVeiwSet,UserVeiwSet,activate_User,create_User,friendlistVeiwSet,profileTXTPostVeiwSet,TXTPostCommentsVeiwSet,profileCommentVeiwSet,TextBookVeiwSet,BookCommentsVeiwSet,OwnBookVeiwSet,WishlistVeiwSet,NewsfeedVeiwSet  )
from SocialBookApp.views.process import (LoginCheckSet,create_Dp)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1



book = BookVeiwSet.as_view({
    'get' : 'list_Book',
    'post' : 'create_Book',
})

book_id = BookVeiwSet.as_view({
    'get' : 'get_Book',
    'put': 'update_Book',
    'delete': 'delete_Book'
})

user = UserVeiwSet.as_view({
    'get' : 'list_User',

})

user_id = UserVeiwSet.as_view({
    'get' : 'get_User',
    'put': 'update_User',
    'delete': 'delete_User'
})

friend = friendlistVeiwSet.as_view({
    'post' : 'create_relationship',
<<<<<<< HEAD
<<<<<<< HEAD
     
=======

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
     
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
})

friend_user_id = friendlistVeiwSet.as_view({

<<<<<<< HEAD
<<<<<<< HEAD
         'get' : 'get_allUsers'
=======
     'get' : 'get_allUsers'
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
         'get' : 'get_allUsers'
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
})

friendprofile = friendlistVeiwSet.as_view({

     'get' : 'get_profile'
})

friendtype = friendlistVeiwSet.as_view({

     'get' : 'get_allUserstype'
})

friend_id = friendlistVeiwSet.as_view({
    'put' : 'update_relationship',
                        #change friendship status
<<<<<<< HEAD
    
})

friend_ids = friendlistVeiwSet.as_view({
    
                                #change friendship status
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    'get' : 'get_friendlist'
})

notfriend_id = friendlistVeiwSet.as_view({

    'get' : 'get_notfriendlist'
                         #pending friend request sent by user
})

addfriend_id = friendlistVeiwSet.as_view({

    'get': 'get_acceptfriendlist'
})
                            #pending request to accept friend
unfriend_id = friendlistVeiwSet.as_view({

    'get': 'Unfriend'
})

listfriend_id = friendlistVeiwSet.as_view({

    'get': 'list_friendlist'
})

login = LoginCheckSet.as_view({
    'post' : 'login',

})

<<<<<<< HEAD

chpass = LoginCheckSet.as_view({
        'post' : 'change_pass',

        })

genpass = LoginCheckSet.as_view({
        'post' : 'generate_pass',

        })


=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
txtpost = profileTXTPostVeiwSet.as_view({

    'post' : 'create_profileTXTPost',

})

txtpostchange = profileTXTPostVeiwSet.as_view({

    'put': 'update_Post',
    'delete': 'delete_Post',

})

txtpostbyuser = profileTXTPostVeiwSet.as_view({

    'get': 'list_profile_post',
})

<<<<<<< HEAD
uplike = profileTXTPostVeiwSet.as_view({

        'get': 'update_Like',
        })

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
txtposthomuser = profileTXTPostVeiwSet.as_view({

    'get': 'list_home_post',
})

postcomment_id = TXTPostCommentsVeiwSet.as_view({
    'get' : 'get_TXTPostComments',
    'put': 'update_TXTPostComments',
    'delete': 'delete_TXTPostComments'
})

postcomment = TXTPostCommentsVeiwSet.as_view({
    'get' : 'list_TXTPostComments',
    'post' : 'create_TXTPostComments',

})

postcommentspecific = TXTPostCommentsVeiwSet.as_view({
    'get' : 'list_Spec_TXTPostComments',


})

profcomment = profileCommentVeiwSet.as_view({
    'get' : 'list_profileComment',
    'post' : 'create_profileComment',
})

profcomment_id = profileCommentVeiwSet.as_view({
    'get' : 'get_profileComment',
    'put': 'update_profileComment',
    'delete': 'delete_profileComment'
})

profcommentusr_id = profileCommentVeiwSet.as_view({
    'get' : 'get_profileCommentbyuser',

})

TextBook = TextBookVeiwSet.as_view({
    'get' : 'list_TextBook',
    'post' : 'create_TextBook',
})

TextBook_id = TextBookVeiwSet.as_view({
    'get' : 'get_TextBook',
    'put': 'update_TextBook',
    'delete': 'delete_TextBook'
})

TextBookusr_id = TextBookVeiwSet.as_view({
    'get' : 'get_TextBookyou',

})

BookComments = BookCommentsVeiwSet.as_view({
    'get' : 'list_BookComments',
    'post' : 'create_BookComments',
})

BookComments_id = BookCommentsVeiwSet.as_view({
    'get' : 'get_BookComments',
    'put': 'update_BookComments',
    'delete': 'delete_BookComments'
})

BookCommentsbok_id = BookCommentsVeiwSet.as_view({
    'get' : 'get_BookCommentsbybook',

})

OwnBookbok_id = OwnBookVeiwSet.as_view({
    'get' : 'get_OwnBookbybook',

})

OwnBook = OwnBookVeiwSet.as_view({
    'get' : 'list_OwnBook',
    'post' : 'create_OwnBook',
})

OwnBook_id = OwnBookVeiwSet.as_view({
    'get' : 'get_OwnBook',
    'put': 'update_OwnBook',
    'delete': 'delete_OwnBook'
})

OwnBookusr_id = OwnBookVeiwSet.as_view({
    'get' : 'get_OwnBookyou',

})

OwnBookbok_id = OwnBookVeiwSet.as_view({
    'get' : 'get_OwnBookbybook',

})

OwnBookusrbok_id = OwnBookVeiwSet.as_view({
    'get' : 'get_OwnBookbybookUser',

})

<<<<<<< HEAD
OwnBook_check = OwnBookVeiwSet.as_view({
        'get' : 'Check_OwnBook',

})

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
Wishlist = WishlistVeiwSet.as_view({
    'get' : 'list_Wishlist',
    'post' : 'create_Wishlist',
})

Wishlist_id = WishlistVeiwSet.as_view({
    'get' : 'get_Wishlist',
    'put': 'update_Wishlist',
    'delete': 'delete_Wishlist'
})

Wishlistusr_id = WishlistVeiwSet.as_view({
    'get' : 'get_Wishlistyou',

})

Wishlistbok_id = WishlistVeiwSet.as_view({
    'get' : 'get_Wishlistbybook',

})

Wishlistusrbok_id = WishlistVeiwSet.as_view({
    'get' : 'get_WishlistbybookUser',

})

feed = NewsfeedVeiwSet.as_view({
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        'get' : 'list_Feed',
            # 'post' : 'create_Book',
})

feed_id = NewsfeedVeiwSet.as_view({
        'get' : 'get_UserFeed',
            # 'post' : 'create_Book',
})
<<<<<<< HEAD
=======
    'get' : 'list_Feed',
    # 'post' : 'create_Book',
})

feed_id = NewsfeedVeiwSet.as_view({
    'get' : 'get_UserFeed',
    # 'post' : 'create_Book',
})

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765


urlpatterns = [
    url(r'^book/$', book),
    url(r'^book/(?P<pk>\d+)/$', book_id),

    url(r'^book/login/$', login),

<<<<<<< HEAD
<<<<<<< HEAD
    url(r'^chpass/$', chpass),
    url(r'^genpass/$', genpass),
=======
    url(r'^dp/$', create_Dp),
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    url(r'^user/$', user),
    url(r'^user/(?P<pk>\d+)/$', user_id),

    url(r'^activate_user/$', activate_User),
    url(r'^create_user/$', create_User),

<<<<<<< HEAD
    url(r'^activate_Tree/$', activate_Tree),

    url(r'^friend/$', friend),
    url(r'^allfriend/$', friend_user_id),
<<<<<<< HEAD
    url(r'^friendupdate/$', friend_id),
    url(r'^friendlist/(?P<pk>\d+)/$', friend_ids),
=======
    url(r'^friendlist/(?P<pk>\d+)/$', friend_id),
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
    url(r'^notfriend/(?P<pk>\d+)/$', notfriend_id),
    url(r'^acceptfriend/(?P<pk>\d+)/$', addfriend_id),
    url(r'^unfriend/$', unfriend_id),
=======
    url(r'^friend/$', friend),
    url(r'^allfriend/$', friend_user_id),
    url(r'^friendlist/(?P<pk>\d+)/$', friend_id),
    url(r'^notfriend/(?P<pk>\d+)/$', notfriend_id),
    url(r'^acceptfriend/(?P<pk>\d+)/$', addfriend_id),
    url(r'^unfriend/(?P<pk>\d+)/$', unfriend_id),
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    url(r'^listfriend/$', listfriend_id),
    url(r'^usertype/$', friendtype),
    url(r'^profile/$', friendprofile),

    url(r'^txtpost/$', txtpost),
    url(r'^txtpostchange/(?P<pk>\d+)/$', txtpostchange),
    url(r'^txtpostbyuser/$', txtpostbyuser),
    url(r'^txtposthomuser/$', txtposthomuser),
<<<<<<< HEAD
    url(r'^uplike/$', uplike),
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

    url(r'^postcomment/$', postcomment),
    url(r'^postspeccomment/$', postcommentspecific),
    url(r'^postcomment/(?P<pk>\d+)/$', postcomment_id),

    url(r'^profcomment/$', profcomment),
    url(r'^profcomment/(?P<pk>\d+)/$', profcomment_id),
    url(r'^profcommentusr/$', profcommentusr_id),

    url(r'^textbook/$', TextBook),
    url(r'^textbook/(?P<pk>\d+)/$', TextBook_id),
    url(r'^textbookusr/$', TextBookusr_id),

    url(r'^ownbook/$', OwnBook),
    url(r'^ownbook/(?P<pk>\d+)/$', OwnBook_id),
    url(r'^ownbookusr/$', OwnBookusr_id),
    url(r'^ownbookbok/$', OwnBookbok_id),
    url(r'^ownbookusrbok/$', OwnBookusrbok_id),
<<<<<<< HEAD
    url(r'^ownbookcheck/$', OwnBook_check),
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

    url(r'^bookcomments/$', BookComments),
    url(r'^bookcomments/(?P<pk>\d+)/$', BookComments_id),
    url(r'^bookcommentssbok/$', BookCommentsbok_id),

    url(r'^wishlist/$', Wishlist),
    url(r'^wishlist/(?P<pk>\d+)/$', Wishlist_id),
    url(r'^wishlistusr/$', Wishlistusr_id),
    url(r'^wishlistbok/$', Wishlistbok_id),
    url(r'^wishlistusrbok/$', Wishlistusrbok_id),

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
    url(r'^activate_Tree/$', activate_Tree),
    url(r'^feed/$', feed),
    url(r'^userfeed/$', feed_id),

<<<<<<< HEAD
    url(r'^keepalive/$',Bookstagram_keepAlive ),
    url(r'^dbdump/$', Bookstagram_DBdump),
=======
    url(r'^feed/$', feed),
    url(r'^userfeed/$', feed_id),
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1

=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
]
