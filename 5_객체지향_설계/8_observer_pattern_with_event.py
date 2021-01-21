class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self, events):
        self.subcribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subcribers[event]

    def register(self, event, who, callback = None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

if __name__ == "__main__":
    pub = Publisher(["점심", "퇴근"])

    astin = Subscriber("아스틴")
    james = Subscriber("제임스")
    jeff = Subscriber("제프")
    
    pub.register("점심", astin)
    pub.register("퇴근", astin)
    pub.register("퇴근", james)
    pub.register("점심", jeff)

    pub.dispatch("점심", "점심시간입니다.")
    pub.dispatch("퇴근", "퇴근시간입니다.")