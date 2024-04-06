import sqlite3

class AdvancedUserOperations:

  def __init__(self):

    self.conn = sqlite3.connect('user_database.db')

    self.cursor = self.conn.cursor()
    table = """ CREATE TABLE IF NOT EXISTS users (
            name TEXT,
                email TEXT,
                password TEXT,
                age INTEGER,
                gender TEXT,
                address TEXT
        ); """
 
    self.cursor.execute(table)

 

  def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
    user_sql = """
        INSERT INTO users (name, email, password, age, gender, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """
    user_values = (name, email, password, age, gender, address)
    self.cursor.execute(user_sql, user_values)
    self.conn.commit()    

 

  def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):
    user_sql = "SELECT * FROM users WHERE 1=1"
    user_values = []
    if min_age != None:
      user_sql += ' AND age >= ?'
      user_values.append(min_age)
    if max_age != None:
      user_sql += ' AND age <= ?'
      user_values.append(max_age)
    if gender != None:
      user_sql += ' AND gender = ?'
      user_values.append(gender)
    self.cursor.execute(user_sql, user_values)
    return self.cursor.fetchall()
 

  def update_user_profile(self, email, age=None, gender=None, address=None):
    user_sql = "UPDATE users SET"
    user_values = []
    if age != None:
      user_sql += ' age = ?,'
      user_values.append(age)
    if gender != None:
      user_sql += ' gender = ?,'
      user_values.append(gender)
    if address != None:
      user_sql += ' address = ?,'
      user_values.append(address)
    user_sql = user_sql.rstrip(',') + " WHERE email = ?"
    user_values.append(email)
    self.cursor.execute(user_sql, user_values)
    self.conn.commit()

 

  def delete_users_by_criteria(self, gender=None):
    user_sql = "DELETE FROM users WHERE 1=1"
    user_values = []
    if gender != None: 
      user_sql += ' AND gender = ?'
      user_values.append(gender)
    self.cursor.execute(user_sql, user_values)
    self.conn.commit()

 

  def __del__(self):

    self.conn.close()
