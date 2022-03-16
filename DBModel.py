import mariadb

class DBModelException(Exception):
    '''Exception handler'''
    pass

class DBModel():
    '''Handle db interactions'''
    def __init__(self) -> None:
        self._conn = None
        self._cur = None
        self._host = '127.0.0.1'
        self._port = 3306
        self._user = 'cs340'
        self._pass = 'collector'
        self._db_name = 'cartridge_collector'

    def _connect(self):
        '''Handle connections'''
        conn = mariadb.connect(
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._pass,
            database=self._db_name
        )
        print('Connected to mariadb! Database: ' + self._db_name)
        return conn

    def _get_cursor(self, connection):
        '''Get cursor from db connection'''
        cur = connection.cursor()
        return cur

    def _verify_values(self, values):
        injections = ['SELECT', 'INSERT', 'DROP', 'DELETE']
        for value in values:
            for sql in injections:
                if sql in value.upper():
                    return False
        return True
     
    def _print_query(self, query):
        '''Print query to console for CLI/testing purposes'''
        print('Query submitted:' + query)

    def _execute(self, query):
        '''Execute query'''
        connection = self._connect()
        cursor = self._get_cursor(connection)
        rows = []
        try:
            cursor.execute(query)  
        except:
            print("Query execution failed!")
            self._close(connection)
            return {'error': 'Query execution failed!'}
            
        print("Query executed!")
        if query.__contains__('SELECT'):
            rows = cursor.fetchall()
            print(rows)
            
        connection.commit()
        self._close(connection)
        return rows    

    def _close(self, connection):
        '''Close database connection'''
        print ('Closing connection')
        connection.close()

    # Public Methods
    def create(self, table_name, fields, values):
        '''Create new entry in <table_name> with given fields and values.'''
        if self._verify_values(values) == False:
            raise DBModelException()

        query = 'INSERT INTO ' +  table_name + ' (' + ', '.join(fields) +') VALUES (' + ', '.join(values) + ')' + ';'
        self._print_query(query)
        res = self._execute(query)
        if len(res) == 0:
            return {'error':'no rows added'}
        return {'success':'{} rows have been inserted'.format(str(len(res)))}
        
    def read(self, table_name, fields=None, filter=None):
        '''Get from <table_name> matching filter specificiations or all entries.'''
        if filter is None:   # SELECT ALL   
            query = 'SELECT * FROM ' + table_name + ';'
        else:
            query = 'SELECT ' +  ', '.join(fields) + ' FROM ' + table_name + ' WHERE ' + filter + ';'

        self._print_query(query)
        res = self._execute(query)
        return res

    def update(self, table_name, updated_values, filter):
        '''Update table in given fields with given values.'''
        if self._verify_values(updated_values) == False:
            raise DBModelException()
        if filter is None: 
            query = 'UPDATE ' + table_name + ' SET ' + updated_values
        else:
            query = 'UPDATE ' + table_name + ' SET ' + updated_values + ' WHERE ' + filter + ';'

        self._print_query(query)
        res = self._execute(query)
        if len(res) == 0:
            return {'error':'no rows updated'}
        return {'success':'{} rows have been updated'.format(str(len(res)))}

    def delete(self, table_name, filter):
        if len(filter.keys()) != 1:     
            raise DBModelException()

        filter_string = list(filter.keys())[0] + '=' + filter.keys
        query = 'DELETE FROM ' +  table_name + ' WHERE ' + filter + ';'
        self._print_query(query)
        res = self._execute(query)
        if len(res) == 0:
            return {'error':'no rows deleted'}
        return {'success':'{} rows have been deleted'.format(str(len(res)))}




# def connect_db():
#     '''Establish DB connection'''
#     conn = mariadb.connect(
#         host='127.0.0.1',
#         port=3306,
#         user='cs340',
#         password='collector',
#         database='cartridge_collector'
#     )
#     print('Connected to mariadb!')
#     return conn

# def get_cursor(connection):
#     '''Get cursor from db connection'''
#     cur = connection.cursor()
#     return cur

# def close_db(conn):
#     '''Close db connection'''
#     conn.close()

# def print_query(query):
#     '''Print query to console for CLI/testing purposes.'''
#     print('Query submitted:')



