from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from database import get_db_connection

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        #role = get_user_role(session['username'])
        #if role == 'Citizen':
            #return redirect(url_for('user_menu'))
        #elif role == 'Admin':
        return redirect(url_for('admin_menu'))
    
    return render_template('loggedOut.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['username']
        last_name_candidate = request.form['password']
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT LastName FROM personnel WHERE FirstName = %s", (first_name,))
                result = cursor.fetchone()
                
                if result and result['LastName'] == last_name_candidate:
                    session['username'] = first_name
                    cursor.execute("SELECT FirstName, ContactInfo, RankLevel FROM personnel WHERE FirstName = %s", (first_name,))
                    user_info = cursor.fetchone()

                    session['first_name'] = user_info["FirstName"]
                    session['user_mail'] = user_info["ContactInfo"]
                    session['role'] = user_info["RankLevel"]
                    return redirect(url_for('index'))
                else:
                    return render_template('invalidLogin.html')
        finally:
            connection.close()
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('first_name', None)
    session.pop('user_mail', None)
    session.pop('role', None)
    return render_template('loggedOut.html')

@app.route('/user_menu')
def user_menu():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('userMenu.html', first_name=session.get('first_name'))

@app.route('/admin_menu')
def admin_menu():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('adminMenu.html', first_name=session.get('first_name'))

@app.route('/admin/view_table/<table_name>')
def view_table(table_name):
    #if 'username' not in session or session.get('role') != 'Admin':
        #return redirect(url_for('login'))
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
    finally:
        connection.close()

    return render_template('viewTable.html', table_name=table_name, columns=columns, rows=rows)

@app.route('/admin/add_entry/<table_name>', methods=['GET', 'POST'])
def add_entry(table_name):
    #if 'username' not in session or session.get('role') != 'Admin':
        #return redirect(url_for('login'))
    
    if request.method == 'POST':
        form_data = request.form.to_dict()
        columns = ', '.join(form_data.keys())
        placeholders = ', '.join(['%s'] * len(form_data))
        values = tuple(form_data.values())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
            connection.commit()
        finally:
            connection.close()
        
        return redirect(url_for('view_table', table_name=table_name))
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
    finally:
        connection.close()
    
    return render_template('addEntry.html', table_name=table_name, columns=columns)

def get_user_role(username):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT RankLevel FROM personnel WHERE FirstName = %s", (username,))
            result = cursor.fetchone()
            if result:
                return result['RankLevel']
    finally:
        connection.close()
    return None

if __name__ == '__main__':
    app.run(port=8000, debug=True)
