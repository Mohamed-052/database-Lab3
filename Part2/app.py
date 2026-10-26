from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="19404", 
        database="library_db"
    )
    return conn

# Home Route (Display Books & Authors)
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT b.book_id, b.title, b.price, b.cover_image, 
               a.name AS author_name, a.country, a.photo 
        FROM BOOK b JOIN AUTHOR a ON b.author_id = a.author_id
    """
    cursor.execute(query)
    books = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

# Add Book Route (With Image Upload Bonus)
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        price = request.form['price']
        author_id = request.form['author_id']
        author_name = request.form.get('author_name', 'Unknown')
        country = request.form.get('country', 'Unknown')
        
        upload_folder = os.path.join('static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        
        # Handle Cover Image
        cover_image = ""
        cover_file = request.files.get('cover_image')
        if cover_file and cover_file.filename != '':
            cover_path = os.path.join(upload_folder, cover_file.filename)
            cover_file.save(cover_path)
            cover_image = cover_path.replace('\\', '/')

        # Handle Author Photo
        author_photo = ""
        photo_file = request.files.get('author_photo')
        if photo_file and photo_file.filename != '':
            photo_path = os.path.join(upload_folder, photo_file.filename)
            photo_file.save(photo_path)
            author_photo = photo_path.replace('\\', '/')
            
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insert or update author first
        cursor.execute("""
            INSERT INTO AUTHOR (author_id, name, country, photo) 
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=%s, country=%s, photo=COALESCE(NULLIF(%s, ''), photo)
        """, (author_id, author_name, country, author_photo, author_name, country, author_photo))
        
        # Insert book
        cursor.execute("""
            INSERT INTO BOOK (book_id, title, price, author_id, cover_image) 
            VALUES (%s, %s, %s, %s, %s)
        """, (book_id, title, price, author_id, cover_image))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
        
    return render_template('add_book.html')

# Delete Book Route
@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM BOOK WHERE book_id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)