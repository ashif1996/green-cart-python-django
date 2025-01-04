# 🛒 Green Cart - Fresh Vegetables Online  
An e-commerce application for buying fresh vegetables online, built with **Python** and **Django**.

This project is designed to provide users with a seamless online shopping experience for fresh vegetables, featuring functionalities like user registration, login, product browsing, cart management, and checkout.

## 🚀 Features  
- **User Authentication**:  
  - Register, log in, and manage profiles.  
- **Product Management**:  
  - View a variety of fresh vegetables with details.  
- **Cart and Checkout**:  
  - Add items to the cart, update quantities, and proceed to checkout.  
- **Address Management**:  
  - Save, update, and manage delivery addresses.  
- **Contact Page**:  
  - A page for users to contact the support team.    

## 🛠️ Tech Stack  
- **Backend**: Python (Django Framework)  
- **Frontend**: HTML, CSS, Bootstrap, JavaScript  
- **Database**: SQLite  

## 📂 Project Structure  

```plaintext
green-cart-python-django/
├── .idea/                 # IDE configuration files
├── GreenCart/             # Django project configuration
├── cart/                  # Cart app
│   ├── migrations/        # Database migrations for the cart
│   ├── templates/         # Cart-specific templates
│   │   ├── cart.html      # Cart page
│   │   └── checkout.html  # Checkout page
│   ├── __init__.py        # Cart app initialization
│   ├── admin.py           # Admin panel configuration for cart
│   ├── apps.py            # App configuration
│   ├── models.py          # Models for cart
│   ├── tests.py           # Unit tests for cart
│   ├── urls.py            # URL routing for cart
│   └── views.py           # Views for cart
├── members/               # User authentication and profile management
│   ├── migrations/        # Database migrations for members
│   ├── templates/         # Member-specific templates
│   │   ├── login.html     # Login page
│   │   ├── profile.html   # User profile page
│   │   └── registration.html # Registration page
│   ├── __init__.py        # Members app initialization
│   ├── admin.py           # Admin panel configuration for members
│   ├── apps.py            # App configuration
│   ├── models.py          # Models for members
│   ├── tests.py           # Unit tests for members
│   ├── urls.py            # URL routing for members
│   └── views.py           # Views for members
├── static/                # Static files for the project
│   ├── css/               # CSS files
│   │   ├── bootstrap.min.css # Bootstrap styles
│   │   ├── flaticon.css   # Custom icon styles
│   │   ├── owl.carousel.min.css # Carousel styles
│   │   ├── style.css      # General styles
│   │   └── style1.css     # Additional styles
│   ├── images/            # Images for the website
│   └── js/                # JavaScript files
│       ├── all.min.js     # Minified JavaScript for features
│       ├── myscript.js    # Custom scripts
│       └── owl.carousel.min.js # Carousel script
├── store/                 # Main app for product display and shopping
│   ├── migrations/        # Database migrations for store
│   ├── templates/         # Store-specific templates
│   │   ├── about.html     # About page
│   │   ├── add_address.html # Address management page
│   │   ├── contact.html   # Contact page
│   │   ├── home.html      # Home page
│   │   ├── main.html      # Main template layout
│   │   ├── messages.html  # Messages/notifications page
│   │   └── store.html     # Store/product listing page
│   ├── __init__.py        # Store app initialization
│   ├── admin.py           # Admin panel configuration for store
│   ├── apps.py            # App configuration
│   ├── forms.py           # Forms for store
│   ├── models.py          # Models for store
│   ├── tests.py           # Unit tests for store
│   ├── urls.py            # URL routing for store
│   └── views.py           # Views for store
├── db.sqlite3             # SQLite database
├── manage.py              # Django's management script
```

## 🔧 Setup and Installation  

### Prerequisites  
- Python 3.8+  
- Django 4.0+  
- pip (Python package manager)  

### Steps  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/green-cart-python-django.git
   cd green-cart-python-django
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the server**:  
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/` to view the app.

## 📜 Usage  

- **Home Page**: Browse available fresh vegetables.  
- **Cart Management**: Add, update, and remove items in your cart.  
- **Checkout**: Provide your delivery address and confirm your purchase.  
- **Admin Panel**: Manage products and orders.  

## 🌱 Learning Outcomes  

- Understanding the Django framework and its core features.  
- Building reusable and scalable applications using the MVC architecture.  
- Implementing authentication and session management.  
- Styling using CSS frameworks like Bootstrap.  

## 📜 License  

This project is licensed under the **MIT License**. Feel free to use and modify it as per your requirements.

## 🌟 Acknowledgements  

Special thanks to the Django community for their excellent documentation and tutorials.  

Happy Coding! 😊