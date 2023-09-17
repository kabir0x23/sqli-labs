-- Create a table to store user information
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Insert some sample data for testing
INSERT INTO users (username, password) VALUES
    ('kabir0x23', 'kabir0x23'),
    ('theanvil01', 'theanvil01'),
    ('0xftw', '0xftw');
