from sqlalchemy import Column, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from whenx.database import Base
import uuid


class Team(Base):
    __tablename__ = "teams"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    description = Column(String)
    userId = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    scouts = relationship('Scout', back_populates='team')
    sentinels = relationship('Sentinel', back_populates='team')
    soldiers = relationship('Soldier', back_populates='team')
    user = relationship("User", backref="teams")
    reports = relationship("Report", back_populates="team")

    def run(self):
        # Run the Scout
        scout = self.scouts[0]
        scout.run()
        # Get the last 2 observations
        observations = scout.observations[:2]
        # Run the Sentinel
        sentinel = self.sentinels[0]
        alarm = sentinel.run(observations)
        # Run the Soldier
        soldier = self.soldiers[0]
        report = soldier.run(alarm)
        # update the updated_at field
        self.updated_at = func.now()
        return report
