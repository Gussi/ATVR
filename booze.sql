CREATE TABLE booze (
    id VARCHAR(6) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DECIMAL NOT NULL,
    category VARCHAR(255),
    volume VARCHAR(10),
    abv DECIMAL(4,2),
    country VARCHAR(255)
);
