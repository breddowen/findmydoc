# ./backend/app/main.py
from sqlalchemy import text
from sqlmodel import Session

from app.core.db import init_sqlite_db, sqlite_engine

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.db import init_sqlite_db
from app.modules.auth.routers import router as auth_router
from app.modules.consents.routers import router as consents_router
from app.modules.events.routers import router as events_router
from app.modules.invitations.routers import router as invitations_router
from app.modules.referrals.routers import router as referrals_router
from app.modules.relationships.routers import router as relationships_router
from app.modules.specialities.routers import router as specialities_router
from app.modules.tags.routers import router as tags_router
from app.modules.users.routers import router as users_router
from app.modules.articles.routers import router as articles_router
from app.modules.services.routers import router as services_router
from app.modules.programs.routers import router as programs_router
from app.modules.questionnaires.routers import router as questionnaires_router
from app.modules.patients.routers import router as patients_router
from app.modules.assignments.routers import router as assignments_router
from app.modules.notifications.routers import router as notifications_router
from app.modules.invitations.admin_routers import router as admin_invitations_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.DATABASE_URL.startswith("sqlite"):
        init_sqlite_db()

    yield


app = FastAPI(
    title="MentalMe API",
    description=(
        "Backend для клинического маршрута MentalMe."
    ),
    version="0.5.0",
    lifespan=lifespan,
    swagger_ui_parameters={
        "persistAuthorization": True,
        "displayRequestDuration": True,
        "filter": True,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(patients_router)
app.include_router(specialities_router)
app.include_router(invitations_router)
app.include_router(admin_invitations_router)
app.include_router(tags_router)
app.include_router(relationships_router)

app.include_router(referrals_router)
app.include_router(consents_router)
app.include_router(events_router)

app.include_router(articles_router)
app.include_router(questionnaires_router)
app.include_router(services_router)
app.include_router(programs_router)

app.include_router(assignments_router)
app.include_router(notifications_router)


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "name": "MentalMe API",
        "status": "ok",
        "docs": "/docs",
    }


@app.get("/health/live", tags=["System"])
async def liveness_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/health/ready", tags=["System"])
async def readiness_check() -> dict[str, str]:
    with Session(sqlite_engine) as session:
        session.exec(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }