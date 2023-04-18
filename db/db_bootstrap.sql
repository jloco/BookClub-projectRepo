-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
create database BookClub;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on BookClub.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too.

use BookClub;

CREATE TABLE Countries (
    country_code VARCHAR(2) NOT NULL PRIMARY KEY, # changed to 2, easier for mockaroo 
    country_name VARCHAR(60) NOT NULL,
    flag_url TINYTEXT NOT NULL
);

CREATE TABLE Languages (
    language_code VARCHAR(2) NOT NULL PRIMARY KEY,
    language_name VARCHAR(60) NOT NULL
);

CREATE TABLE Users (
    user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(35) NOT NULL UNIQUE,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    bio TEXT,
    country_code  VARCHAR(3),
    company VARCHAR(50),
    CONSTRAINT user_country FOREIGN KEY (country_code) REFERENCES Countries (country_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE Books (
    book_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    num_pages INTEGER NOT NULL,
    num_chapters INTEGER NOT NULL,
    language_code VARCHAR(2) NOT NULL,
    content MEDIUMTEXT NOT NULL,
    CONSTRAINT book_language FOREIGN KEY (language_code) REFERENCES Languages (language_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE Comments ( 
    # having trouble with replies referring to the same book_id
    comment_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(1000) NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    replying_to INTEGER,
    parent_book INTEGER NOT NULL,
    comment_author INTEGER,
    CONSTRAINT comment_book FOREIGN KEY (parent_book) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT comment_reply FOREIGN KEY (replying_to) REFERENCES Comments (comment_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT comment_author FOREIGN KEY (comment_author) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Genres (
    genre_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE Followers (
    follower_id INTEGER NOT NULL,
    followed_id INTEGER NOT NULL,
    follow_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, followed_id),
    CONSTRAINT followers_follower FOREIGN KEY (follower_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT followers_followed FOREIGN KEY (followed_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Book_Genres (
    book_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, genre_id),
    CONSTRAINT book_genres_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT book_genres_genre FOREIGN KEY (genre_id) REFERENCES Genres (genre_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Written_By (
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, user_id),
    CONSTRAINT written_by_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT written_by_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Book_Likes (
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (book_id, user_id),
    CONSTRAINT book_likes_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT book_likes_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Book_Dislikes (
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (book_id, user_id),
    CONSTRAINT book_dislikes_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT book_dislikes_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Currently_Reading (
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date_started DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (book_id, user_id),
    CONSTRAINT currently_reading_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT currently_reading_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Comment_Likes (
    comment_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (comment_id, user_id),
    CONSTRAINT comment_likes_comment FOREIGN KEY (comment_id) REFERENCES Comments (comment_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT comment_likes_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Comment_Dislikes (
    comment_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (comment_id, user_id),
    CONSTRAINT comment_dislikes_comment FOREIGN KEY (comment_id) REFERENCES Comments (comment_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT comment_dislikes_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Bookshelf (
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    date_started DATETIME NOT NULL,
    date_finished DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    rating INTEGER,
    PRIMARY KEY (user_id, book_id),
    CONSTRAINT bookshelf_book FOREIGN KEY (book_id) REFERENCES Books (book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT bookshelf_user FOREIGN KEY (user_id) REFERENCES Users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);



