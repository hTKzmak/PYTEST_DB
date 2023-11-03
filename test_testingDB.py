import sqlite3
import allure
import pytest

@pytest.fixture(scope='session')
def start_stop_rest_service(start_db):
    print('Start Rest service')
    yield
    print('Stop Rest service')

@pytest.fixture(scope='session')
def start_db():
    print('Start DB')
    connection = sqlite3.connect('mainDB.db')
    yield connection
    connection.close()
    print('Stop DB')

def check_dog_added(start_db, name, breed, age):
    with start_db as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, breed, Age FROM Dogs WHERE name = ? AND breed = ? AND age = ?", (name, breed, age))
        result = cursor.fetchone()
        assert result is not None


# Проверка на добавление собаки в БД
@allure.feature('Insert dog')
@allure.story('Checking insert dog')
@pytest.mark.parametrize('name, breed, age', [('Alan', 'Banhar', 2), ('Bob', 'Banhar', 2), ('Clara', 'Beagle', 3), ('Daniel', 'Beagle', 6), ('Alan', 'Banhar', 5)])
def test_insert_dog(start_stop_rest_service, start_db, name, breed, age):
    with allure.step('making INSERT-request'):
        with start_db as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Dogs (name, breed, age) VALUES (?, ?, ?)", (name, breed, age))
            conn.commit()
            check_dog_added(start_db, name, breed, age)

        with allure.step("Checking what dog was inserted"):
            check_dog_added(start_db, name, breed, age)


# Проверка на обновление данных о собаке из БД
@allure.feature('Update dog')
@allure.story('Checking update dog')
@pytest.mark.parametrize('name, age', [('Walker', 12)])
def test_update_dog(start_stop_rest_service, start_db, name, age):
    with allure.step('making UPDATE-request'):
        with start_db as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Dogs SET age = ? WHERE name = ?", (age, name))
            conn.commit()

        with allure.step("Checking what dog was updated"):
            cursor = conn.cursor()
            cursor.execute("SELECT name, age FROM Dogs WHERE name = ?", (name,))
            result = cursor.fetchone()
            assert result is not None


# Проверка удаления собаки из БД
@allure.feature('Delete dog')
@allure.story('Checking delete dog')
@pytest.mark.parametrize('id', [(5)])
def test_delete_dog(start_stop_rest_service, start_db, id):
    with allure.step('making DELETE-request'):
        with start_db as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Dogs WHERE id = ?", (id,))
            conn.commit()

        with allure.step("Checking if dog was deleted"):
            with start_db as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Dogs WHERE id = ?", (id,))
                result = cursor.fetchone()
                assert result is None

