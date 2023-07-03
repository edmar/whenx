from whenx.services.create_autogpt import create_autogpt


def test_create_autogpt():
    instruction = "what was the latest book from Haruki Murakami?"
    agent = create_autogpt()
    result = agent.run(instruction)
    assert result is not None
