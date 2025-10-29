from abc import ABC, abstractmethod

class Device(ABC):
    
    def __init__(self, id: str):
        self.id = id
        
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
