CREATE TABLE BOOKS (
    ISBN VARCHAR(13) PRIMARY KEY,
    author VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    volume INTEGER,
    binding VARCHAR(50),
    cost DECIMAL(10, 2)
);

CREATE TABLE READERS (
    passport_data VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    registration_date DATE
);

CREATE TABLE MAGAZINE (
    book_isbn VARCHAR(13) REFERENCES BOOKS(ISBN),
    reader_passport_data VARCHAR(20) REFERENCES READERS(passport_data),
    issue_date DATE,
    deadline DATE,
    PRIMARY KEY (book_isbn, reader_passport_data)
);