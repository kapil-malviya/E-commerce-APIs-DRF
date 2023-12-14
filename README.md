# E-Commerce API Documentation

This document provides an overview of the E-Commerce API built using Django Rest Framework to manage customers, orders, and products.

## Table of Contents
1. [Database Structure](#database-structure)
2. [API Endpoints](#api-endpoints)
3. [Validations](#validations)
4. [Example Payload for any API](#example-payload-for-any-api)
5. [Requirements](#requirements)
6. [Getting Started](#getting-started)
   - [Creating a Virtual Environment](#creating-a-virtual-environment)
   - [Installation](#installation)
   - [Usage](#usage)

## Database Structure

### Customer Model
- **Fields:**
  - id (AutoField)
  - name (CharField)
  - contact_number (CharField)
  - email (EmailField)

### Product Model
- **Fields:**
  - id (AutoField)
  - name (CharField)
  - weight (DecimalField)

### Order Model
- **Fields:**
  - id (AutoField)
  - order_number (CharField) (Auto-generated with prefix ORD and incremental numbering)
  - customer (ForeignKey to Customer)
  - order_date (DateField)
  - address (CharField)

### Order Item Model
- **Fields:**
  - id (AutoField)
  - order (ForeignKey to Order)
  - product (ForeignKey to Product)
  - quantity (PositiveIntegerField)


## API Endpoints

### Customers
- List all customers: `GET /api/customers/`
- Create a new customer: `POST /api/customers/`
- Update existing customer: `PUT /api/customers/<id>/`

### Products
- List all products: `GET /api/products/`
- Create a new product: `POST /api/products/`

### Orders
- List all orders: `GET /api/orders/`
- Create a new order with multiple products and corresponding quantities: `POST /api/orders/`
- Edit existing order: `PUT /api/orders/<id>/`
- List orders based on products: `GET /api/orders/?products=Book,Pen`
- List orders based on the customer: `GET /api/orders/?customer=Sam`


## Validations

- Customer's and product’s name must be unique
- Weight must be a positive decimal and not more than 25kg
- Order cumulative weight must be under 150kg
- Order Date cannot be in the past

## Example Payload for any API

Example Payload for creating customer

```json
{
  "name": "Customer Name",
  "contact_number": "1234567890",
  "email": "dummycustomer@example.com"
}

```

## Requirements

Ensure your system meets the following requirements before setting up the E-Commerce API:

- Python 3.10+
- pip

Verify installed versions by running following commands:
```bash
python3 --version
pip3 --version
```


## Getting Started

### Creating a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies. Run the following commands:

```bash
# Install virtual environment
pip install virtualenv

# Activate the virtual environment
source venv/bin/activate
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kapil-malviya/E-commerce-APIs-DRF.git
   ```

2. Navigate to the project directory:
   ```bash
   cd E-commerce-APIs-DRF
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

### Usage

Run the development server:
```bash
python3 manage.py runserver
```

Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)          
For testing various APIS refer [API Endpoints](#api-endpoints)
