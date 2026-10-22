from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession





class LoyaltyService:
    def __init__(self):
        self.repository = LoyaltyRepository()

    async def create_loyalty_service(self, session: AsyncSession, loyalty: ServiceCreate) -> LoyaltyResponse:
        try:
            db_service = await self.repository.create(session, loyalty)

            await session.commit()
            await session.refresh(db_service)
            return LoyaltyResponse.model_validate(db_service)
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to create :{str(e)}")

