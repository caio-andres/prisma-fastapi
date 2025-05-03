# Prisma + FastAPI

A modern web application built with FastAPI and Prisma ORM, using PostgreSQL as the database.

### Technologies used

- Python 3.8+
- Prisma ORM
- FastAPI
- PostgreSQL
- Docker

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- Git

### Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/prisma-fastapi.git
cd prisma-fastapi
```

#### 2. Set up the environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.\.venv\Scripts\activate

# MacOS or Linux
source .venv/bin/activate
```

#### 3. Install dependencies

```bash
# Install Python dependencies
make install
```

#### 4. Set up the database

1. Start PostgreSQL using Docker Compose:
```bash
docker-compose up -d
```

2. Create a `.env` file based on the example:
```bash
cp .env-example .env
```

3. Update the `.env` file with your database credentials:
```
DATABASE_URL=postgresql://[username]:[password]@[host]:[port]/[database]?schema=public
```

#### 5. Initialize Prisma

```bash
# Generate Prisma client
prisma generate

# Apply database migrations
prisma db push
```

#### 6. Run the application

```bash
# Start the FastAPI server
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

### API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Development

- The main application code is in `main.py`
- Prisma schema is in the `prisma` directory
- Database migrations are managed through Prisma

### Docker

The project includes a Docker Compose configuration for PostgreSQL:
- Port: 5432
- Database: [Choose your database name]
- Username: postgres
- Password: [Choose a secure password]

Note: Make sure to update your `.env` file with the same database name and password you choose here.

### Make Commands

- `make install`: Install Python dependencies

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
