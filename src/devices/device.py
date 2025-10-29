from abc import ABC, abstractmethod

class Device(ABC):
    
    def __init__(self, id: str):
        self.id = id
        
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def init(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def __enter__():
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass