### Backend Dependencies ###
pip install pymysql flask-cors


### Database Commands ###
# Create database
CREATE DATABASE IF NOT EXISTS aws_ug_ensenada;
USE aws_ug_ensenada;

# Create table users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

# Create table careers
CREATE TABLE careers (
    career_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(100),
    industry VARCHAR(100),
    experience_years INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

# Create table skills
CREATE TABLE skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    skill VARCHAR(100),
    level VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

# Create table hobbies
CREATE TABLE hobbies (
    hobby_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    hobby VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
