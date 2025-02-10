from app.achievements.model import Achievement
from app.fighters.model import Fighter
from app.lineages.model import Lineage
from app.teams.model import Team

class ApiPagination:
    def __init__(self, pagination):
        self.total = pagination.total
        self.pages = pagination.pages
        self.page = pagination.page
        self.per_page = pagination.per_page
        self.has_next = pagination.has_next
        self.has_prev = pagination.has_prev

def create_pagination(
        model: Team | Fighter | Lineage | Achievement,
        page: int | None=None
) -> dict[str, ApiPagination | list[Team | Fighter | Lineage | Achievement]]:
    pagination = model.query.paginate(page=page, per_page=30)
    api_pagination = ApiPagination(pagination)
    return {
        "total": api_pagination.total,
        "pages": api_pagination.pages,
        "current_page": api_pagination.page,
        "per_page": api_pagination.per_page,
        "has_next": api_pagination.has_next,
        "has_prev": api_pagination.has_prev,
        'z_data': [m.dto() for m in pagination.items],
    }