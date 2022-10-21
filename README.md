# Description

It's a simple API-Server to controll the `Student Data` using models and crud's methods in Django

## Needed Installition

- First you need to install `python-3`

- Second you need to install `poetry`

## Install Poetry

Follow the decoumentation here `https://python-poetry.org/docs/`

## Installation

```shell
# clone the repo
git clone https://github.com/AhmedMustafaEl-Zahaby/Django-Server.git
```

```shell
# get into repo's directoriy
cd Django-Server
```

```shell
# start the project
poetry shell
poetry install
python manage.py runserver
```

## Usage/Examples

There are two paths:

- With out parameters (id):

  There are 2 allowed requests:

  - GET
  - POST

- With parameters (id):

There are 4 allowed requests:

- GET
- POST
- PUT
- DELETE

---

### With Parameters

### GET

**_Request_**

- Request Header
  - `localhost:8000/api/student`

**_Response_**

```json
[] <!--- There is no data init --->
```

### POST

**_Request_**

- Request Header
  - `localhost:8000/api/student`
- Request Body

  - ```json
    {
      "First_name": "Ali",
      "Second_name": "Mohamed",
      "Email": "https://www.google.com",
      "Class": 16,
      "Age": 20
    }
    ```

**\*Response**

```json
[
  {
    "First_name": "Ali",
    "Second_name": "Mohamed",
    "Email": "https://www.google.com",
    "Class": 16,
    "Age": 20
  }
]
```

---

### With Parameters

### GET

**_Request_**

- Request Header
  - `localhost:8000/api/student/1`

**_Response_**

```json
[] <!--- There is no data init --->
```

### POST

**_Request_**

- Request Header
  - `localhost:8000/api/student/1`
- Request Body

  - ```json
    {
      "First_name": "Ali",
      "Second_name": "Mohamed",
      "Email": "https://www.google.com",
      "Class": 16,
      "Age": 20
    }
    ```

**\*Response**

```json
[
  {
    "First_name": "Ali",
    "Second_name": "Mohamed",
    "Email": "https://www.google.com",
    "Class": 16,
    "Age": 20
  }
]
```

### PUT

**_Request_**

- Request Header
  - `localhost:8000/api/student/1`
- Request Body

  - ```json
    {
      "First_name": "Ahmed",
      "Second_name": "Hashem",
      "Email": "https://www.Facebook.com",
      "Class": 2,
      "Age": 15
    }
    ```

**_Response_**

```json
[
  {
    "First_name": "Ahmed",
    "Second_name": "Hashem",
    "Email": "https://www.Facebook.com",
    "Class": 2,
    "Age": 15
  }
]
```

### DELETE

**_Request_**

- Request Header
  - `localhost:8000/api/student/1`

**_Response_**

```json
[] <!--- There is no data init --->
```
