def connectdb():
    '''Establish DB connection'''
    conn = mariadb.connect(
        host='127.0.0.1',
        port=3306,
        user='cs340',
        password='collector',
        database='cartridge_collector'
    )
    return conn

def get_cursor(connection):
    '''Get cursor from db connection'''
    cur = connection.cursor()
    return cur

def execute_query(db_connection = None, query = None, query_params = ()):
    '''
    executes a given SQL query on the given db connection and returns a Cursor object
    db_connection: a MySQLdb connection object created by connect_to_database()
    query: string containing SQL query
    returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
    You need to run .fetchall() or .fetchone() on that object to actually acccess the results.
    '''

    if db_connection is None:
        print("Connecting to database ...")
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params))
    cursor = db_connection.cursor()
    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor

#CREATE

def insert(table_name, fields, values):
    query = 'INSERT INTO ' +  table_name + ' (' + ', '.join(fields) +') VALUES (' + ', '.join(values) + ')'
    conn = connectdb()
    cur = get_cursor(conn)
    cur.execute(query)
    conn.commit()
    conn.close()
    return cur


def add_user():
    if request.method == 'GET':
        return view_users()

    elif request.method == 'POST':
        user_id = request.form['user_id']
        email = request.form['email']
        screen_name  = request.form['screen_name']
        country_code = request.form['country_code']

        query = 'INSERT INTO users (user_id, email, screen_name, country_code) VALUES (%s,%s,%s,%s)'
        data = (user_id, email, screen_name, country_code)
        execute_query(conn, query, data)
        return ('User added!')

def add_game_to_user_collection():
    if request.method == 'GET':
        return view_user_collection()

    elif request.method == 'POST':
        user_id = request.form['user_id']
        game_id = request.form['game_id']

        query = 'INSERT INTO collection (user_id, game_id) VALUES (%s,%s)'
        data = (user_id, game_id)
        execute_query(conn, query, data)
        return ('Game added!')

def add_game_to_user_wishlist():
    if request.method == 'GET':
        return view_user_wishlist()

    elif request.method == 'POST':
        user_id = request.form['user_id']
        game_id = request.form['game_id']

        query = 'INSERT INTO wishes (user_id, game_id) VALUES (%s,%s)'
        data = (user_id, game_id)
        execute_query(conn, query, data)
        return ('Game added to wishlist!')

def add_game_review():
    if request.method == 'GET':
        return view_game_reviews()

    elif request.method == 'POST':
        user_id = request.form['user_id']
        game_id = request.form['game_id']
        rating_value = request.form['rating_value']
        rating_comment = request.form['rating_comment']

        query = 'INSERT INTO ratings (user_id, game_id, rating_value, rating_comment)  VALUES (%s,%s,%s,%s)'
        data = (user_id, game_id, rating_value, rating_comment)
        execute_query(conn, query, data)
        return ('Review submitted!')


#READ
def view_users():
    query = 'SELECT * from users;'
    result = execute_query(conn, query)
    print(result)

def view_user_collection(user_id):
    query = 'SELECT %s from collections;'
    result = execute_query(conn, query)
    print(result)

def view_user_reviews(user_id):
    query = 'SELECT %s FROM ratings;'
    result = execute_query(conn, query)
    print(result)

def view_user_wishlist(user_id):
    query = 'SELECT %s from wishes;'
    result = execute_query(conn, query)
    print(result)

def view_all_games():
    query = 'SELECT * from games;'
    result = execute_query(conn, query)
    print(result)

def view_users_that_have_game(game_id):
    query = 'SELECT %s FROM collection;'
    result = execute_query(conn, query)
    print(result)

def view_game_reviews(game_id):
    query = 'SELECT %s FROM ratings;'
    result = execute_query(conn, query)
    print(result)

