import sqlite3
con = sqlite3.connect("banco/ex4.db")

# script_criacao = '''
# CREATE TABLE Times (
#     Nome VARCHAR(255),
#     Estado VARCHAR(2),
#     Pontos INT
# );'''

# insercao_data = [
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Corinthians', 'SP', 80);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Flamengo', 'RJ', 78);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Palmeiras', 'SP', 74);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Internacional', 'RS', 68);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Atlético Mineiro', 'MG', 65);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Grêmio', 'RS', 62);",
#     "INSERT INTO Times (Nome, Estado, Pontos) VALUES ('Santos', 'SP', 61);"
# ]

consulta_times_por_pontos = "SELECT * FROM Times ORDER BY Pontos DESC;"

consulta_soma_pontos_estado = "SELECT Estado, SUM(Pontos) AS TotalPontos FROM Times GROUP BY Estado     "

cur = con.cursor()
# cur.execute(script_criacao)
# for i in insercao_data:
#     cur.execute(i)

cur.execute(consulta_times_por_pontos)
print(cur.fetchall())

cur.execute(consulta_soma_pontos_estado)
print(cur.fetchall())

con.commit()

con.close()
