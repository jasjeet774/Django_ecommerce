# Django E-commerce Website

This project is a simple e-commerce website built with Django and Tailwind CSS. It includes functionality for product listing, a shopping cart, and a checkout process.

## Features

- **Product Listing:** View all available products.
- **Product Detail:** View detailed information about a product.
- **Shopping Cart:** Add products to the cart, view the cart, and update quantities.
- **Checkout:** Proceed to checkout and complete the order.

## Prerequisites

- Python 3.x
- Django 3.x or later
- Tailwind CSS (via CDN)
   
## Tailwind CSS
This project uses Tailwind CSS via CDN. The CDN link is included in the base.html template:

    ```bash
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jasjeet774/Django_ecommerce.git
   cd Django_ecommerce

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  
    # On Windows, use 
    env\Scripts\activate


3. **Install dependencies::**
    ```bash
    pip install django

4. **Create and apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
   
6. **Run the development server:**
    ```bash
    python manage.py runserver

7. **Open your browser and go to:**
    ```bash
    http://127.0.0.1:8000/
 