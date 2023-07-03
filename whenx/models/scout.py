from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, ForeignKey
from whenx.database import Base
import uuid
from sqlalchemy.sql import func
from whenx.database import db
from whenx.services import create_react_agent


class Scout(Base):
    __tablename__ = "scouts"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    instruction = Column(String)
    teamId = Column(String, ForeignKey("teams.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    team = relationship('Team', back_populates='scouts')

    observations = relationship('Observation', back_populates='scout', cascade='all, delete-orphan')

    def run(self):
        agent = create_react_agent()
        result = agent.run(self.instruction)
        observation = Observation(instruction=self.instruction, content=result, scoutId=self.id)
        db.add(observation)
        db.commit()
        return observation


class Observation(Base):
    __tablename__ = "observations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    instruction = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    scoutId = Column(String, ForeignKey("scouts.id"))

    scout = relationship("Scout", back_populates="observations")
