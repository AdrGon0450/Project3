from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__)

# Database connection details
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'DBpokedex'

# Function to connect to PostgreSQL database
connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)



# Route to handle search queries
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    # Construct SQL query
    sql_query = (f"SELECT * FROM pokemon_stats WHERE name ILIKE '%{query}%'")

    # Execute SQL query
    cursor = connection.cursor()
    cursor.execute(sql_query)
    search_results = cursor.fetchall()
    cursor.close()


    # Print search results in the terminal for debugging
    print("Search Results:")
    for row in search_results:
        print(row)
        
    results = [{'Name': row[1], 'Number': row[0], 'Type_1': row[2], 'Type_2': row[3], 'HP': row[4], 'Attack': row[5], 'Defense': row[6], 'Sp.Attack': row[7], 'Sp.Defense': row[8], 'Speed': row[9]} for row in search_results]
    
    # Render the template 'searchpage.html' and pass the results to it
    return render_template('searchpage.html', results=results)

if __name__ == '__main__':
    app.run()
