from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship


if TYPE_CHECKING:
    from .order import Order


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_association",
        back_populates="products",
    )
