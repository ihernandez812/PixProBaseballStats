from team import Team
from constants import *
import uuid
from uuid import UUID

class Division:
    ID='id'
    NAME='name'
    def __init__(self, name: str, teams: list[str], conference: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.teams = teams
        self.conference = conference

    def get_id(self) -> UUID:
        return self.id
    
    def get_teams(self) -> list[str]:
        return self.teams
    
    def add_team(self, team: str) -> None:
        self.teams.append(team)

    def get_conference(self) -> str:
        return self.conference
    
    def set_conference(self, conference: str) -> None:
        self.conference = conference

    def to_dict(self) -> dict:
        return {
            self.ID: str(self.id),
            self.NAME: self.name,
            League.TEAMS: self.teams,
            League.CONFERENCE: self.conference
        }
    
