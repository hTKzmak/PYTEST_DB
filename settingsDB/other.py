import sqlite3
coding: 'utf-8'

connection = sqlite3.connect('../mainDB.db')
cursor = connection.cursor()



# dogs1 = ['Banhar', 'Bobtail', 'Beagle', 'Banhar']
# dogs2 = ['Beagle', 'Gampr', 'Banhar']
# dogs3 = ['Banhar', 'Gampr', 'Boerbur']
#
# cursor.execute('INSERT INTO Nursery (city, dogs) VALUES (?, ?)', ('Moscow', str(dogs1)))
# cursor.execute('INSERT INTO Nursery (city, dogs) VALUES (?, ?)', ('Kazan', str(dogs2)))
# cursor.execute('INSERT INTO Nursery (city, dogs) VALUES (?, ?)', ('Saint-Petersburg', str(dogs2)))


# cursor.execute("DELETE FROM Nursery WHERE id = ?", ((3),))


# dogs1 = ['Bobtail', 'Beagle']
# dogs2 = ['Beagle', 'Gampr']
# dogs3 = ['Banhar']



# cursor.execute('UPDATE Users SET PreferredBreeds = ? WHERE id = ?', (str(dogs1), 1))

# cursor.execute('INSERT INTO Users (FirstName, LastName, PreferredBreeds) VALUES (?, ?, ?)', ('Alan', 'Wake', str(dogs1)))
# cursor.execute('INSERT INTO Users (FirstName, LastName, PreferredBreeds) VALUES (?, ?, ?)', ('Mark', 'Ryden', str(dogs2)))
# cursor.execute('INSERT INTO Users (FirstName, LastName, PreferredBreeds) VALUES (?, ?, ?)', ('Alan', 'Becker', str(dogs3)))

# cursor.execute("DELETE FROM Users WHERE id = ?", ((1),))
# cursor.execute("DELETE FROM Users WHERE id = ?", ((2),))
# cursor.execute("DELETE FROM Users WHERE id = ?", ((3),))
connection.commit()
connection.close()