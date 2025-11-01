create database ShopSmart_DB;
use ShopSmart_DB;

create table customers (
customer_id int primary key,
first_name varchar(50),
last_name varchar(50),
email varchar(50),
mobile_number varchar(15),
registered_date date
);
INSERT INTO Customers (customer_id, first_name, last_name, email, mobile_number, registered_date) VALUES
(1, 'Aarav', 'Sharma', 'aarav.sharma@example.com', '9876543210', '2023-01-10'),
(2, 'Navya', 'Kaur', 'navya.kaur@example.com', '9876543211', '2023-01-15'),
(3, 'Rohan', 'Mehta', 'rohan.mehta@example.com', '9876543212', '2023-02-01'),
(4, 'Diya', 'Patel', 'diya.patel@example.com', '9876543213', '2023-02-05'),
(5, 'Arjun', 'Singh', 'arjun.singh@example.com', '9876543214', '2023-02-18'),
(6, 'Isha', 'Verma', 'isha.verma@example.com', '9876543215', '2023-03-01'),
(7, 'Kabir', 'Malhotra', 'kabir.malhotra@example.com', '9876543216', '2023-03-10'),
(8, 'Aditi', 'Rao', 'aditi.rao@example.com', '9876543217', '2023-03-20'),
(9, 'Vivaan', 'Bansal', 'vivaan.bansal@example.com', '9876543218', '2023-04-02'),
(10, 'Meera', 'Chopra', 'meera.chopra@example.com', '9876543219', '2023-04-15'),
(11, 'Reyansh', 'Gupta', 'reyansh.gupta@example.com', '9876543220', '2023-04-28'),
(12, 'Anaya', 'Khanna', 'anaya.khanna@example.com', '9876543221', '2023-05-10'),
(13, 'Vihaan', 'Sethi', 'vihaan.sethi@example.com', '9876543222', '2023-05-22'),
(14, 'Tara', 'Nair', 'tara.nair@example.com', '9876543223', '2023-06-05'),
(15, 'Advait', 'Reddy', 'advait.reddy@example.com', '9876543224', '2023-06-15');



create table addresses (
addresses_id int primary key,
customer_id int,
street varchar(50),
city varchar(50),
state varchar(50),
zip_code varchar(15),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
INSERT INTO Addresses (addresses_id, customer_id, street, city, state, zip_code) VALUES
(1, 1, '12 Green Park Road', 'Delhi', 'Delhi', '110016'),
(2, 2, '45 Model Town', 'Amritsar', 'Punjab', '143001'),
(3, 3, '23 MG Road', 'Mumbai', 'Maharashtra', '400001'),
(4, 4, '78 Satellite Area', 'Ahmedabad', 'Gujarat', '380015'),
(5, 5, '56 Sector 22', 'Chandigarh', 'Chandigarh', '160022'),
(6, 6, '90 Civil Lines', 'Kanpur', 'Uttar Pradesh', '208001'),
(7, 7, '34 Park Street', 'Kolkata', 'West Bengal', '700016'),
(8, 8, '10 Anna Nagar', 'Chennai', 'Tamil Nadu', '600040'),
(9, 9, '5 Banjara Hills', 'Hyderabad', 'Telangana', '500034'),
(10, 10, '22 Koregaon Park', 'Pune', 'Maharashtra', '411001'),
(11, 11, '89 Rajouri Garden', 'Delhi', 'Delhi', '110027'),
(12, 12, '11 Sector 14', 'Gurugram', 'Haryana', '122001'),
(13, 13, '7 Vasant Vihar', 'Delhi', 'Delhi', '110057'),
(14, 14, '29 Marine Drive', 'Mumbai', 'Maharashtra', '400020'),
(15, 15, '64 Indiranagar', 'Bengaluru', 'Karnataka', '560038');


create table categories (
category_id int primary key,
category_name varchar(50),
descriptions varchar(100)
);
INSERT INTO Categories (category_id, category_name, descriptions) VALUES
(1, 'Electronics', 'Devices like mobiles, laptops, and accessories'),
(2, 'Fashion', 'Clothing, shoes, and accessories'),
(3, 'Home Appliances', 'Essential appliances for home use'),
(4, 'Books', 'Educational, fictional, and non-fictional books'),
(5, 'Beauty & Personal Care', 'Cosmetics and skincare products'),
(6, 'Sports & Fitness', 'Gym equipment and sports gear'),
(7, 'Toys & Games', 'Toys and games for kids and adults'),
(8, 'Furniture', 'Home and office furniture items'),
(9, 'Groceries', 'Everyday food and household items'),
(10, 'Automobile Accessories', 'Car and bike accessories'),
(11, 'Jewelry', 'Gold, silver, and artificial jewelry items'),
(12, 'Pet Supplies', 'Products for pets and animals'),
(13, 'Health & Wellness', 'Medicines, supplements, and wellness products'),
(14, 'Stationery', 'Office and school stationery items'),
(15, 'Garden & Outdoor', 'Tools and equipment for gardening and outdoor use');


CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    category_id INT,
    supplier_id INT,
    product_name VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);
