from whenx.models.captain import Captain
from pytest import fixture


@fixture
def captain():
    mission = "when Haruki Murakami releases a new book, write a report about it."
    captain = Captain(mission)
    yield captain


def test_run(captain):
    team = captain.run()
    assert team.scouts[0].instruction == "What is the new Haruki Murakami book? return the answer."
    assert team.sentinels[0].instruction == "Was a new Haruki Murakami book released? Reply with (Yes/No) and the name of the book."
    assert team.soldier[0].instruction == "Write a report about it."


def test_run_team(captain):
    team = captain.run()
    report = team.run()
    assert report == "A new Haruki Murakami book was released."
