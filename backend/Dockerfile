# Use official Python image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the rest of the project
COPY . .

# Install dependencies manually
RUN pip install --no-cache-dir django gunicorn

# Expose the backend port
EXPOSE 8000

# Run database migrations and collect static files before starting the server
RUN python manage.py migrate

# Command to start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]

