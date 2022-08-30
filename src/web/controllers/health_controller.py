# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends

from src.infra.logging import get_logger

router = APIRouter()

# logger = logging.getLogger("HealthController")


@router.get("/health")
async def health(logger=Depends(get_logger)):
    logger.info("hello there")
    return {"status": "ok"}
