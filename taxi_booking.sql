show databases;
CREATE DATABASE IF NOT EXISTS taxi_booking;

CREATE DATABASE taxi_booking2;

USE taxi_booking2;

CREATE TABLE  users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    role ENUM('user', 'admin') DEFAULT 'user'
);

CREATE TABLE  drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    license_number VARCHAR(100) NOT NULL,
    status ENUM('available', 'unavailable') DEFAULT 'available'
);
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    driver_id INT,
    pickup_location VARCHAR(255) NOT NULL,
    drop_location VARCHAR(255) NOT NULL,
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
    booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

INSERT INTO users (name, email, password, phone, role) VALUES
('Abi', 'abi.@gmail.com', 'abi123', '1234567890', 'user'),
('Banu', 'banu@gmail.com', 'banu123', '0987654321', 'user');

INSERT INTO drivers (name, phone, license_number, status) VALUES
('Driver 1', '1112223333', 'XYZ12345', 'available'),
('Driver 2', '4445556666', 'ABC98765', 'available');

INSERT INTO bookings (user_id, driver_id, pickup_location, drop_location, status) VALUES
(1, 1, 'Location A', 'Location B', 'Completed'),
(2, 2, 'Location C', 'Location D', 'Pending'),
(1, 3, 'Location E', 'Location F', 'Cancelled');

DESCRIBE bookings;

SHOW CREATE TABLE bookings;


select*from users;

select* from drivers;

SELECT * FROM drivers WHERE driver_id = 1;


select*from bookings;