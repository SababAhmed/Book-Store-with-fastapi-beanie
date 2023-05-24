# Part 1: Basic System Structure, CRUD Operations and Model Interactions

## Models

### 1. Bcooks
- id: ObjectId (unique)
- title: str
- author_id: ObjectId (foreign key linked to Author)
- publication_year: int
- isbn: str (unique)
- stock: int

### 2. Author
- id: ObjectId (unique)
- name: str
- dob: datetime
- nationality: str

## Endpoints
### 1. Book
- GET /books: Retrieve all books
- POST /books: Create a new book
- GET /books/{id}: Retrieve a book by its ID
- PUT /books/{id}: Update a book by its ID
- DELETE /books/{id}: Delete a book by its ID
### 2. Author
- GET /authors: Retrieve all authors
- POST /authors: Create a new author
- GET /authors/{id}: Retrieve an author by their ID
- PUT /authors/{id}: Update an author by their ID
- DELETE /authors/{id}: Delete an author by their ID
### 3. Interaction
- GET /authors/{id}/books: Retrieve all books from a specific author
- GET /books/{id}/author: Retrieve the author of a specific book
