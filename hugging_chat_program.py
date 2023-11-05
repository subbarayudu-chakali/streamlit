import streamlit as st
import streamlit.cookiemanager as cookiemanager
from streamlit.auth import Authenticator
from streamlit.errors import StreamlitError
import sqlite3
# import Authenticator

# Set up authentication
authenticator = Authenticator()

# Create a SQLite database
conn = sqlite3.connect('userdb.db')
cursor = conn.cursor()

# Define schema
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, password HASH NOT NULL)')

# Create table
cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('admin', 'admin@example.com', b'$2b$12$YEah6LpI8TK5tOqKjNyWuue5iV2X/C9RLnQW2LfLpQW2LfLpQ=='))
cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('user', 'user@example.com', b'$2b$12$YEah6LpI8TK5tOqKjNyWuue5iV2X/C9RLnQW2LfLpQW2LfLpQ=='))

# Commit changes
conn.commit()

# Close connection
conn.close()

# Define routes
@authenticator.route('/login')
def login():
    return st.html('<form method="post">Login</br><input type="text" name="username">
    <input type="password" name="password">
    <button>Log in</button></form>')

@authenticator.route('/signup')
def signup():
    return st.html('<form method="post">Sign Up</br><input type="text" name="username">
    <input type="email" name="email">
    <input type="password" name="password">
    <button>Create Account</button></form>')

@authenticator.route('/protected')
def protected():
    user = authenticator.get_user()
    if user is None:
        raise StreamlitError("You must log in first")
    return st.html('Welcome, {}'.format(user['username']))

# Run Streamlit app
if __name__