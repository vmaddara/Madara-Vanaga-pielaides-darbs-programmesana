# Importē sqlite3 moduli.
import sqlite3

# Izveido savienojumu ar 'klienti.db' datu bāzi.
conn = sqlite3.connect('klienti.db')
cursor = conn.cursor()

# Izveido kursora objektu.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS klienti
    (id INTEGER PRIMARY KEY, vards TEXT, epasts TEXT, telNum INTEGER )
''')

# Definē funkciju klienta pievienošanai datu bāzei.
def pievienotKlientu(vards, epasts, telNum):
    conn = sqlite3.connect('klienti.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO klienti (vards, epasts, telNum)
        VALUES (?, ?, ?)
    ''', (vards, epasts, telNum))

    conn.commit()
    conn.close()

# Definē funkciju klienta atjaunināšanai datu bāzē.
def atjauninatKlientu(id, vards, epasts, telNum):
    conn = sqlite3.connect('klienti.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE klienti
        SET vards = ?, epasts = ?, telNum = ?
        WHERE id = ?
    ''', (vards, epasts, telNum, id))

    conn.commit()
    conn.close()

# Definē funkciju, lai iegūtu visus klientus no datu bāzes.
def dabutVisusKlientus():
    conn = sqlite3.connect('klienti.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM klienti
    ''')

    rindas = cursor.fetchall()
    conn.close()
    return rindas

# Definē funkciju klientu meklēšanai datu bāzē.
def mekletKlientu(query):
    conn = sqlite3.connect('klienti.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM klienti
        WHERE vards LIKE ? OR epasts LIKE ?
    ''', ('%{}%'.format(query), '%{}%'.format(query)))

    rindas = cursor.fetchall()
    conn.close()
    return rindas

conn = sqlite3.connect('klienti.db')
cursor = conn.cursor()

# Izdrukā izvēlni ar lietotāja iespējām.
while True:
    print('1. pievienot jaunu klientu')
    print('2. atjaunināt klientu')
    print('3. apskatīt visus klientus')
    print('4. meklēt klientu')
    print('5. iziet')

# Iegūt lietotāja izvēli.
    choice = input('Ievadiet savu izvēli: ')

# Ja lietotājs izvēlas 1. opciju, pieprasīt klienta informāciju un pievienot klientu datu bāzei.
    if choice == '1':
        vards = input('ievadiet klienta vārdu: ')
        epasts = input('ievadiet klienta e-pastu: ')
        telNum = input('ievadiet klienta telefona numuru: ')
        pievienotKlientu(vards, epasts, telNum)
        print('klients pievienots veiksmīgi!')

# Ja lietotājs izvēlas 2. opciju, pieprasīt klienta ID un jaunu informāciju un atjaunot klientu datu bāzē.
    elif choice == '2':
        id = input('ievadiet klienta ID: ')
        vards = input('ievadiet klienta vārdu: ')
        epasts = input('ievadiet klienta e-pastu: ')
        telNum = input('ievadiet klienta telefona numuru: ')
        atjauninatKlientu(id, vards, epasts, telNum)
        print('klients atjaunots veiksmīgi!')

# Ja lietotājs izvēlas 3. opciju, iegūt visus klientus no datu bāzes un izdrukāt tos.
    elif choice == '3':
        klienti = dabutVisusKlientus()
        print('ID\tvards\tepasts\ttelNum')
        print('--\t----\t-----\t-----')
        for klients in klienti:
            print('{}\t{}\t{}\t{}'.format(klients[0], klients[1], klients[2], klients[3]))

# Ja lietotājs izvēlas 4. opciju, jautāt meklēšanas vaicājumam un meklēt klientus datu bāzē.
    elif choice == '4':
        query = input('Ievadiet meklēšanas vaicājumu(query): ')
        rezultats = mekletKlientu(query)
        print('ID\tvards\tepasts\ttelNum')
        print('--\t----\t-----\t-----')
        for klients in rezultats:
            print('{}\t{}\t{}\t{}'.format(klients[0], klients[1], klients[2], klients[3]))

# Ja lietotājs izvēlas 5. opciju, iziet no programmas.
    elif choice == '5':
        print('Visu labu!')
        break

# Ja lietotājs ievada nederīgu izvēli, izdrukāt kļūdas ziņojumu un vēlreiz jautājiet.
    else:
        print('Nederīga izvēle. Lūdzu mēģiniet vēlreiz.')


