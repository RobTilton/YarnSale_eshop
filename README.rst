===========================
Your E-Commerce Website
===========================
.. image:: static/images/YardSale_002.png
    :alt: Homepage
    
.. image:: static/images/YardSale_001.png
    :alt: Shop page
Overview
========
My Django project is a simple e-commerce website designed to showcase my skills
and understanding in various technologies, including Django, Python, CSS, HTML,
and Django REST Framework. The primary goal of this project is to demonstrate 
my capabilities in account creation, database design, API calls, and effective
use of version control systems like Git. 

I've employed Faker to create a script that populates the database with fake 
product data, simulating a real-world application and demonstrating the 
database's functionality. This project serves as a practical example of my 
work for potential employers and fellow developers, highlighting the challenges
I faced and the solutions I implemented. It's a testament to my learning journey 
and a platform where I've applied my theoretical knowledge in a practical setting.


Technical Details
=================
- **Django Version**: 5.0.1
- **Key Dependencies**: Django REST Framework 3.14.0, Faker 22.2.0, Pillow 10.2.0.
- **Database**: SQLite (default), configurable for other databases.
- **Languages**: Python, HTML, CSS.

Dev Environment Setup
=====================

1. **Clone the Repository**: Fork the repository and clone your fork to your local machine. 
   To do this, open your RUN box (Windows + R), then enter 'cmd'. 
   Navigate to the directory you want to use for the clone and enter the command:

   .. code-block:: bash

       git clone https://github.com/your-username/repository-name.git

   Replace the URL with the one to your fork of this repo.

2. **Set Up a Virtual Environment**: Create and activate a virtual environment in the project directory:

   .. code-block:: bash

       # On Windows
       python -m venv venv
       .\\venv\\Scripts\\activate

       # On Unix or MacOS
       python3 -m venv venv
       source venv/bin/activate

3. **Install Dependencies**: Install the required packages from `requirements.txt`:

   .. code-block:: bash

       pip install -r requirements.txt

4. **Running the Application**: Start the Django development server:

   .. code-block:: bash

       python manage.py runserver

Usage Instructions
==================

Account Creation
----------------
To begin exploring the features of the website, users must first create an account. The account creation process is straightforward:

- Navigate to the Sign-Up page from the homepage.
- Fill in the required fields with your information.
- Submit the form to create your account.

Upon successful account creation, users can log in, browse products, and add them to their cart.

Browsing and Searching Products
-------------------------------
The shop is designed to enhance user experience with several search and filter options:

- **Color**: Users can filter products based on their color preferences from the choices of Blue, Red, Green, Yellow, and Purple.
- **Length**: For products where length is applicable, users can search for 100, 200, and 300 length yarns.
- **Weight**: For products where weight is applicable, users can search for Light, Medium, and Heavy yarn weight.
- **Material**: A key search feature for users interested in products made from specific materials.
- **By Name**: If a user knows exactly what they are looking for, a simple name search is available.

Each product is presented in a card format, providing essential information at a glance. Users can click on a 
product card to view more detailed attributes of each item.

Shopping Cart
-------------
The shopping cart is an integral part of the e-commerce experience:

- **Adding Products**: When browsing, users can add products to their cart with a single click.
- **Viewing the Cart**: The cart page summarizes all items a user plans to purchase, allowing for review before proceeding.
- **Removing Items**: Users have the option to remove items from the cart if they change their mind.

Checkout Process
----------------
While the website simulates a complete e-commerce experience, the checkout process is not implemented, 
as this platform serves as a demonstration of web development skills and is not intended for actual transactions.


Features
========
- **Database Design**: Efficiently structured relational database for storing user data, product information, and transaction records.
- **RESTful API**: API endpoints for handling CRUD operations on products, users, and orders, demonstrating the use of Django REST Framework.
- **Security**: Implementation of security best practices, including password hashing and user authentication. 
- **Advanced Search**: Users can search for products by keywords.
- **Data Population**: Use of Faker library to generate realistic product data for demonstration purposes.
- **Image Handling**: Use of Pillow library to seamlessly handle images for products.
  
Contact Information
===================
If you wish to ask me about anything seen here, email me at RobertJTilon89@Gmail.com
