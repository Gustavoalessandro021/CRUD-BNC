import sqlite3  

banco_alunos = sqlite3.connect('banco_alunos')


cursor = banco_alunos.cursor()

# cursor.execute("CREATE TABLE alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, idade integer,email text )")
# cursor.execute("INSERT INTO alunos(id,nome,idade,email)VALUES(1, 'Juan',17,'juanpedro@gmail.com')") 
# cursor.execute("INSERT INTO alunos(id,nome,idade,email)VALUES(2, 'Arthur',18,'arthurfreitas@gmail.com')") 
# cursor.execute("INSERT INTO alunos(id,nome,idade,email)VALUES(3, 'Gustavo',19,'gustavosilva@gmail.com')") 


# cursor.execute("SELECT * FROM alunos")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM alunos WHERE id = 2")
# print(cursor.fetchall())
# cursor.execute("UPDATE alunos SET nome = 'Juam' WHERE id = 1 ")
# print(cursor.fetchall())

# cursor.execute("DELETE FROM alunos WHERE id = 3 ")

banco_alunos.commit()



