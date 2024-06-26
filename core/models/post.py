from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Post(UserRelationMixin, Base):
    # _user_id_unique: bool = False
    # _user_id_nullable: bool = False
    _user_back_populates: str|None = "posts"
     
    title: Mapped[str] = mapped_column(String(64))
    body: Mapped[str] = mapped_column(Text, default="", server_default="")