import pytest

from main import BooksCollector

@pytest.fixture
def book_collector():
    book_collector = BooksCollector()
    return book_collector