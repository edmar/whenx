from pytest import fixture
from whenx.services.create_report import create_report


@fixture(scope="function")
def instruction():
    alarm = "Yes, the latest book by Haruki Murakami is The Forbidden Worlds of Haruki Murakami."
    instruction = f"{alarm} Write a report about it."
    yield instruction


def test_create_report(instruction):
    report = create_report(instruction)
    assert report.status is True
