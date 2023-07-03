from whenx.models import Team, Captain
from whenx.database import db
import schedule
import time
from prettytable import PrettyTable


def create(mission):
    captain = Captain(mission)
    team = Team(name=mission)
    team = captain.run(team)
    print(f"Team created with mission: {team.name}")
    print(f"Scout: {team.scouts[0].instruction}")
    print(f"Sentinel: {team.sentinels[0].instruction}")
    print(f"Soldier: {team.soldiers[0].instruction}")


def run():
    # Get all teams from the database
    for team in db.query(Team).all():
        # Run the team
        print(f"Team: {team.name}")
        print("Running...")
        report = team.run()
        if report:
            print(report.content)
        else:
            print("Nothing new to report\n")


def monitor():
    schedule.every().day.do(run)

    while True:
        schedule.run_pending()
        print('Waiting for next')
        time.sleep(60)


def list():
    teams = db.query(Team).all()

    # Create a new table with the column headers
    table = PrettyTable()
    table.field_names = ["ID", "Mission", "Last Update"]

    # Add each team to the table as a new row
    for team in teams:
        table.add_row([team.id, team.name, team.updated_at])

    # Print the table to the console
    print(table)


def delete(id):
    db.query(Team).filter(Team.id == id).delete()
    db.commit()
