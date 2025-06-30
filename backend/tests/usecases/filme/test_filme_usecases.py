from sofilmes.domain.entities.filme import Filme
import uuid
from sofilmes.infra.repositories.in_memory_filme_repository import InMemoryFilmeRepository
from sofilmes.usecases.filme.create_filme import CreateFilmeUseCase
from sofilmes.usecases.filme.update_filme import UpdateFilmeUseCase
from sofilmes.usecases.filme.get_by_id_filme import GetByIdFilmeUseCase

def create_test_filme()->Filme:
    return Filme(
        id=str(uuid.uuid4()),
        titulo="Filme 1",
        tituloOriginal="Movie 1",
        ano=2025,
        avaliacao=5,
        capa="",
        descricao="Um filme com imagens",
        diretor="Nolan",
        generos=["Ação"],
    )

def test_create_filme():
    repo = InMemoryFilmeRepository()
    usecase  = CreateFilmeUseCase(repo)
    filme = create_test_filme()

    result = usecase.execute(filme)

    assert result == filme
    assert repo.get_by_id(filme.id) == filme

def test_update_filme():
    repo = InMemoryFilmeRepository()
    filme = create_test_filme()
    repo.create(filme)

    filme.titulo = "Novo Filme"

    usecase  = UpdateFilmeUseCase(repo)
    result = usecase.execute(filme)

    assert repo.get_by_id(filme.id).titulo == "Novo Filme"

def test_get_by_id_filme():
    repo = InMemoryFilmeRepository()
    filme = create_test_filme()
    repo.create(filme)


    usecase  = GetByIdFilmeUseCase(repo)
    result = usecase.execute(filme.id)

    assert result.titulo == filme.titulo