INSERT INTO Products (product_id, category_id, supplier_id, product_name, price, stock_quantity) VALUES
(1, 1, 1, 'Samsung Galaxy A55', 28999.00, 45),
(2, 1, 1, 'HP Pavilion Laptop', 67990.00, 25),
(3, 2, 2, 'Men Cotton T-Shirt', 599.00, 150),
(4, 2, 2, 'Women Denim Jacket', 1799.00, 80),
(5, 3, 3, 'Philips Mixer Grinder', 3499.00, 60),
(6, 3, 3, 'LG Smart Refrigerator', 45999.00, 15),
(7, 4, 4, 'The Psychology of Money', 499.00, 120),
(8, 4, 4, 'Atomic Habits', 399.00, 100),
(9, 5, 5, 'L’Oreal Face Serum', 999.00, 75),
(10, 5, 5, 'Maybelline Lipstick', 499.00, 200),
(11, 6, 6, 'Yoga Mat', 899.00, 90),
(12, 6, 6, 'Dumbbell Set 10kg', 2499.00, 40),
(13, 8, 8, 'Wooden Study Table', 6999.00, 30),
(14, 9, 9, 'Fortune Sunflower Oil (5L)', 799.00, 180),
(15, 13, 13, 'Vitamin C Tablets (60)', 699.00, 95);

create table suppliers (
supplier_id int primary key,
supplier_name varchar(50),
supplier_email varchar(50),
supplier_phone varchar(15)
);
INSERT INTO Suppliers (supplier_id, supplier_name, supplier_email, supplier_phone) VALUES
(1, 'TechWorld Distributors', 'support@techworld.com', '9876500011'),
(2, 'StyleHub Clothing Co.', 'contact@stylehub.com', '9876500012'),
(3, 'HomeEase Appliances', 'info@homeease.com', '9876500013'),
(4, 'BookNest Publishers', 'sales@booknest.com', '9876500014'),
(5, 'GlowCare Cosmetics', 'hello@glowcare.com', '9876500015'),
(6, 'FitPro Sports', 'support@fitpro.com', '9876500016'),
(7, 'ToyTime Ltd.', 'service@toytime.com', '9876500017'),
(8, 'FurniCraft', 'info@furnicraft.com', '9876500018'),
(9, 'DailyFresh Grocers', 'orders@dailyfresh.com', '9876500019'),
(10, 'AutoGear Traders', 'sales@autogear.com', '9876500020'),
(11, 'JewelsNest', 'info@jewelsnest.com', '9876500021'),
(12, 'PetPal Suppliers', 'support@petpal.com', '9876500022'),
(13, 'MediHealth Pharma', 'care@medihealth.com', '9876500023'),
(14, 'OfficeMate Stationers', 'sales@officemate.com', '9876500024'),
(15, 'GreenScape Outdoors', 'contact@greenscape.com', '9876500025');


