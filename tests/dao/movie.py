import pytest

from dao.movie import MovieDAO


class MovieDAOMock(MovieDAO):
    def __init__(self):
        super().__init__(None)

    def get_one(self, bid):
        return {'id': bid, 'name': 'test'}

    def get_all(self):
        return [{'id': 1, 'name': 'test'}]

    def create(self, director_d):
        return director_d

    def delete(self, rid):
        pass

    def update(self, director_d):
        pass


@pytest.fixture()
def movie_dao():
    return MovieDAOMock()


@pytest.fixture()
def movie_data():
    return {'id': 1, 'name': 'test'}
