from flask import Blueprint

from app.fighters.model import Fighter
from app.utils import create_pagination

fighters_bp = Blueprint('fighters', __name__, url_prefix='/fighters')

@fighters_bp.route('/')
def index(page: int | None=None) -> dict[str, int | bool | list[Fighter]]:
    return create_pagination(Fighter(), page)

@fighters_bp.route('/<slug>')
def detail(slug: str) -> Fighter:
    fighter = Fighter.query.filter(Fighter.slug == slug).first()
    return fighter.dto()