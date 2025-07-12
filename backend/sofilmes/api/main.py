from fastapi import FastAPI
from sofilmes.api.routes import filme_route
from sofilmes.api.routes import usuario_route
from sofilmes.api.routes import avaliacao_route
from sofilmes.api.openapi_tags import openapi_tags
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="SóFilmes API",
    description="API backend do SóFilmes com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Marcos Daré e Pedro Manoel", "email": "sofilmes@exemplo.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
)

origins = [
    "http://localhost:5173",  # Vite local
    "https://frontclean.vercel.app",  # Produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # lista de origens confiáveis
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique ["GET", "POST"]
    allow_headers=["*"],
)


@app.get("/")
def ola():
    return {"olá": "fastapi"}


app.include_router(usuario_route.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(filme_route.router, prefix="/filme", tags=["Filmes"])
app.include_router(avaliacao_route.router, prefix="/avaliacao", tags=["Avaliações"])
