## jk Backend API

### Overview

This is the backend API for the jk application, built using FastAPI and SQLAlchemy.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

2. Create a new virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Documentation

The API documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).

### Usage

The API can be used by sending HTTP requests to the following endpoints:

* `GET /api/health`: Health check endpoint
* `GET /api/users`: Get all users
* `POST /api/users`: Create new user
* `GET /api/users/{user_id}`: Get user by ID
* `PUT /api/users/{user_id}`: Update user
* `DELETE /api/users/{user_id}`: Delete user
* `GET /api/data`: Get all data
* `POST /api/data`: Create new data
* `PUT /api/data/{data_id}`: Update data
* `DELETE /api/data/{data_id}`: Delete data

### Docker

The application can be run using Docker by executing the following command:

```bash
docker-compose up
```

This will start the application and make it available at [http://localhost:8000](http://localhost:8000).

### Testing

The application can be tested using Pytest by executing the following command:

```bash
pytest
```

This will run all the tests in the `tests` directory.
