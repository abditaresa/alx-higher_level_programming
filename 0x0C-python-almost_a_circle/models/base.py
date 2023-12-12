class Base:
    def __init__(self, id=None):
        self.id = id if id is not None else self.id_gen()

    @staticmethod
    def id_gen():
        if not hasattr(Base.id_gen, 'counter'):
            Base.id_gen.counter = 0
        Base.id_gen.counter += 1
        return Base.id_gen.counter
