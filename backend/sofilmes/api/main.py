from fastapi import FastAPI
#from sofilmes.api.routes import comment_route, post_route, user_route
from sofilmes.api.openapi_tags import openapi_tags


app = FastAPI(
    title="SóFilmes API",
    description="API backend do SóFilmes com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Marcos Daré e Pedro Manoel", "email": "sofilmes@exemplo.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
)


@app.get("/")
def ola():
    return {"olá": "fastapi"}