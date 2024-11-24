from flask import Flask, render_template, request, jsonify
import flasgger
from models import Book
from config import session


'''1. Зробити модель для книги
   2. Заповнити базу данних даними
   3. Реалізувати 5 ендпоінтів - get, put, path, delete, post
'''

app = Flask(__name__)

@app.post("/add-books")
def add_book():
    data = request.get_json()

    if not data.get("title"):
        return jsonify({"error": "Enter the title"})
    elif not data.get("author"):
        return jsonify({"error": "Enter the author"})
    elif not data.get("year"):
        return jsonify({"error": "Enter the year"})
    
    book = Book(**data)

    session.add(book)
    session.commit()

    return jsonify(book.model_dump()), 201


if __name__ == "__main__":
    app.run(debug=True)