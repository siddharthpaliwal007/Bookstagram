import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NewBookTicker(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip",self.channel_name)

    async def connect(self):
                
        await self.channel_layer.group_dicard("gossip",self.channel_name)

    async def ticker_gossip(self, event):

        await self.send_json(event)

