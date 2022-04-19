from dao.genre import GenreDAO
import pytest

from dao.model.genre import Genre


class GenreDAOMock(GenreDAO):
    def __init__(self):
        super().__init__(None)

    def get_one(self, bid):
        return Genre(id=bid, name='test')

    def get_all(self):
        return [Genre(id=1, name='test')]

    def create(self, director_d):
        return director_d

    def delete(self, rid):
        pass

    def update(self, director_d):
        pass


@pytest.fixture()
def genre_dao():
    return GenreDAOMock()


@pytest.fixture()
def genre_data():
    return {'id': 1, 'name': 'test'}
