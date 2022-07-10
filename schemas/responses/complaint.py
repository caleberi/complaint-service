from datetime import datetime
from models import State
from schemas.base import BaseComplaint


class ComplaintResponse(BaseComplaint):
    id: int
    created_at: datetime
    status: State
