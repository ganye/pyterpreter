
class BaseCommand:
    @staticmethod
    def callback(*args):
        raise NotImplementedError()

    @staticmethod
    def help(*args):
        raise NotImplementedError()
