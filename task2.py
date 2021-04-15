

class EventBus:
    def __init__(self):
        self.event_x_subscribers = dict()

    def subscribe(self, subscriber, event):
        self.event_x_subscribers.setdefault(event, set())
        self.event_x_subscribers[event].add(subscriber)

    def unsubscribe(self, subscriber, event):
        if event in self.event_x_subscribers:
            if subscriber in self.event_x_subscribers[event]:
                self.event_x_subscribers[event].remove(subscriber)
            else:
                raise Exception(f"Object {subscriber} is not subscribed to this event")
        else:
            raise Exception(f"Event {event} doesn't exist")

    def emit_event(self, event, data=None):
        print(f'Event {event} emitted by {id(self)}')
        if event in self.event_x_subscribers:
            for subscriber in self.event_x_subscribers[event]:
                subscriber(data)


def event_bus_destroyer(event_bus):
    def f(data):
        event_bus.emit_event(data, data)
    return f


eb = EventBus()
eb.subscribe(event_bus_destroyer(eb), 'some_event')
eb.emit_event('some_event', 'some_event')  # Oops!
# l1 = lambda x: print('call_1', x)
# l2 = lambda x: print('call_2', x)
# eb = EventBus()
# eb.subscribe(l1, 'first')
# eb.subscribe(l2, 'second')
# eb.subscribe(l1, 'third')
# eb.subscribe(l2, 'third')
# eb.emit_event('first', '1')
# eb.emit_event('second', '2')
# eb.emit_event('third', '3')
