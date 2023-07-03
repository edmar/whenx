import uuid
from sqlalchemy import Column, String
from whenx.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
