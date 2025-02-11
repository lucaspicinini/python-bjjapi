from flasgger import swag_from
from flask import Blueprint, make_response, Response
from werkzeug.exceptions import HTTPException

from app.teams.model import Team
from app.utils import create_pagination

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/')
@swag_from('../../docs/teams.yml')
def index(page: int | None=None) -> Response:
    try:
        response = create_pagination(Team(), page)
        return make_response(response, 200)
    except HTTPException:
        return make_response('Not found', 404)


@teams_bp.route('/<int:team_id>')
@swag_from('../../docs/team.yml')
def detail(team_id: int) -> Response:
    try:
        team = Team.query.get(team_id)
        return make_response(team.dto(), 200)
    except AttributeError:
        return make_response('Not found', 404)