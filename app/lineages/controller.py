from flasgger import swag_from
from flask import Blueprint, make_response, Response
from werkzeug.exceptions import HTTPException

from app.lineages.model import Lineage
from app.utils import create_pagination

lineages_bp = Blueprint('lineages', __name__, url_prefix='/lineages')

@lineages_bp.route('/')
@swag_from('../../docs/lineages.yml')
def index(page: int | None=None) -> Response:
    try:
        response = create_pagination(Lineage(), page)
        return make_response(response, 200)
    except HTTPException:
        return make_response('Not Found', 404)

@lineages_bp.route('/<int:lineage_id>')
@swag_from('../../docs/lineage.yml')
def detail(lineage_id: int) -> Response:
    try:
        lineage = Lineage.query.get(lineage_id)
        return make_response(lineage.dto(), 200)
    except AttributeError:
        return make_response('Not Found', 404)