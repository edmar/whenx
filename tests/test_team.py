from pytest import fixture
from whenx.models.team import Team
from whenx.models.soldier import Soldier
from whenx.models.scout import Scout
from whenx.models.sentinel import Sentinel
from whenx.database import db


@fixture
def team():
    team = Team(name="test team")
    db.add(team)
    db.commit()
    scout = Scout(instruction="what was the latest book by Haruki murakami? return the answer.", teamId=team.id)
    sentinel = Sentinel(instruction="Was a new book released? Reply with (Yes/No) and the title.", teamId=team.id)
    soldier = Soldier(instruction="Write a report about it.", teamId=team.id)
    db.add(scout)
    db.add(sentinel)
    db.add(soldier)
    db.commit()

    yield team

    db.delete(soldier)
    db.delete(sentinel)
    db.delete(scout)
    db.delete(team)
    db.commit()


def test_run(team):
    report = team.run()
    assert report.status is True
