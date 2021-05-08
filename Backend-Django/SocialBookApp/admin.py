'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

<<<<<<< HEAD

<<<<<<< HEAD
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed,profileTXTPost,TXTPostComments,TXTPostCommentsNewsFeed,BookTickerNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment)
=======
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeDB,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment,profileTXTPost,TXTPostComments)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment,profileTXTPost,TXTPostComments)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765

admin.site.register(Book)
admin.site.register(TextBook)
admin.site.register(BookComments)
admin.site.register(OwnBook)
admin.site.register(App_User)
admin.site.register(friendlist)
admin.site.register(profileComment)
admin.site.register(profileTXTPost)
admin.site.register(TXTPostComments)
<<<<<<< HEAD
<<<<<<< HEAD
admin.site.register(BookWishlist)
=======
admin.site.register(BookTreeDB)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
admin.site.register(BookWishlist)
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
admin.site.register(BookTreeConnect)
admin.site.register(BookNewsFeed)
admin.site.register(FriendNewsFeed)
admin.site.register(CommentsNewsFeed)
<<<<<<< HEAD
<<<<<<< HEAD
admin.site.register(BookUserTree)
admin.site.register(TXTPostCommentsNewsFeed)
admin.site.register(BookTickerNewsFeed)

=======
class BookUserTreeAdmin(TreeNodeModelAdmin):

    # set the changelist display mode: 'accordion', 'breadcrumbs' or 'indentation' (default)
    # when changelist results are filtered by a querystring,
    # 'breadcrumbs' mode will be used (to preserve data display integrity)
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    # use TreeNodeForm to automatically exclude invalid parent choices
    form = TreeNodeForm

admin.site.register(BookUserTree, BookUserTreeAdmin)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======
admin.site.register(BookUserTree)


>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
