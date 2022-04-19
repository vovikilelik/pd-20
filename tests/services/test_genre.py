import pytest

from service.genre import GenreService
from tests.dao.genre import genre_dao, genre_data


class TestGenreService:

    @pytest.fixture(autouse=True)
    def init(self, genre_dao):
        self.service = GenreService(genre_dao)

    def test_get_one(self):
        record = self.service.get_one(1)

        assert record

    def test_get_all(self):
        records = self.service.get_all()

        assert len(records) > 0

    def test_create(self, genre_data):
        record = self.service.create(genre_data)

        assert record

    def test_update(self, genre_data):
        self.service.update(genre_data)

    def test_partially_update(self, genre_data):
        self.service.partially_update(genre_data)

    def test_delete(self):
        self.service.delete(1)
