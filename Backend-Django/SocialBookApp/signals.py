from SocialBookApp.models.bookmodels import (BookTickerNewsFeed)
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=BookTickerNewsFeed)
def announce_new_ticker(sender,instance,created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
                
                "gossip", {
                    "type": "ticker.gossip",
                    "event": "New Ticker",
                    "TickerJSON": instance.comments
                    }
                
                )
