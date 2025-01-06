USE ArticlesDatabase;
GO

BEGIN
    CREATE TABLE Articles
        id int NOT NULL IDENTITY(1,1),
        title varchar(255),
        category varchar(255),
        author varchar(255)
END