from fastapi import FastAPI
from db.database import Base, engine
from router import user
from router import address
from router import organization
from router import auth
from router import server
from fastapi.middleware.cors import CORSMiddleware
# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
    # Agrega aquí más dominios permitidos
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(user.router)
app.include_router(address.router)
app.include_router(organization.router)
app.include_router(auth.router)
app.include_router(server.router)
