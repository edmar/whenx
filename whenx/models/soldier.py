from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from whenx.database import Base
import uuid
from sqlalchemy.sql import func
from whenx.services.create_report import create_report
from whenx.services.send_email import send_email
from dotenv import load_dotenv
import os

load_dotenv()


class Soldier(Base):
    __tablename__ = "soldiers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    instruction = Column(String)
    teamId = Column(String, ForeignKey("teams.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    team = relationship('Team', back_populates='soldiers')

    def run(self, alarm):
        if alarm.status is True:
            instruction = f"{alarm.content}{self.instruction}"
            report_content = create_report(instruction)
            report = Report(content=report_content, teamId=self.team.id, status=True)
            self.reports.append(report)
            self.send_report(self.team.name, report.content)
            return report
        else:
            return False

    def send_report(self, mission, report):
        sender = os.getenv("SENDER_EMAIL")
        email = os.getenv("USER_EMAIL")
        subject = f"Whenx Alert: {mission}"
        send_email(sender, email, subject, report)


class Report(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(String)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    soldierId = Column(String, ForeignKey("soldiers.id"))
    teamId = Column(String, ForeignKey("teams.id"))

    soldier = relationship("Soldier", backref="reports")
