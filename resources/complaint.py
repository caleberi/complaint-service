from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import is_admin, is_approver, oauth2_scheme, is_complainer
from managers.complaint import ComplaintManager
from models import complaint
from schemas.requests.complaint import ComplaintCreateRequest
from schemas.responses.complaint import ComplaintResponse

router = APIRouter(tags=["Complaint"])


@router.get(
    "/complaints/",
    dependencies=[Depends(oauth2_scheme)],
    response_model=List[ComplaintResponse],
)
async def get_complaints(request: Request):
    user = request.state.user
    return await ComplaintManager.get_all_complaints(user)


@router.post(
    "/complaints/",
    dependencies=[Depends(oauth2_scheme), Depends(is_complainer)],
    response_model=ComplaintResponse,
)
async def create_complaint(request: Request, complaint: ComplaintCreateRequest):
    user = request.state.user
    return await ComplaintManager.create_complaint(user, complaint.dict())


@router.delete(
    "/complaint/{complaint_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def delete_complaint(complaint_id: int):
    return await ComplaintManager.delete_complaint(complaint_id)


@router.put(
    "/complaint/{complaint_id}/approve",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
)
async def approve_complaint(complaint_id: int):
    return await ComplaintManager.approve_complaint(complaint_id)


@router.put(
    "/complaint/{complaint_id}/reject",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
)
async def reject_complaint(complaint_id: int):
    return await ComplaintManager.reject_complaint(complaint_id)
