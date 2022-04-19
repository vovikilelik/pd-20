import pytest

from service.director import DirectorService
from tests.dao.director import director_dao, director_data


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def init(self, director_dao):
        self.service = DirectorService(director_dao)

    def test_get_one(self):
        record = self.service.get_one(1)

        assert record

    def test_get_all(self):
        records = self.service.get_all()

        assert len(records) > 0

    def test_create(self, director_data):
        record = self.service.create(director_data)

        assert record

    def test_update(self, director_data):
        self.service.update(director_data)

    def test_partially_update(self, director_data):
        self.service.partially_update(director_data)

    def test_delete(self):
        self.service.delete(1)
