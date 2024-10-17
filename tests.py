import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('new_book',
                             ['Harry Potter', '123456789_123456789_123456789_1234567890']
                             )
    def test_add_new_book(self, new_book):
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        assert new_book in BooksCollector().books_genre

    def test_add_new_book_41symbols(self):
        book_41symbol = '123456789_123456789_123456789_12345678910'
        book_collector = BooksCollector()
        book_collector.add_new_book(book_41symbol)
        assert book_41symbol not in BooksCollector().books_genre

    def test_add_new_book_no_genre(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        assert BooksCollector().books_genre[new_book] == ''

    def test_add_new_book_one_time(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.add_new_book(new_book)
        assert BooksCollector().books_genre[1] != new_book

    def test_set_book_genre(self):
        new_book = 'Harry Potter'
        new_book_genre = 'Фантастика'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.set_book_genre(new_book, new_book_genre)
        assert BooksCollector().books_genre[new_book] == new_book_genre

    def test_set_book_genre_no_genre(self):
        new_book = 'Harry Potter'
        new_book_genre = '18+'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.set_book_genre(new_book, new_book_genre)
        assert BooksCollector().books_genre[new_book] != new_book_genre

    def test_get_books_with_specific_genre(self):
        new_book1 = 'Harry Potter'
        new_book1_genre = 'Фантастика'
        new_book2 = 'LOTR'
        new_book2_genre = 'Фантастика'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book1)
        book_collector.set_book_genre(new_book1, new_book1_genre)
        book_collector.add_new_book(new_book2)
        book_collector.set_book_genre(new_book2, new_book2_genre)
        assert BooksCollector().get_books_with_specific_genre(new_book1_genre) == [new_book1, new_book2]

    def test_get_book_genre(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        assert book_collector.get_books_genre() == BooksCollector().books_genre

    def test_get_books_for_children(self):
        new_book = 'Трясло Камыш'
        book_collector = BooksCollector()
        new_book_genre = 'Комедии'
        book_collector.add_new_book(new_book)
        book_collector.set_book_genre(new_book, new_book_genre)
        assert BooksCollector().get_books_for_children() == new_book

    @pytest.mark.parametrize(
        'new_book,new_book_genre',
        [
            ['Vyazov Street', 'Ужасы'],
            ['Колобок', 'Детективы']
        ]
    )
    def test_get_books_for_children_negative(self, new_book, new_book_genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.set_book_genre(new_book, new_book_genre)
        assert BooksCollector().get_books_for_children() != new_book

    def test_add_book_in_favorites(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.add_book_in_favorites(new_book)
        assert BooksCollector().favorites == new_book

    def test_add_book_in_favorites_without_adding(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_book_in_favorites(new_book)
        assert BooksCollector().favorites != new_book

    def test_add_book_in_favorites_twice(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.add_book_in_favorites(new_book)
        book_collector.add_book_in_favorites(new_book)
        assert BooksCollector().favorites[1] != new_book

    def test_delete_book_from_favorites(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.add_book_in_favorites(new_book)
        book_collector.delete_book_from_favorites(new_book)
        assert new_book not in BooksCollector().favorites

    def test_get_list_of_favorites_books(self):
        new_book = 'Harry Potter'
        book_collector = BooksCollector()
        book_collector.add_new_book(new_book)
        book_collector.add_book_in_favorites(new_book)
        assert BooksCollector().get_list_of_favorites_books() == new_book


