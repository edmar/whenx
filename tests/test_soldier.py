from pytest import fixture
from whenx.models.soldier import Soldier
from whenx.models.sentinel import Alarm


@fixture(scope="function")
def soldier():
    # Setup
    soldier = Soldier(instruction="Write a report about it.")
    yield soldier

    # Teardown
    pass


@fixture(scope="function")
def alarm_true():
    alarm = Alarm(content="Yes, The latest book by Haruki Murakami is The Forbidden Worlds of Haruki Murakami.", status=True)
    yield alarm


@fixture(scope="function")
def alarm_false():
    alarm = Alarm(content="No, The last book is Killing Comendatore", status=False)
    yield alarm


def test_run_true(alarm_true, soldier):
    report = soldier.run(alarm_true)
    assert report.content is not None


def test_run_false(alarm_false, soldier):
    report = soldier.run(alarm_false)
    assert report is False
