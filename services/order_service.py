from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession





class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    async def create_order_service(self, session: AsyncSession, order: OrderCreate) -> OrderResponse:
        try:
            db_service = await self.repository.create(session, order)

            await session.commit()
            await session.refresh(db_service)
            return OrderResponse.model_validate(db_service)
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to create :{str(e)}")

