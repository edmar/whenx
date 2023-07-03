from whenx.models import Scout, Sentinel, Soldier
from whenx.database import db


def create_team(team):
    scout = Scout(instruction=team.name, teamId=team.id)
    sentinel = Sentinel(instruction=team.name, teamId=team.id)
    soldier = Soldier(instruction="Write a report about the answer.", teamId=team.id)
    db.add(scout)
    db.add(sentinel)
    db.add(soldier)
    db.commit()
    team.initialized = True
    db.add(team)
    db.commit()
    return team
