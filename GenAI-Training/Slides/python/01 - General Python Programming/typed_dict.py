from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

# Creating an instance of the TypedDict
my_movie: Movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8
}

# Accessing values
print(my_movie["title"])  # Output: Inception
print(my_movie["year"])   # Output: 2010
print(my_movie["rating"]) # Output: 8.8

# Modifying values
my_movie['rating'] = 9

def process_movie(mov: Movie) -> None:
    """Prints movie details."""
    print(f'Title: {mov["title"]}')
    print(f'Year: {mov["year"]}')
    print(f"Rating: {mov['rating']}")

# Correct usage
amovie = {'title': 'Alice', 'year': 1990, 'rating': 8.5}
process_movie(amovie)

# Incorrect usage (missing required keys)
m = {'title': 'Alice'}
# process_movie(m)  # Type error

# Defining a TypedDict with optional keys
class Employee(TypedDict, total=False):
    name: str
    age: int
    department: str

# Creating an instance with optional keys
employee: Employee = {
    "name": "Alice"
}

# Accessing values
print(employee.get("name"))  # Output: Alice
print(employee.get("age", "N/A"))  # Output: N/A (since age is not defined)

# Nested TypedDict
class Address(TypedDict):
    street: str
    city: str
    zip: str

class User(TypedDict):
    username: str
    email: str
    address: Address

# Creating an instance with nested Address
user: User = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "12345"
    }
}

# Accessing nested values
print(user["address"]["city"])  # Output: NYC
