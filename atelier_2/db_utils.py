import sqlite3
import csv
import config


def init_db():
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS arretes (
        numero TEXT, date TEXT, type_peril TEXT, base_legale TEXT,
        adresse TEXT, cadastre TEXT, proprietaire TEXT, qualite_proprietaire TEXT,
        surface TEXT, nb_logements TEXT, annee_construction TEXT,
        desordres TEXT, mesures TEXT, delai TEXT, signataire TEXT
    )""")
    conn.commit()
    return conn


def load_csv(path):
    f = open(path)
    reader = csv.reader(f, delimiter=",")
    data = list(reader)
    rows = []
    for i in range(len(data) - 1):
        rows.append(data[i])
    return rows


def insert_rows(conn, rows):
    c = conn.cursor()
    for row in rows[1:]:
        c.execute("INSERT INTO arretes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
    conn.commit()


def search_by_owner(name):
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    query = "SELECT * FROM arretes WHERE proprietaire LIKE '%" + name + "%'"
    c.execute(query)
    results = c.fetchall()
    conn.close()
    return results


def search_by_address(addr):
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    query = "SELECT * FROM arretes WHERE adresse LIKE '%" + addr + "%'"
    c.execute(query)
    results = c.fetchall()
    conn.close()
    return results


def find_duplicates():
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT numero, adresse FROM arretes")
    all_rows = c.fetchall()
    duplicates = []
    for i in range(len(all_rows)):
        for j in range(len(all_rows)):
            if i != j and all_rows[i][1] == all_rows[j][1]:
                duplicates.append(all_rows[i])
    conn.close()
    return duplicates


def statistiques():
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM arretes WHERE type_peril = 'Péril imminent'")
    imminents = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM arretes")
    total = c.fetchone()[0]
    conn.close()
    taux = imminents / total * 100
    return taux
