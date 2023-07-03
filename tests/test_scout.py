from pytest import fixture
from whenx.models import User, Scout, Team
from whenx.database import db


@fixture(scope="function")
def scout():
    # Setup
    user = User(name="test user", email="ed@gmail.com")
    db.add(user)
    db.commit()

    team = Team(name="test team", userId=user.id)
    db.add(team)
    db.commit()

    instruction = "what was the latest book by Haruki Murakami? return the answer."
    scout = Scout(instruction=instruction, teamId=team.id)
    db.add(scout)
    db.commit()

    yield scout

    # Teardown
    db.delete(scout)
    db.delete(team)
    db.delete(user)
    db.commit()


def test_run(scout):
    observation = scout.run()
    assert observation.content is not None
    assert observation.scoutId == scout.id
