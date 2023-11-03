import sqlite3
import allure
import pytest


# ����� �� ����������� ��: � ����� ��������� �� ����� 5 ����� �� ������:
@allure.feature('Dogs in nursery')
@allure.story('Checking that there are no more than 5 dogs in one kennel')
def test_dog_limit():
    conn = sqlite3.connect('mainDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Nursery")
    rows = cursor.fetchall()
    for row in rows:
        dog_list = eval(row[2])
        print(dog_list)
        assert len(dog_list) < 5  # ok


# ������ ������������� �� �����
@allure.feature('Sorted dogs names')
@allure.story('Checking that dogs are sorted by name')
def test_sorted_dogsName():
    conn = sqlite3.connect('mainDB.db')
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM Dogs ORDER BY name ASC")  # ���������� �� ����� � ������������ �������
    cursor.execute("SELECT * FROM Dogs")
    rows = cursor.fetchall()

    dogs_names = [row[1] for row in rows]
    print(dogs_names)
    # ���������, ������������� �� ������ �� �����
    assert dogs_names == sorted(dogs_names)

# ���������� ����� �� ����� 3 ���������������� �����
@allure.feature("User's preferred dog breeds")
@allure.story('Checking that buyers have no more than 3 preferred breeds')
def test_users_preferedbreeds():
    conn = sqlite3.connect('mainDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    for row in rows:
        dog_list = eval(row[3])
        print(dog_list)
        assert len(dog_list) < 3  # ok

