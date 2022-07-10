from schemas.base import BaseComplaint


class ComplaintCreateRequest(BaseComplaint):
    title: str
    description: str
    photo_url: str
    amount: float
