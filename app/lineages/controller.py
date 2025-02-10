from flask import Blueprint

from app.lineages.model import Lineage
from app.utils import create_pagination

lineages_bp = Blueprint('lineages', __name__, url_prefix='/lineages')

@lineages_bp.route('/')
def index(page: int | None=None) -> dict[str, int | bool | list[Lineage]]:
    return create_pagination(Lineage(), page)

@lineages_bp.route('/<int:id>')
def detail(lineage_id: int) -> Lineage:
    lineage = Lineage.query.get(lineage_id)
    return lineage.dto()