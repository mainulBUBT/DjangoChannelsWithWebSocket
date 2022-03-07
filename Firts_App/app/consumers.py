from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket Connected..", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received",event)

    def websocket_disconnect(self, event):
        print("Websocket disconnected..", event)

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket Connected..", event)

    async def websocket_receive(self, event):
        print("Message received", event)

    async def websocket_disconnect(self, event):
        print("Websocket disconnected..", event)