create table inventories (
inventory_id int primary key,
product_id int,
quantity_in_stock int,
last_updated date,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO Inventories (inventory_id, product_id, quantity_in_stock, last_updated) VALUES
(1, 1, 45, '2025-10-01'),
(2, 2, 25, '2025-09-29'),
(3, 3, 150, '2025-10-10'),
(4, 4, 80, '2025-10-07'),
(5, 5, 60, '2025-10-05'),
(6, 6, 15, '2025-09-30'),
(7, 7, 120, '2025-10-12'),
(8, 8, 100, '2025-10-08'),
(9, 9, 75, '2025-10-03'),
(10, 10, 200, '2025-10-04'),
(11, 11, 90, '2025-10-09'),
(12, 12, 40, '2025-10-02'),
(13, 13, 30, '2025-10-06'),
(14, 14, 180, '2025-10-11'),
(15, 15, 95, '2025-10-10');


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
INSERT INTO Orders (order_id, customer_id, order_date, total_amount, status) VALUES
(1, 1, '2025-09-25', 28999.00, 'Delivered'),
(2, 2, '2025-09-26', 67990.00, 'Delivered'),
(3, 3, '2025-09-27', 1198.00, 'Pending'),
(4, 4, '2025-09-28', 1799.00, 'Delivered'),
(5, 5, '2025-09-29', 3499.00, 'Shipped'),
(6, 6, '2025-09-30', 45999.00, 'Delivered'),
(7, 7, '2025-10-01', 499.00, 'Delivered'),
(8, 8, '2025-10-02', 1398.00, 'Pending'),
(9, 9, '2025-10-03', 1998.00, 'Delivered'),
(10, 10, '2025-10-04', 999.00, 'Cancelled'),
(11, 11, '2025-10-05', 2499.00, 'Shipped'),
(12, 12, '2025-10-06', 6999.00, 'Delivered'),
(13, 13, '2025-10-07', 799.00, 'Delivered'),
(14, 14, '2025-10-08', 699.00, 'Pending'),
(15, 15, '2025-10-09', 55998.00, 'Delivered');


create table order_detail (
order_detail_id int primary key,
order_id int,
product_id int,
quantity int,
price decimal(10,2),
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO Order_Detail (order_detail_id, order_id, product_id, quantity, price) VALUES
(1, 1, 1, 1, 28999.00),
(2, 2, 2, 1, 67990.00),
(3, 3, 3, 2, 599.00),
(4, 4, 4, 1, 1799.00),
(5, 5, 5, 1, 3499.00),
(6, 6, 6, 1, 45999.00),
(7, 7, 7, 1, 499.00),
(8, 8, 8, 2, 699.00),
(9, 9, 9, 2, 999.00),
(10, 10, 10, 1, 999.00),
(11, 11, 12, 1, 2499.00),
(12, 12, 13, 1, 6999.00),
(13, 13, 14, 2, 799.00),
(14, 14, 15, 1, 699.00),
(15, 15, 2, 1, 55998.00);

create table payments (
payment_id int primary key,
order_id int,
payment_date date,
payment_method varchar(50),
payment_amount decimal(10,2),
FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
INSERT INTO Payments (payment_id, order_id, payment_date, payment_method, payment_amount) VALUES
(1, 1, '2025-09-25', 'UPI', 28999.00),
(2, 2, '2025-09-26', 'Credit Card', 67990.00),
(3, 3, '2025-09-27', 'Debit Card', 1198.00),
(4, 4, '2025-09-28', 'Net Banking', 1799.00),
(5, 5, '2025-09-29', 'Cash on Delivery', 3499.00),
(6, 6, '2025-09-30', 'UPI', 45999.00),
(7, 7, '2025-10-01', 'UPI', 499.00),
(8, 8, '2025-10-02', 'Credit Card', 1398.00),
(9, 9, '2025-10-03', 'UPI', 1998.00),
(10, 10, '2025-10-04', 'Debit Card', 999.00),
(11, 11, '2025-10-05', 'UPI', 2499.00),
(12, 12, '2025-10-06', 'Net Banking', 6999.00),
(13, 13, '2025-10-07', 'Cash on Delivery', 799.00),
(14, 14, '2025-10-08', 'Credit Card', 699.00),
(15, 15, '2025-10-09', 'UPI', 55998.00);


create table delivery (
delivery_id int primary key,
order_id int,
delivery_status varchar(50),
delivery_date datetime,
FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
INSERT INTO Delivery (delivery_id, order_id, delivery_status, delivery_date) VALUES
(1, 1, 'Delivered', '2025-09-27 14:30:00'),
(2, 2, 'Delivered', '2025-09-28 11:45:00'),
(3, 3, 'Pending', NULL),
(4, 4, 'Delivered', '2025-09-29 16:10:00'),
(5, 5, 'Shipped', NULL),
(6, 6, 'Delivered', '2025-10-01 13:00:00'),
(7, 7, 'Delivered', '2025-10-02 10:30:00'),
(8, 8, 'Pending', NULL),
(9, 9, 'Delivered', '2025-10-04 18:00:00'),
(10, 10, 'Cancelled', NULL),
(11, 11, 'Shipped', NULL),
(12, 12, 'Delivered', '2025-10-07 09:20:00'),
(13, 13, 'Delivered', '2025-10-08 15:40:00'),
(14, 14, 'Pending', NULL),
(15, 15, 'Delivered', '2025-10-10 12:10:00');


create table employees (
employee_id int primary key,
employee_name varchar(50),
employee_role varchar(50),
employee_email varchar(100)
);
INSERT INTO Employees (employee_id, employee_name, employee_role, employee_email) VALUES
(1, 'Aarav Sharma', 'Delivery Executive', 'aarav.sharma@onlinestore.com'),
(2, 'Priya Mehta', 'Customer Support', 'priya.mehta@onlinestore.com'),
(3, 'Rohan Verma', 'Warehouse Manager', 'rohan.verma@onlinestore.com'),
(4, 'Neha Singh', 'Delivery Executive', 'neha.singh@onlinestore.com'),
(5, 'Vikram Das', 'Inventory Analyst', 'vikram.das@onlinestore.com'),
(6, 'Simran Kaur', 'Customer Support', 'simran.kaur@onlinestore.com'),
(7, 'Aditya Patel', 'Logistics Coordinator', 'aditya.patel@onlinestore.com'),
(8, 'Kavita Nair', 'Delivery Executive', 'kavita.nair@onlinestore.com'),
(9, 'Rahul Bansal', 'Data Analyst', 'rahul.bansal@onlinestore.com'),
(10, 'Sneha Iyer', 'Customer Support', 'sneha.iyer@onlinestore.com'),
(11, 'Manish Kumar', 'Warehouse Staff', 'manish.kumar@onlinestore.com'),
(12, 'Pooja Reddy', 'Delivery Executive', 'pooja.reddy@onlinestore.com'),
(13, 'Arjun Kapoor', 'Operations Manager', 'arjun.kapoor@onlinestore.com'),
(14, 'Tanya Gupta', 'Customer Support', 'tanya.gupta@onlinestore.com'),
(15, 'Harish Nair', 'Warehouse Supervisor', 'harish.nair@onlinestore.com');


create table reviews (
review_id int primary key,
product_id int,
customer_id int,
rating int,
review_text varchar(1024),
FOREIGN KEY (product_id) REFERENCES products(product_id),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO Reviews (review_id, product_id, customer_id, rating, review_text) VALUES
(1, 1, 3, 5, 'Excellent quality product, totally worth the price.'),
(2, 2, 5, 4, 'Good performance but delivery was a bit late.'),
(3, 3, 2, 3, 'Average product, expected better packaging.'),
(4, 4, 7, 5, 'Amazing! Highly recommended for daily use.'),
(5, 5, 8, 4, 'Nice design and build quality. Value for money.'),
(6, 6, 4, 2, 'Product stopped working after a week. Disappointed.'),
(7, 7, 9, 5, 'Very satisfied. Fast shipping and great service.'),
(8, 8, 10, 4, 'Looks great and functions well.'),
(9, 9, 1, 3, 'Not bad, but can be improved.'),
(10, 10, 6, 5, 'Superb experience, will buy again.'),
(11, 11, 11, 4, 'Good product but a bit overpriced.'),
(12, 12, 12, 5, 'Perfect! Exactly as described.'),
(13, 13, 13, 3, 'Okay product, nothing special.'),
(14, 14, 14, 4, 'Good service and product quality.'),
(15, 15, 15, 5, 'Loved it! Fast delivery and top-notch quality.');


create table discounts (
discount_id int primary key,
product_id int,
discount_percentage decimal(5,2),
start_date date,
end_date date,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO Discounts (discount_id, product_id, discount_percentage, start_date, end_date) VALUES
(1, 1, 10.00, '2025-10-01', '2025-10-15'),
(2, 2, 5.00, '2025-09-20', '2025-10-10'),
(3, 3, 15.00, '2025-10-10', '2025-10-25'),
(4, 4, 20.00, '2025-10-05', '2025-10-30'),
(5, 5, 7.50, '2025-10-12', '2025-11-01'),
(6, 6, 25.00, '2025-10-01', '2025-10-20'),
(7, 7, 12.00, '2025-09-28', '2025-10-12'),
(8, 8, 18.00, '2025-10-15', '2025-10-31'),
(9, 9, 10.00, '2025-10-03', '2025-10-17'),
(10, 10, 5.50, '2025-10-08', '2025-10-28'),
(11, 11, 30.00, '2025-10-01', '2025-10-18'),
(12, 12, 8.00, '2025-10-06', '2025-10-26'),
(13, 13, 22.00, '2025-10-02', '2025-10-22'),
(14, 14, 9.00, '2025-09-29', '2025-10-19'),
(15, 15, 17.50, '2025-10-10', '2025-10-29');


create table wishlist (
wishlist_id int primary key,
customer_id int,
product_id int,
FOREIGN KEY (product_id) REFERENCES products(product_id),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO Wishlist (wishlist_id, customer_id, product_id) VALUES
(1, 1, 5),
(2, 2, 3),
(3, 3, 7),
(4, 4, 2),
(5, 5, 10),
(6, 6, 1),
(7, 7, 8),
(8, 8, 6),
(9, 9, 4),
(10, 10, 12),
(11, 11, 9),
(12, 12, 11),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15);


create table cart (
cart_id int primary key,
customer_id int,
product_id int,
quantity int,
FOREIGN KEY (product_id) REFERENCES products(product_id),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO Cart (cart_id, customer_id, product_id, quantity) VALUES
(1, 1, 1, 2),
(2, 2, 3, 1),
(3, 3, 5, 4),
(4, 4, 2, 3),
(5, 5, 8, 1),
(6, 6, 4, 2),
(7, 7, 7, 1),
(8, 8, 9, 5),
(9, 9, 6, 2),
(10, 10, 10, 1),
(11, 11, 11, 3),
(12, 12, 12, 2),
(13, 13, 13, 1),
(14, 14, 14, 4),
(15, 15, 15, 2);