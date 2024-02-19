from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class MovieEmitter:
    def emit(self, movie_data):
        async_to_sync(get_channel_layer().group_send)(
            "movies_consumer",
            {"type": "send.all", "event": movie_data},
        )
