from dao.director import DirectorDAO
from dao.model.director import Director
import pytest


class DirectorDAOMock(DirectorDAO):
    def __init__(self):
        super().__init__(None)

    def get_one(self, bid):
        return Director(id=bid, name='test')

    def get_all(self):
        return [Director(id=1, name='test')]

    def create(self, director_d):
        return director_d

    def delete(self, rid):
        pass

    def update(self, director_d):
        pass


@pytest.fixture()
def director_dao():
    return DirectorDAOMock()


@pytest.fixture()
def director_data():
    return {'id': 1, 'name': 'test'}
