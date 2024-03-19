-- Создание таблицы "Users" для хранения информации о пользователях
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    RegistrationDate DATE NOT NULL
);

-- Создание таблицы "Orders" для хранения информации о заказах
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    UserID INTEGER,
    OrderDate DATE NOT NULL,
    TotalAmount REAL NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
