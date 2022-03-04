from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket Connected..")

    def websocket_receive(self, event):
        print("Message received")

    def websocket_disconnect(self, event):
        print("Websocket disconnected..")

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket Connected..")

    async def websocket_receive(self, event):
        print("Message received")

    async def websocket_disconnect(self, event):
        print("Websocket disconnected..")