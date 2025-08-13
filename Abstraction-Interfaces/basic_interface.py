from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass
    
class Document(Printable):
    def print(self):
        return "\nPrinting Document...\n"
    
class Photo(Printable):
    def print(self):
        return "\nPrinting Photo...\n"

doc = Document()
photo = Photo()

print("-" * 20)
print(doc.print())
print("-" * 20)
print(photo.print())
print("-" * 20)