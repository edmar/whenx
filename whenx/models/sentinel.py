from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from whenx.database import Base
import uuid
from sqlalchemy.sql import func
from whenx.services.compare_observations import compare_observations


class Sentinel(Base):
    __tablename__ = "sentinels"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    instruction = Column(String)
    teamId = Column(String, ForeignKey("teams.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    team = relationship('Team', back_populates='sentinels')

    def run(self, observations=[]):
        # IF there is only one observation then we don't need to compare
        if len(observations) == 1:
            alarm = Alarm(instruction=self.instruction, content=observations[0].content, status=True)
            self.alarms.append(alarm)
            return alarm

        comparison = compare_observations(observations)
        status = "yes" in comparison.content.lower()
        alarm = Alarm(instruction=self.instruction, content=comparison.content, status=status, sentinelId=self.id)
        self.alarms.append(alarm)
        return alarm


class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(String)
    instruction = Column(String)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    sentinelId = Column(String, ForeignKey("sentinels.id"))

    sentinel = relationship("Sentinel", backref="alarms")
