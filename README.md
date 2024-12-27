# Django Blog Application

## Overview
A simple blog application built with Django and Django REST Framework. It supports CRUD operations for posts and comments, token-based authentication, and pagination.

---

## Features
- Create, Read, Update, and Delete posts.
- Add comments to posts.
- User authentication using tokens.
- Pagination for posts.
- Like and count likes for posts.

---

## Setup and Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment tool (optional)

### Steps
1. Clone the repository:
   - git clone <repository_url>
2. Install the requirements: 
   - pip freeze > requirements.txt
3. Move to the project folder:
   - cd <project_folder>
4. Run the application:
   - python manage.py runserver

<br><br>
### API ENDPOINTS 
- **GET METHOD** **Get Posts : **   http://127.0.0.1:8000/posts
- **GET METHOD** **Get Posts by id : **   http://127.0.0.1:8000/posts/5
- **POST METHOD** **Add new post : **   http://127.0.0.1:8000/posts
- **PUT METHOD** **Change the post : **  http://127.0.0.1:8000/posts/change/2
- **DELETE METHOD** **Remove the post : **  http://127.0.0.1:8000/posts/remove/3

- **GET METHOD** **Get Comments : **   http://127.0.0.1:8000/comments
- **POST METHOD** **Add new comment : **   http://127.0.0.1:8000/comments/
- ** GET METHOD** **Virtual Documentation : **   http://127.0.0.1:8000/blogDocs/


<br><br>

### Sample API Response/Output
#### Get all posts (Both Authenticated and Unauthenticated Users can see the results)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Get%20Posts.png)
<br><br><br>
#### Add new post (Only Authenticated Users can add the post)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Authenticated%20User%20Able%20To%20Add%20Post.png)
<br><br><br>
#### Add new post (Non Authenticated Users cannot add the post)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Non%20Authenticated%20User%20Cannot%20Add%20The%20%20Post.png)
<br><br><br>
#### Change existing post (Only Authenticated Users can change the post)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Authenticated%20User%20Able%20to%20Update%20The%20Post.png)
<br><br><br>
#### Remove existing post (Only Authenticated Users can remove the post)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Authenticated%20User%20Able%20To%20Remove%20The%20Post.png)
<br><br><br>
#### Get all comments (Both Authenticated and Unauthenticated Users can see the results)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Get%20Comments.png)
<br><br><br>
#### Add new comment (Non Authenticated Users cannot add the comment)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Non%20Authenticated%20User%20Cannot%20Add%20Comment.png)
<br><br><br>
#### Add new comment (Authenticated Users able to add the comment)
![Home Page](https://github.com/Periyasamy107/django_blog_application/blob/dev/Sample%20API%20Response/Authenticated%20User%20Able%20to%20Add%20Comment.png)
<br><br><br>







