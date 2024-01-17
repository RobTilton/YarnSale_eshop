import os
import django
import random
from faker import Faker

# Setting the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YarnSale.settings")
django.setup()

from django.contrib.auth.models import User
from shop.models import Product, ProductAttribute

fake = Faker()

def create_products(n):
    # Predefined attribute values for yarn products
    attribute_values = {
        'Color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple'],
        'Material': ['Cotton', 'Wool', 'Acrylic', 'Silk'],
        'Weight': ['Light', 'Medium', 'Heavy'],
        'Length': ['100m', '200m', '300m']
    }

    for _ in range(n):
        name = fake.word().title() + ' Yarn'
        description = fake.text()
        price = random.randint(10, 1000)
        product = Product.objects.create(name=name, description=description, price=price)

        for attr_name, values in attribute_values.items():
            value = random.choice(values)  # Randomly select from predefined values
            ProductAttribute.objects.create(
                product=product,
                name=attr_name,
                value=value
            )

create_products(25)