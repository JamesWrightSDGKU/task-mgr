
-- Create database table

CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Insert some dummy data to test with (multi-insert):

INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "wash the car",
    "Take the car to the car wash",
    "Make sure it gets vacuumed and waxed"
),
(
    "walk the dog",
    "Fido needs exercise daily",
    "Make sure to do three laps around the park"
),
(
    "Buy groceries",
    "Go to the super market and buy groceries",
    "We need: Eggs, bacon, tomatoes and bread"
);

-- Don't forget the semi-colon!