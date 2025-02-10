from app.achievements.model import Achievement
from app.fighters.model import Fighter
from app.lineages.model import Lineage
from app.teams.model import Team

def create_pagination(
        model: Team | Fighter | Lineage | Achievement,
        page: int | None=None
) -> dict[str, int | bool | list[Team | Fighter | Lineage | Achievement]]:
    pagination = model.query.paginate(page=page, per_page=30)
    return {
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
        "per_page": pagination.per_page,
        "has_next": pagination.has_next,
        "has_prev": pagination.has_prev,
        'z_data': [m.dto() for m in pagination.items],
    }