import psycopg2

def create_db(cur):
        cur.execute("""CREATE TABLE IF NOT EXISTS clients(
        client_id SERIAL PRIMARY KEY,
        first_name VARCHAR(10),
        last_name VARCHAR(20),
        email VARCHAR(30) UNIQUE
        );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER REFERENCES clients(client_id),
        phone VARCHAR(12)
        );""")
 
def add_client(cur, client_id, first_name, last_name, email, phones=None):
        cur.execute("""INSERT INTO clients(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);"""
        , (client_id, first_name, last_name, email))
        
        cur.execute("""INSERT INTO phones(client_id, phone) VALUES(%s, %s);""", (client_id, phones))
        
def add_phone(cur, client_id, phone):
        cur.execute("""INSERT INTO phones(client_id, phone) VALUES(%s, %s);""", (client_id, phone))
    
def change_client(cur, client_id, first_name, last_name, email, phone):
        cur.execute("""UPDATE clients SET first_name=%s, last_name=%s, email=%s WHERE client_id=%s;""", (first_name, last_name, email, client_id))
        
        cur.execute("""UPDATE phones SET phone=%s WHERE client_id=%s;""", (phone, client_id))
        
def delete_phone(cur, client_id, phone):
        cur.execute("""DELETE FROM phones WHERE client_id=%s AND phone=%s;""", (client_id, phone))

def delete_client(cur, client_id):
        cur.execute("""DELETE FROM phones WHERE client_id=%s;""", (client_id))
        cur.execute("""DELETE FROM clients WHERE client_id=%s;""", (client_id))
        
def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
        cur.execute("""
                SELECT *
                  FROM clients cl
                  JOIN phones ph ON cl.client_id = ph.client_id
                 WHERE (first_name = %(first_name)s OR %(first_name)s IS NULL)
                   AND (last_name = %(last_name)s OR %(last_name)s IS NULL)
                   AND (email = %(email)s OR %(email)s IS NULL)
                   AND (phone = %(phone)s OR %(phone)s IS NULL);
            """, {"first_name": first_name, "last_name": last_name, "email": email, "phone": phone})
        print(cur.fetchall())
if __name__ == "__main__":          
    with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
        with conn.cursor() as cur:        
        #     create_db(cur)
        #     add_client(cur, 1, 'Илья', 'Потешонков', 'ilyapatis24@mail.ru')
            # add_client(cur, 2, 'Алексей', 'Дэрий', 'aderiy@mail.ru', 89115422112)
            # add_phone(cur, 2, 89315212145)
            # change_client(cur, 1, 'Илья', 'Петров', 'ilyapetrov28@gmail.com', 89115330286)
            # change_client(cur, 2, 'Данила', 'Иванов', 'divanov25@gmail.com', 89117660133)
            # delete_phone(cur, 2, '89117660133')
            # delete_client(cur,'1')
            # delete_client(cur,'2')
            find_client(cur,'Илья', 'Потешонков')