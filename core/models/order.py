from typing import TYPE_CHECKING
from datetime import datetime, timezone
from .base import Base
from .order_product_association import OrderProductAssociation
from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .product import Product


def aware_utcnow():
    return datetime.now(timezone.utc)


class Order(Base):
    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        default=aware_utcnow,
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_association",
        back_populates="orders",
    )
