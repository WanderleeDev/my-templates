from typing import Optional
from fastapi import status


class AppException(Exception):
    """Base exception for all application exceptions"""

    def __init__(
        self,
        message: str = "Unknown error, please try again later",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundResourceException(AppException):
    """Exception raised when a resource is not found"""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=status.HTTP_404_NOT_FOUND)


class UpdateResourceException(AppException):
    """Exception raised when a resource couldn't be updated"""

    def __init__(self, message: str = "The resource couldn't be updated"):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST)


class DeleteResourceException(AppException):
    """Exception raised when a resource couldn't be deleted"""

    def __init__(self, message: str = "The resource couldn't be deleted"):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST)


class CreateResourceException(AppException):
    """Exception raised when a resource couldn't be created"""

    def __init__(self, message: str = "The resource couldn't be created"):
        super().__init__(message)


class ResourceAlreadyExistsException(AppException):
    """Exception raised when a resource already exists"""

    def __init__(self, message: Optional[str] = None):
        super().__init__(
            message=f"The resource already exists{': ' + message if message else ''}", 
            status_code=status.HTTP_409_CONFLICT
        )
