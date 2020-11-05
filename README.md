# Key-Document Database in MongoDB

## 3 different databases

```
connect(alias='user-db-alias', db='user-db')
connect(alias='book-db-alias', db='book-db')
connect(alias='users-books-db-alias', db='users-books-db')

class User(Document):
    name = StringField()
    meta = {'db_alias': 'user-db-alias'}

class Book(Document):
    name = StringField()
    meta = {'db_alias': 'book-db-alias'}

class AuthorBooks(Document):
    author = ReferenceField(User)
    book = ReferenceField(Book)
    meta = {'db_alias': 'users-books-db-alias'}
 ```
