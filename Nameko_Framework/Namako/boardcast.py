from nameko.events import BROADCAST, event_handler


class Service:
    name = "ListenerService"

    @event_handler(
        "monitor", "ping", handler_type=BROADCAST, reliable_delivery=False
    )
    def ping(self, payload):
        # all running services will respond
        print("pong from {}".format(self.name))
