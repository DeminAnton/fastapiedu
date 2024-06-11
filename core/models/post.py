from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    # _user_id_unique: bool = False
    # _user_id_nullable: bool = False
    _user_back_populates: str | None = "posts"

    title: Mapped[str] = mapped_column(String(64))
    body: Mapped[str] = mapped_column(Text, default="", server_default="")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)
