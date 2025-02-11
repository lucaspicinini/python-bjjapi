from flasgger import swag_from
from flask import Blueprint, make_response, Response
from werkzeug.exceptions import HTTPException

from app.achievements.model import Achievement
from app.utils import create_pagination

achievements_bp = Blueprint('achievements', __name__, url_prefix='/achievements')

@achievements_bp.route('/')
@swag_from('../../docs/achievements.yml')
def index(page: int | None=None) -> Response:
    try:
        response = create_pagination(Achievement(), page)
        return make_response(response, 200)
    except HTTPException:
        return make_response('Not Found', 404)

@achievements_bp.route('/<int:achievement_id>')
@swag_from('../../docs/achievement.yml')
def detail(achievement_id: int) -> Response:
    try:
        achievement = Achievement.query.get(achievement_id)
        return make_response(achievement.dto(), 200)
    except AttributeError:
        return make_response('Not Found', 404)