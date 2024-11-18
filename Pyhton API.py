# app.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookstore"  # Change as needed
mongo = PyMongo(app)

# CREATE - Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    try:
        # Get the data from the request
        book_name = request.json['book_name']
        author = request.json['author']
        publisher = request.json['publisher']

        # Insert into the MongoDB 'books' collection
        book = {
            'book_name': book_name,
            'author': author,
            'publisher': publisher
        }

        result = mongo.db.books.insert_one(book)
        
        # Return the created book with its ID
        return jsonify({
            'id': str(result.inserted_id),
            'book_name': book_name,
            'author': author,
            'publisher': publisher
        }), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 400


# READ - Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        books = mongo.db.books.find()
        # Convert books to a list of dictionaries
        books_list = [{"id": str(book["_id"]), "book_name": book["book_name"], "author": book["author"], "publisher": book["publisher"]} for book in books]
        return jsonify(books_list), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# READ - Get a book by ID
@app.route('/books/<id>', methods=['GET'])
def get_book_by_id(id):
    try:
        book = mongo.db.books.find_one({"_id": ObjectId(id)})
        if book:
            return jsonify({
                "id": str(book["_id"]),
                "book_name": book["book_name"],
                "author": book["author"],
                "publisher": book["publisher"]
            }), 200
        else:
            return jsonify({"message": "Book not found"}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# UPDATE - Update a book by ID
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    try:
        # Get the data from the request
        book_name = request.json.get('book_name')
        author = request.json.get('author')
        publisher = request.json.get('publisher')

        # Update the book in MongoDB
        updated_book = {}
        if book_name:
            updated_book['book_name'] = book_name
        if author:
            updated_book['author'] = author
        if publisher:
            updated_book['publisher'] = publisher

        result = mongo.db.books.update_one({"_id": ObjectId(id)}, {"$set": updated_book})

        if result.matched_count == 0:
            return jsonify({"message": "Book not found"}), 404

        return jsonify({"message": "Book updated successfully"}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# DELETE - Delete a book by ID
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        # Delete the book from MongoDB
        result = mongo.db.books.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({"message": "Book not found"}), 404

        return jsonify({"message": "Book deleted successfully"}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
