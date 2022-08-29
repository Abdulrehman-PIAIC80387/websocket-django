from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Connected",event)
        self.send({


            'type':'websocket.accept'
        })


    def websocket_receive(self, event):
        print("message received",event)
        self.send({

            'type':'websocket.send',
             'text':'Message sent to clinet'
        })


    def websocket_disconnect(self,event):
        print("disconnected",event)
        raise StopConsumer()