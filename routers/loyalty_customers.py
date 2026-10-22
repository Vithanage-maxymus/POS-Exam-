from typing import Optional
from fastapi import APIRouter

from services.loyalty_service import LoyaltyService

router = APIRouter(prefix="/routes")

service = LoyaltyService(repo=LoyaltyRepository())



@router.get("/{router_id}", response_model=Optional[LoyaltyResponse])
def get_by_id( router_id: int):
    return service.get_loyalty_costomer_by_id(router_id)


