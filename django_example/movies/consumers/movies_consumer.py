import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class MoviesConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("movies_consumer", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("movies_consumer", self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    def send_all(self, event):
        self.send(text_data=json.dumps(event["event"]))
