from pytest import fixture
from whenx.models.sentinel import Sentinel
from whenx.models.scout import Observation


@fixture(scope="function")
def sentinel():
    # Setup
    sentinel = Sentinel(instruction="Was a new book released? Reply with (Yes/No) and the title.")
    yield sentinel

    # Teardown
    pass


@fixture(scope="function")
def no_change():
    observation_1 = Observation(instruction="What was the last book by Murakami?", content="The last book is Killing Comendatore", created_at="2019-01-01 00:00:00")
    observation_2 = Observation(instruction="What was the last book by Murakami?", content="Killing Comendatore", created_at="2019-01-02 00:00:00")
    obeservations = [observation_1, observation_2]
    yield obeservations


@fixture(scope="function")
def change():
    observation_1 = Observation(instruction="What was the last book by Murakami?", content="The books is Killing Comendatore", created_at="2019-01-01 00:00:00")
    observation_2 = Observation(instruction="What was the last book by Murakami?", content="The latest book by Haruki Murakami is The Forbidden Worlds of Haruki Murakami.", created_at="2019-01-02 00:00:00")
    obeservations = [observation_1, observation_2]
    yield obeservations


def test_run_no_change(sentinel, no_change):
    alarm = sentinel.run(no_change)
    assert alarm.status is False


def test_run_change(sentinel, change):
    alarm = sentinel.run(change)
    assert alarm.status is True
