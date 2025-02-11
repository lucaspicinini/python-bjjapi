from flasgger import swag_from
from flask import Blueprint, make_response, Response
from werkzeug.exceptions import HTTPException

from app.fighters.model import Fighter
from app.utils import create_pagination

fighters_bp = Blueprint('fighters', __name__, url_prefix='/fighters')

@fighters_bp.route('/')
@swag_from('../../docs/fighters.yml')
def index(page: int | None=None) -> Response:
    try:
        response = create_pagination(Fighter(), page)
        return make_response(response, 200)
    except HTTPException:
        return make_response('Not found', 404)

@fighters_bp.route('/<slug>')
@swag_from('../../docs/fighter.yml')
def detail(slug: str) -> Response:
    try:
        fighter = Fighter.query.filter(Fighter.slug == slug).first()
        return make_response(fighter.dto(), 200)
    except AttributeError:
        return make_response('Not found', 404)