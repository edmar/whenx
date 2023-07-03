from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from whenx.models.team import Team
from whenx.models.scout import Scout
from whenx.models.sentinel import Sentinel
from whenx.models.soldier import Soldier
import re
from whenx.database import db


class Captain:

    def __init__(self, mission: str):
        self.mission = mission

    def run(self, team):
        prompts = self.generate_prompts()
        team = self.create_team(prompts, team)
        return team

    def initialize_team(self, prompts, team):
        db.add(team)
        db.commit()
        scout = Scout(instruction=prompts["scout"], teamId=team.id)
        sentinel = Sentinel(instruction=prompts["sentinel"], teamId=team.id)
        soldier = Soldier(instruction=prompts["soldier"], teamId=team.id)
        db.add(scout)
        db.add(sentinel)
        db.add(soldier)
        db.commit()
        return team

    def generate_prompts(self):
        system = """You are the captain of a team of scouts, sentinels, and soldiers.
You generate instructions for your team to follow based on a mission.
Scouts are responsible for gathering information from the internet.
Sentinels are responsible for monitoring the observations of scouts for changes.
Soldiers are responsible for writing reports.
Instruction examples:
Mission: When apple relseases a new product.
Scout:  What is the new apple product? return the answer.
Sentinel: Was a new product released? Reply with (Yes/No) and the name of the product.
Soldier: Write a report about it.
"""

        prompt = f"""
Complete the instructions for the scouts, sentinels, and soldiers. One per line.
Mission:{self.mission}
"""
        model = ChatOpenAI(model="gpt-4", temperature=0)
        messages = [
            SystemMessage(
                content=system
            ),
            HumanMessage(content=prompt),
        ]
        response = model(messages)
        response = self.parse_response(response.content)
        return response

    def parse_response(self, response):
        lines = re.split(r'\n+', response.strip())
        # Extract the relevant information from the lines
        prompts = {}
        prompts["scout"] = lines[0].split(": ")[1]
        prompts["sentinel"] = lines[1].split(": ")[1]
        prompts["soldier"] = lines[2].split(": ")[1]
        return prompts
