from whenx.services.create_react_agent import create_react_agent


def create_report(instruction):
    agent = create_react_agent()
    report = agent.run(instruction)
    return report
