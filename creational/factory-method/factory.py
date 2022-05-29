
from abc import ABC, abstractclassmethod



class Creator(ABC):

    @abstractclassmethod
    def factory_method(self):
        ...

    def some_operation(self):
        product = self.factory_method()

        result = f"Creator has created {product}"

        return result

class MyConcreteCreator(Creator):

    def factory_method(self):
        product = MyConcreteProduct()
        return product

class MyOtherConcreteCreator(Creator):

    def factory_method(self):
        product = MyOtherConcreteProduct()
        return product

class Product(ABC):

    @abstractclassmethod
    def operation(self):
        ...

class MyConcreteProduct(Product):

    def operation(self):
        return "My concrete product"

class MyOtherConcreteProduct(Product):

    def operation(self):
        return "My Other concrete product"


def client_code(creator: Creator) -> None:
    print(f"Calling creator {creator.__class__}")
    print(f"Operation {creator.some_operation()}")

if __name__ == "__main__":

    creator = MyConcreteCreator()
    client_code(creator)

    othercreator = MyOtherConcreteCreator()
    client_code(othercreator)

