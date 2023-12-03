import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random

from clients.models import Client


def make_people(number_of_people):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(number_of_people):
        cpf = CPF()
        name = fake.name()
        email = f"{name.lower()}@{fake.free_email_domain()}"
        email = email.replace(" ", '')
        cpf = cpf.generate()
        rg = f"{random.randrange(10, 99)}{random.randrange(100, 999)}{random.randrange(100, 999)}{random.randrange(0, 9)}"
        phone = f"{random.randrange(10,99)} 9{random.randrange(4000, 9999)}-{random.randrange(4000, 9999)}"
        active = random.choice([True, False])
        p = Client(name=name, email=email, cpf=cpf, rg=rg, phone=phone, active=active)
        p.save()
    

make_people(50)
print("Success!!")