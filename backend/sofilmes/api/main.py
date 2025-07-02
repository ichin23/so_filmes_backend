from fastapi import FastAPI
<<<<<<< HEAD
#from sofilmes.api.routes import comment_route, post_route, user_route
=======
from sofilmes.api.routes import comment_route, post_route, user_route
>>>>>>> 5fe0da8 (schemas e models)
from sofilmes.api.openapi_tags import openapi_tags


app = FastAPI(
<<<<<<< HEAD
    title="SóFilmes API",
    description="API backend do SóFilmes com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Marcos Daré e Pedro Manoel", "email": "sofilmes@exemplo.com"},
=======
    title="SoFilmes API",
    description="API backend do Blog com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Lázaro Eduardo", "email": "lazaro@exemplo.com"},
>>>>>>> 5fe0da8 (schemas e models)
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
)


@app.get("/")
def ola():
<<<<<<< HEAD
    return {"olá": "fastapi"}
=======
    return {"olá": "fastapi"}


app.include_router(user_route.router, prefix="/users", tags=["Users"])
app.include_router(post_route.router, prefix="/posts", tags=["Posts"])
app.include_router(comment_route.router, prefix="/comments", tags=["Comments"])
>>>>>>> 5fe0da8 (schemas e models)
