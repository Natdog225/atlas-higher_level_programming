-- Creates the table `unique_id` if it doesn't exist.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT PRIMARY KEY DEFAULT 1,
    name VARCHAR(256)
);