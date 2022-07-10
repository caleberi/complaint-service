from db import database
from models import complaints, RoleType, State


class ComplaintManager:
    @staticmethod
    async def get_all_complaints(user):
        query = complaints.select()
        if user["role"] == RoleType.complainer:
            return await database.fetch_all(
                query.where(complaints.c.complainer_id == user["id"])
            )
        elif user["role"] == RoleType.approver:
            return await database.fetch_all(
                query.where(complaints.c.status == State.pending)
            )
        return await database.fetch_all(query)

    @staticmethod
    async def create_complaint(user, complaint):
        complaint["complainer_id"] = user["id"]
        id_ = await database.execute(complaints.insert().values(**complaint))
        return await database.fetch_one(
            complaints.select().where(complaints.c.id == id_)
        )

    @staticmethod
    async def delete_complaint(id_: int):
        await database.execute(complaints.delete().where(complaints.c.id == id_))

    @staticmethod
    async def approve_complaint(id_: int):
        await database.execute(
            complaints.update()
            .where(complaints.c.id == id_)
            .values(status=State.approved)
        )

    @staticmethod
    async def reject_complaint(id_: int):
        await database.execute(
            complaints.update()
            .where(complaints.c.id == id_)
            .values(status=State.rejected)
        )
