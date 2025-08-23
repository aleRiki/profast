from fastapi import FastAPI
from db.database import Base, engine
from router import user
from router import address
from router import organization
from router import auth
# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir routers
app.include_router(user.router)
app.include_router(address.router)
app.include_router(organization.router)
app.include_router(auth.router)

