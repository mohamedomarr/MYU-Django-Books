import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from book.models import Author, Book, Review

def create_author(n):
    fake = Faker()
    for x in range(n):
        Author.objects.create(
            name = fake.name(),
            birth_date = fake.date(),
            biography = fake.text()
        )
        
def create_book(n):
    fake = Faker()
    for x in range(n):
        Book.objects.create(
            author = Author.objects.all().order_by('?')[0],
            title = fake.name(),
            publication_date = fake.date(),
            price = random.randint(1, 200),
            genre = fake.text()
        )
        
def create_review(n):
    fake = Faker()
    for x in range(n):
        Review.objects.create(
            book = Book.objects.all().order_by('?')[0],
            reviewer_name = fake.name(),
            content = fake.text(),
            rating = random.randint(1, 5)
        )
        

create_author(44)
create_book(99)
create_review(2999)