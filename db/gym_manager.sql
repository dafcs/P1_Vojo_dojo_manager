DROP TABLE IF EXISTS scheduled_time;
DROP TABLE IF EXISTS scheduled_classes;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership_type VARCHAR(255),
    account_status BOOLEAN
);

CREATE TABLE classes (
    id INT PRIMARY KEY,
    duration INT,
    name VARCHAR(255)
);

CREATE TABLE rooms (
    id INT PRIMARY KEY
    capacity INT
);

CREATE TABLE scheduled_classes (
    id INT PRIMARY KEY,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    room_id INT REFERENCES rooms(id) ON DELETE CASCADE,
);

CREATE TABLE scheduled_time (
    id INT PRIMARY KEY,
    date INT,
    time INT,
    scheduled_id INT REFERENCES scheduled_classes(id) ON DELETE CASCADE
)