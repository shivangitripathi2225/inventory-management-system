from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.dashboard import (
    DashboardResponse
)

from app.services.dashboard_service import (
    DashboardService
)

from app.api.dependencies import (
    get_dashboard_service
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "",
    response_model=DashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db),
    service: DashboardService = Depends(
        get_dashboard_service
    )
):
    return service.get_dashboard(db)