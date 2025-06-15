from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), nullable=False, unique=True, index=True
    )

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
