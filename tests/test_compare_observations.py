from pytest import fixture
from whenx.services.compare_observations import compare_observations
from whenx.models.scout import Observation


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


def test_compare_observations_no_change(no_change):
    instruction = "Was a new book released? Reply with (Yes/No) and the title."
    result = compare_observations(instruction, no_change)
    # check if the result.content contains "No"
    assert "No" in result.content


def test_compare_observations_change(change):
    instruction = "Was a new book released? Reply with (Yes/No) and the title."
    result = compare_observations(instruction, change)
    assert "Yes" in result.content
