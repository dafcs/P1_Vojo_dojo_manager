DROP TABLE IF EXISTS scheduled_time;
DROP TABLE IF EXISTS scheduled_classes;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership_type VARCHAR(255),
    account_status BOOLEAN
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    capacity INT
);

CREATE TABLE scheduled_classes (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    room_id INT REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE TABLE scheduled_time (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME,
    scheduled_id INT REFERENCES scheduled_classes(id) ON DELETE CASCADE
);