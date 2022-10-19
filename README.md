# Description

It's a simple API-Server to return `Students Data` that reads and wrrite data in json file

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

There are 4 allowed requests:

- GET
- POST
- PUT
- DELETE

---

### GET

**_Request_**

- Request Header
  - `localhost:8000/student/`

**_Response_**

```json
[
  {
    "id": 1,
    "name": "Ahmed",
    "class": 13,
    "age": 14
  },
  {
    "id": 2,
    "name": "Ali",
    "class": 16,
    "age": 20
  }
]
```

### POST

**_Request_**

- Request Header
  - `localhost:8000/student/`
- Request Body

  - ```json
    {
      "id": 3,
      "name": "Ali",
      "class": 16,
      "age": 20
    }
    ```

**\*Response**

```json
{
  "id": 3,
  "name": "Ali",
  "class": 16,
  "age": 20
}
```

### PUT

**_Request_**

- Request Header
  - `localhost:8000/student/2`
- Request Body

  - ```json
    {
      "id": 2,
      "name": "Ammar",
      "class": 10,
      "age": 17
    }
    ```

**_Response_**

```json
[
  {
    "id": 1,
    "name": "Ahmed",
    "class": 13,
    "age": 14
  },
  {
    "id": 2,
    "name": "Ammar",
    "class": 10,
    "age": 17
  },
  {
    "id": 3,
    "name": "Ali",
    "class": 16,
    "age": 20
  }
]
```

### DELETE

**_Request_**

- Request Header
  - `localhost:8000/student/3/`

**_Response_**

```json
{
  "Message": "Sucessful Deleting"
}
```
