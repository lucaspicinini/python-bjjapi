from flask import Blueprint

from app.achievements.model import Achievement
from app.utils import create_pagination

achievements_bp = Blueprint('achievements', __name__, url_prefix='/achievements')

@achievements_bp.route('/')
def index(page: int | None=None) -> dict[str, int | bool | list[Achievement]]:
    return create_pagination(Achievement(), page)

@achievements_bp.route('/<int:id>')
def detail(achievement_id: int) -> Achievement:
    achievement = Achievement.query.get(achievement_id)
    return achievement.dto()