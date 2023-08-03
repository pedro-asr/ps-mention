from sqlalchemy import Column, Integer, String, Boolean

from db.base_class import Base


class To_do(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    