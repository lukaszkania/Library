from constants.API_URLS import GOOGLE_BOOKS_API
import requests
from books.models import Book
from author.models import Author
from industrie.models import Industrie

# Creating python dictionary based on single book object got from API
def create_book_dictionary_based_on_API(book_object_from_Api):
        book_dict = {}
        book_dict["title"] = book_object_from_Api["volumeInfo"].get("title", "Undefined")
        book_dict["authors"] = book_object_from_Api["volumeInfo"].get("authors", "Undefined")
        book_dict["industryIdentifiers"] = book_object_from_Api["volumeInfo"].get("industryIdentifiers", "Undefined")
        book_dict["publishedDate"] = book_object_from_Api["volumeInfo"].get("publishedDate", "Undefined") 
        book_dict["pageCount"] = book_object_from_Api["volumeInfo"].get("pageCount", 1) 
        book_dict["imageLinks"] = book_object_from_Api["volumeInfo"].get("imageLinks", "Undefined") 
        book_dict["language"] = book_object_from_Api["volumeInfo"].get("language", "Undefined") 
  
        return book_dict

# Handling object from API that have not thumbnails
def safe_adding_thumbnails_to_new_book_object(book_dict, kind_of_thumbnail, default="Undefined"):
    try:
        return book_dict["imageLinks"].get(kind_of_thumbnail, default)
    except AttributeError:
        return default

# Create new Book object based on python dict made from create_book_dictionary_based_on_API function and save it if there is not allready in db Book instance that have the same title
def create_book_object_based_on_book_dict_and_save_in_db(book_dict):
    try:
        object_allready_in_db = Book.objects.get(title=book_dict["title"])
        return object_allready_in_db
    except Book.DoesNotExist:
        new_book_object = Book(
            title = book_dict.get("title", "Undefined"),
            published_date = book_dict.get("publishedDate", "Undefined"),
            page_count = book_dict.get("pageCount", 1),
            language = book_dict.get("language", "Undefined"),
            small_thumbnail = safe_adding_thumbnails_to_new_book_object(book_dict, "smallThumbnail"),
            thumbnail = safe_adding_thumbnails_to_new_book_object(book_dict, "thumbnail")
        )
        new_book_object.save()
        return new_book_object

# Create new Author object based on python dict made from create_book_dictionary_based_on_API function and save it if there is not allready in db Author instance that have the same authorName
def create_author_object_based_on_book_dict_and_save_in_db(book_dict):
    authors_list = book_dict["authors"]
    for author in authors_list:
        try:
            object_allready_in_db = Author.objects.get(authorName=author)
            return object_allready_in_db
        except Author.DoesNotExist:
            new_author_object = Author(authorName=author)
            new_author_object.save()
            return new_author_object

# Add book objects to authors book_set's and book to authors_set's
def update_books_author_set_and_authors_book_set(book_object, author_object):
    book = Book.objects.get(title=book_object.title)
    author = Author.objects.get(authorName=author_object.authorName)
    author.book_set.add(book)
    book.author_set.add(author)

# Handling object from API that have not industries
def safe_adding_industries_to_new_industrie_object(industrie_dict, type_or_identifier, default="Undefined"):
    try:
        return industrie_dict.get(type_or_identifier, default)
    except AttributeError:
        return default

# Create new Industrie object based on python dict made from create_book_dictionary_based_on_API function and save it if there is not allready in db Industrie instance that have the same type_of_industrie
def create_industrie_object_based_on_book_dict_and_save_in_db(book_dict):
    industry_identifiers = book_dict["industryIdentifiers"]
    for industrie in industry_identifiers:
        industry_type = safe_adding_industries_to_new_industrie_object(industrie,"type", "Undefined") 
        industry_identifier = safe_adding_industries_to_new_industrie_object(industrie,"identifier", "Undefined") 
        try:
            object_allready_in_db = Industrie.objects.get(type_of_industrie=industry_type, identifier=industry_identifier)
            return object_allready_in_db
        except Industrie.DoesNotExist:
            new_industrie_object = Industrie(type_of_industrie=industry_type, identifier=industry_identifier)
            new_industrie_object.save()
            return new_industrie_object

# Add book objects to industrie released_books_set's and industrie to industries_set's
def update_books_industrie_set_and_industrie_book_set(book_object, industrie_object):
    book = Book.objects.get(title=book_object.title)
    industrie = Industrie.objects.get(type_of_industrie=industrie_object.type_of_industrie, identifier=industrie_object.identifier)
    industrie.book_set.add(book)
    book.industrie_set.add(industrie)

# Main function that handels importing books from api
def import_books_from_API(request, question, api_url=GOOGLE_BOOKS_API):
    response = requests.get(api_url + str(question))
    
    books_from_Api = response.json().get("items", "Error, probably missing query...")
    
    for book in books_from_Api:
        book_dict_created_basing_on_API = create_book_dictionary_based_on_API(book)
        book_object = create_book_object_based_on_book_dict_and_save_in_db(book_dict_created_basing_on_API)
        author_object = create_author_object_based_on_book_dict_and_save_in_db(book_dict_created_basing_on_API)
        industrie_object = create_industrie_object_based_on_book_dict_and_save_in_db(book_dict_created_basing_on_API)
        update_books_author_set_and_authors_book_set(book_object, author_object)
        update_books_industrie_set_and_industrie_book_set(book_object, industrie_object)
        
    
    
