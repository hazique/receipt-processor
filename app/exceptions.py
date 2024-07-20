from abc import ABC, abstractmethod

class ReceiptProcessorException(Exception, ABC):
    """
    Base class for all application errors.

    Each custom exception should be derived from this class.
    """
    @abstractmethod
    def serialize(self):
        pass
    

class InvalidReceiptException(ReceiptProcessorException):

    def serialize(self):
        return {"description": "The receipt is invalid"}, 400
    

class InvalidReceiptIdException(ReceiptProcessorException):

    def serialize(self):
        return {"description": "No receipt found for that id"}, 404