# def create(table_name, fields, values):
#     query = 'INSERT INTO ' +  table_name + ' (' + ', '.join(fields) +') VALUES (' + ', '.join(values) + ')'
#     print('Query submitted: ' + query)
#     conn = connectdb()
#     cur = get_cursor(conn)
#     cur.execute(query)
#     response = cur.fetchone()
#     print()
#     conn.commit()
#     conn.close()
#     return response

# def read(table_name, filter=None):
#     '''Return table with filter appleid. Filter is a tuple of a pair, attribute and value to be matched in query'''
#     # Construct query
#     query = 'SELECT * FROM ' + table_name
#     if filter != None:
#         query += ' WHERE ' + filter[0] + '=' + filter[1]    
#     query += ';'
#     print(query)
#     conn = connectdb()
#     cur = get_cursor(conn)
#     cur.execute(query)
#     results = cur.fetchall()
#     print(results)
#     return results

# def update(table_name, fields, values):
#     pass

# def delete(table_name, filter):
#     pass

# def execute_query(db_connection = None, query = None, query_params = ()):
#     '''
#     executes a given SQL query on the given db connection and returns a Cursor object
#     db_connection: a MySQLdb connection object created by connect_to_database()
#     query: string containing SQL query
#     returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
#     You need to run .fetchall() or .fetchone() on that object to actually acccess the results.
#     '''

#     if db_connection is None:
#         print("Connecting to database ...")
#         return None

#     if query is None or len(query.strip()) == 0:
#         print("query is empty! Please pass a SQL query in query")
#         return None

#     print("Executing %s with %s" % (query, query_params))
#     cursor = db_connection.cursor()
#     cursor.execute(query, query_params)
#     db_connection.commit()
#     return cursor

# #CREATE

# def add_user():
#     if request.method == 'GET':
#         return view_users()

#     elif request.method == 'POST':
#         user_id = request.form['user_id']
#         email = request.form['email']
#         screen_name  = request.form['screen_name']
#         country_code = request.form['country_code']

#         query = 'INSERT INTO users (user_id, email, screen_name, country_code) VALUES (%s,%s,%s,%s)'
#         data = (user_id, email, screen_name, country_code)
#         execute_query(conn, query, data)
#         return ('User added!')

# def add_game_to_user_collection():
#     if request.method == 'GET':
#         return view_user_collection()

#     elif request.method == 'POST':
#         user_id = request.form['user_id']
#         game_id = request.form['game_id']

#         query = 'INSERT INTO collection (user_id, game_id) VALUES (%s,%s)'
#         data = (user_id, game_id)
#         execute_query(conn, query, data)
#         return ('Game added!')

# def add_game_to_user_wishlist():
#     if request.method == 'GET':
#         return view_user_wishlist()

#     elif request.method == 'POST':
#         user_id = request.form['user_id']
#         game_id = request.form['game_id']

#         query = 'INSERT INTO wishes (user_id, game_id) VALUES (%s,%s)'
#         data = (user_id, game_id)
#         execute_query(conn, query, data)
#         return ('Game added to wishlist!')

# def add_game_review():
#     if request.method == 'GET':
#         return view_game_reviews()

#     elif request.method == 'POST':
#         user_id = request.form['user_id']
#         game_id = request.form['game_id']
#         rating_value = request.form['rating_value']
#         rating_comment = request.form['rating_comment']

#         query = 'INSERT INTO ratings (user_id, game_id, rating_value, rating_comment)  VALUES (%s,%s,%s,%s)'
#         data = (user_id, game_id, rating_value, rating_comment)
#         execute_query(conn, query, data)
#         return ('Review submitted!')


# #READ

# def view_users():
#     query = 'SELECT * from users;'
#     result = execute_query(conn, query)
#     print(result)

# def view_user_collection(user_id):
#     query = 'SELECT %s from collections;'
#     result = execute_query(conn, query)
#     print(result)

# def view_user_reviews(user_id):
#     query = 'SELECT %s FROM ratings;'
#     result = execute_query(conn, query)
#     print(result)

# def view_user_wishlist(user_id):
#     query = 'SELECT %s from wishes;'
#     result = execute_query(conn, query)
#     print(result)

# def view_all_games():
#     query = 'SELECT * from games;'
#     result = execute_query(conn, query)
#     print(result)

# def view_users_that_have_game(game_id):
#     query = 'SELECT %s FROM collection;'
#     result = execute_query(conn, query)
#     print(result)

# def view_game_reviews(game_id):
#     query = 'SELECT %s FROM ratings;'
#     result = execute_query(conn, query)
#     print(result)

