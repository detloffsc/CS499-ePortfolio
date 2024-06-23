from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

def fetch_data():
    # Connect to SQLite database
    connection = sqlite3.connect('mazedata.db')
    cursor = connection.cursor()
    
    # Retrieve data from the table
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    
    # Close the connection
    connection.close()
    
    return rows

def generate_html_table(data):
    html = '<table border="1">'
    html += '<tr><th>ID</th><th>Epochs</th><th>Number of Mazes</th><th>H</th><th>W</th></tr>'
    
    for row in data:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>'
    
    html += '</table>'
    return html

@app.route('/')
def index():
    data = fetch_data()
    html_table = generate_html_table(data)
    return render_template_string(f'''
        <html>
            <head>
                <title>SQLite Table</title>
            </head>
            <body>
                <h1>Maze Data</h1>
                {html_table}
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)