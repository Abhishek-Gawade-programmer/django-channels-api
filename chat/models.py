from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# create 3 models with name and type
class IOT(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "global_notifcation_group",
            {
                "command": "iot_number1",
                "type": "send_notification",
                "value": {"name": self.name, "type": self.type},
            },
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IOT1(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "global_notifcation_group",
            {
                "command": "iot_number2",
                "type": "send_notification",
                "value": {"name": self.name, "type": self.type},
            },
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IOT2(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "global_notifcation_group",
            {
                "command": "iot_number3",
                "type": "send_notification",
                "value": {"name": self.name, "type": self.type},
            },
        )
        super().save(*args, **kwargs)
