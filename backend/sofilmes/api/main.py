from fastapi import FastAPI, status, Request
from sofilmes.api.routes import filme_route
from sofilmes.api.routes import usuario_route
from sofilmes.api.routes import avaliacao_route
from sofilmes.api.openapi_tags import openapi_tags
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI(
    title="SóFilmes API",
    description="API backend do SóFilmes com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Marcos Daré e Pedro Manoel", "email": "sofilmes@exemplo.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
    redirect_slashes=True
)

origins = [
    "http://localhost:5173",  # Vite local
    #"https://localhost:5173",  # Vite local
    "https://so-filmes.vercel.app/",  # Produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # lista de origens confiáveis
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique ["GET", "POST"]
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        field = ".".join(str(loc) for loc in err["loc"] if isinstance(loc, str))
        errors.append({
            "field": field,
            "message": err["msg"]
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Erro de validação nos campos enviados.",
            "errors": errors
        },
    )


@app.get("/")
def ola():
    return {"olá": "fastapi"}


app.include_router(usuario_route.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(filme_route.router, prefix="/filme", tags=["Filmes"])
app.include_router(avaliacao_route.router, prefix="/avaliacao", tags=["Avaliações"])
