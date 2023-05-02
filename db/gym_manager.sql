-- DROP TABLE IF EXISTS scheduled_time;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership_type VARCHAR(255),
    account_status BOOLEAN
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    capacity INT
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE
);

-- CREATE TABLE scheduled_time (
--     id SERIAL PRIMARY KEY,
--     date DATE,
--     time TIME,
--     scheduled_id INT REFERENCES scheduled_lessons(id) ON DELETE CASCADE
-- );