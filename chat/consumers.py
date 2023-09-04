import json

from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        if self.scope["url_route"]["kwargs"]["room_name"] == "global":
            print("we are connected as a global")
            self.room_name = "global_notifcation"
            self.room_group_name = "global_notifcation_group"
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name,
            )
            self.send(text_data=json.dumps({"START GLOBAL": "we as a GOBAL"}))

        self.send(text_data=json.dumps({"START GLOBAL": "we as a GOBAL"}))

    def disconnect(self, close_code):
        # Unsubscribe the client from the group when they disconnect
        self.channel_layer.group_discard(
            "global_notifcation_group", "global_notifcation_group"
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

    def send_data(self, event):
        data = event["data"]
        self.send(json.dumps(data))

    def send_notification(self, event):
        self.send(text_data=json.dumps(event))
