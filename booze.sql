CREATE TABLE booze (
    id VARCHAR(6) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    price INT(10) NOT NULL,
    category VARCHAR(255) NOT NULL,
    subcategory VARCHAR(255),
    volume VARCHAR(10),
    abv INT(3),
    description VARCHAR(1024),
    country VARCHAR(255)
);
