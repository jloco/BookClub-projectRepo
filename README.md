# Book Club


## Overview
Introducing BookClub, a comprehensive library database that aims to revolutionize the way people read, publish, and rate books. BookClub is designed to be a one-stop shop for all your literary needs, offering a vast selection of books across various genres, both old and new, from individual authors not found in mainstream publishing. The platform also features a rating and review system, allowing users to share their thoughts and opinions on the books they have read, and discover new titles based on recommendations from other users. In addition to being a rental service, BookClub also serves as a social media platform for individual authors. Authors can create their profiles, collaborate with other authors, and even contribute to each other’s work. This collaborative feature is designed to foster a sense of community and promote creativity among writers, which is often lacking in the traditional publishing industry. Finally, BookClub aims to make the process of publishing books more accessible and affordable for aspiring authors. Whether someone is looking to read or publish their own novel, BookClub provides a convenient and accessible solution for all book lovers. 

### Features
- Return all information about a given user
- Users can follow and be followed by other users
- Access books and their relevant information in the system
- Return dates a user has started, finished and currently reading a book
- Return users' comments, likes, and dislikes on books

## To run
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


## Project Video 
https://youtu.be/Skf9JiZg2E8
