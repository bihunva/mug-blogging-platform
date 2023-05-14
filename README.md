# MUG blogging-platform

Broadcast-style communications systems that enable authors to publish articles.

## Check it out!

[MUG project deployed to Render](https://mug-91nk.onrender.com/)

## Installation

Before you begin, make sure you have Python 3.11 installed on your computer

1. Clone the project repository to your computer using the following command:
    ```shell
    git clone https://github.com/bihunva/mug-blogging-platform
    ```

2. Create and activate a virtual environment (venv) by running the following commands:
    ```shell
    python3 -m venv venv
    source venv/bin/activate # for Unix-based systems
    venv\Scripts\activate # for Windows
    ```

3. Install the necessary dependencies by running the following command:
    ```shell
    pip install -r requirements.txt
    ```

4. Set the following environment variables in your shell or IDE to run the project:
   ```shell
   export DJANGO_SECRET_KEY='your_secret_key'
   export DJANGO_DEBUG=True
   ```

5. Apply all required migrations by running the following command:
    ```shell
   python manage.py migrate
    ```

6. Start the local server by running the following command:
    ```shell
    python manage.py runserver
    ```

7. After the project has successfully started, open a web browser and navigate to the local server
   at `http://localhost:8000/`.

## Features

### User Authentication

The Mug Blogging Platform includes a user authentication system that allows users to sign up and login to the platform
using their email address and password.

### Commenting System

Registered users can leave comments on posts published on the Mug Blogging platform.

### Post Management

Registered users can publish their own posts. They can also save posts to their favorite list.

### Search Functionality

The Mug Blogging Platform has a search functionality that allows users to search for posts using keywords. This can help
users quickly find relevant posts on topics they are interested in.

### Tagging System

Posts on the Mug Blogging Platform can be tagged with one or more keywords, making it easy to find posts related to
specific topics. Users can also browse posts by tags, allowing them to discover new content on topics they enjoy.

## Test user credentials:

Username:

```
testuser
```

Password:

```
user12345
```

## Demo

![Website Interface](demo.png)