import pytest

from service.movie import MovieService
from tests.dao.movie import movie_dao, movie_data


class TestMovieService:

    @pytest.fixture(autouse=True)
    def init(self, movie_dao):
        self.service = MovieService(movie_dao)

    def test_get_one(self):
        record = self.service.get_one(1)

        assert record

    def test_get_all(self):
        records = self.service.get_all()

        assert len(records) > 0

    def test_create(self, movie_data):
        record = self.service.create(movie_data)

        assert record

    def test_update(self, movie_data):
        self.service.update(movie_data)

    def test_partially_update(self, movie_data):
        self.service.partially_update(movie_data)

    def test_delete(self):
        self.service.delete(1)
