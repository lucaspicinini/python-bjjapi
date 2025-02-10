from flask import Blueprint

from app.teams.model import Team
from app.utils import create_pagination

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/')
def index(page: int | None=None) -> dict[str, int | bool | list[Team]]:
    return create_pagination(Team(), page)

@teams_bp.route('/<int:id>')
def detail(team_id: int) -> Team:
    fighter = Team.query.get(team_id)
    return fighter.dto()