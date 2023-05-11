from .models import Brand
from django.core.files import File
import os
from .models import Category, SubCategory, GeneralProduct, Brand
from urllib.request import urlretrieve
import tempfile


def populate_catagories():

    categories = {
        'Electronics': ['Laptops', 'Smartphones', 'Televisions', 'Gaming'],
        'Fashion': ['Men', 'Women', 'Kids', 'Accessories'],
        'Home & Furniture': ['Furniture', 'Decor', 'Lighting'],
        'Books': ['Fiction', 'Non-fiction', 'Children'],
        'Beauty & Personal Care': ['Makeup', 'Skincare', 'Fragrances']
    }

    for category_name, subcategories in categories.items():
        category = Category.objects.create(category_name=category_name)
        for subcategory_name in subcategories:
            subcategory = SubCategory.objects.create(
                parent_category=category, subcategory_name=subcategory_name)


def p():
    # brands = ['Apple', 'Samsung', 'Microsoft', 'Amazon', 'Google',
    #           'Coca-Cola', 'Pepsi', 'McDonald\'s', 'Nike', 'Adidas']

    # for brand in brands:
    #     Brand.objects.create(brand_name=brand)

    # def populate_products():

    electronics_products = {
        'Laptops': [
            {'name': 'MacBook Pro',
                'description': 'Apple laptop with Retina display and M1 chip'},
            {'name': 'Dell XPS 13',
                'description': 'Ultrabook with 11th-gen Intel Core processors and InfinityEdge display'},
            {'name': 'HP Spectre x360',
                'description': '2-in-1 laptop with 11th-gen Intel Core processors and OLED display'},
            {'name': 'Lenovo ThinkPad X1 Carbon',
                'description': 'Business laptop with 11th-gen Intel Core processors and 4K display option'},
            {'name': 'ASUS ZenBook Flip S',
                'description': '2-in-1 laptop with 11th-gen Intel Core processors and OLED display'}
        ],
        'Smartphones': [
            {'name': 'iPhone 13 Pro Max',
                'description': 'Apple smartphone with A15 Bionic chip and ProMotion display'},
            {'name': 'Samsung Galaxy S21 Ultra',
                'description': 'Samsung smartphone with Exynos 2100 or Snapdragon 888 chip and 120Hz display'},
            {'name': 'Google Pixel 6',
                'description': 'Google smartphone with Tensor chip and 90Hz display'},
            {'name': 'OnePlus 10 Pro',
                'description': 'OnePlus smartphone with Snapdragon 8 Gen 1 chip and AMOLED display'},
            {'name': 'Xiaomi Mi 12',
                'description': 'Xiaomi smartphone with Snapdragon 8 Gen 1 chip and OLED display'}
        ],
        'Televisions': [
            {'name': 'LG OLED CX', 'description': '4K OLED TV with AI ThinQ and webOS'},
            {'name': 'Samsung QN90A',
                'description': '4K QLED TV with Neo QLED and Quantum HDR'},
            {'name': 'Sony A90J',
                'description': '4K OLED TV with Cognitive Processor XR and Acoustic Surface Audio'},
            {'name': 'Vizio M-Series Quantum',
                'description': '4K TV with Quantum Color and Active Full Array backlight'},
            {'name': 'TCL 6-Series',
                'description': '4K QLED TV with Mini LED backlight and Dolby Vision HDR'}
        ],
        'Gaming': [
            {'name': 'PlayStation 5',
                'description': 'Sony gaming console with AMD Ryzen CPU and RDNA 2 GPU'},
            {'name': 'Xbox Series X',
                'description': 'Microsoft gaming console with AMD Ryzen CPU and RDNA 2 GPU'},
            {'name': 'Nintendo Switch OLED',
                'description': 'Nintendo gaming console with 7-inch OLED display and improved audio'},
            {'name': 'Alienware m15 R6',
                'description': 'Dell gaming laptop with 11th-gen Intel Core processors and NVIDIA RTX graphics'}
        ]
    }

    fashion_products = {
        'Men': ['Levi\'s 501 Jeans', 'Adidas Ultraboost', 'Patagonia Better Sweater', 'Ralph Lauren Polo Shirt', 'Timberland 6-Inch Boots'],
        'Women': ['Lululemon Align Pants', 'Everlane Day Heel', 'Madewell Perfect Vintage Jeans', 'Reformation Lacey Dress', 'Nike Air Force 1'],
        'Kids': ['Carter\'s Baby Onesies', 'Vans Slip-On Shoes', 'Mini Boden Rainbow Stripe Sweater', 'Pottery Barn Kids Backpack', 'Old Navy Graphic Tee'],
        'Accessories': ['Ray-Ban Wayfarer Sunglasses', 'Herschel Supply Co. Backpack', 'Daniel Wellington Watch', 'Gucci Belt', 'Tiffany & Co. Necklace']
    }

    home_and_furniture_products = {
        'Furniture': ['West Elm Andes Sofa', 'IKEA Billy Bookcase', 'CB2 Stax Console', 'Pottery Barn Aaron Chair', 'Article Culla Bed'],
        'Decor': ['Anthropologie Capri Blue Volcano Candle', 'West Elm Framed Canvas Art', 'CB2 Marble Bookends', 'Pottery Barn Classic Bath Towels', 'IKEA Rens Sheepskin Rug'],
        'Lighting': ['Muuto Ambit Pendant Light', 'Artemide Tolomeo Desk Lamp', 'Hive Active Light Bulb', 'Philips Hue Light Strip', 'LIFX Mini Color Smart Bulb']
    }
    books_products = {
        'Fiction': ['The Vanishing Half by Brit Bennett', 'The Four Winds by Kristin Hannah', 'Mexican Gothic by Silvia Moreno-Garcia', 'The Nightingale by Kristin Hannah', 'The Push by Ashley Audrain'],
        'Non-fiction': ['Empire of Pain by Patrick Radden Keefe', 'The Code Breaker by Walter Isaacson', 'Caste by Isabel Wilkerson', 'The Body Keeps the Score by Bessel van der Kolk', 'Braiding Sweetgrass by Robin Wall Kimmerer'],
        'Children': ['I Promise by LeBron James', 'Hair Love by Matthew A. Cherry', 'We Will Rock Our Classmates by Ryan T. Higgins', 'The Bad Seed by Jory John', 'The Wonky Donkey by Craig Smith']
    }
    beauty_and_personal_care_products = {
        'Makeup': ['Fenty Beauty Pro Filt', 'Soft Matte Foundation', 'Glossier Boy Brow', 'Pat McGrath Labs Mothership VIII Eyeshadow Palette', 'Charlotte Tilbury Pillow Talk Lipstick', 'Milk Makeup Hydro Grip Primer'],
        'Skincare': ['CeraVe Hydrating Facial Cleanser', 'The Ordinary Niacinamide 10% + Zinc 1%', 'Drunk Elephant Protini Polypeptide Cream', 'La Roche-Posay Anthelios Sunscreen', 'Youth to the People Superfood Antioxidant Cleanser'],
        'Fragrances': ['Chanel No. 5 Eau de Parfum', 'Byredo Gypsy Water Eau de Parfum', 'Jo Malone London Wood Sage & Sea Salt Cologne', 'Le Labo Santal 33 Eau de Parfum', 'Maison Margiela Replica Beach Walk Eau de Toilette']
    }

    for product in electronics_products["Laptops"]:

        s_cat = SubCategory.objects.get(id=4)

        GeneralProduct.objects.create(
            product_name=product["name"],
            subcategory=s_cat,
            product_description=product["description"],
            price_per_unit=499.99,
            total_available_in_stock=20,
            is_countable=True
        )
