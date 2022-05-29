
class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = cls.__new__(cls)

        return cls._instance

    def my_method(self):
        print("My method")


# Só conseguimos acessar o metodo My_Method de chamarmos Logger.instance()
# Caso contrário, teremos um runtime error

# Isso nos garante que só existe uma instancia de _instance em todo o programa



