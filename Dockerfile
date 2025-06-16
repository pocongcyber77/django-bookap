# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if any (e.g., for Pillow, psycopg2-binary)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/ 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Run Gunicorn when the container launches
CMD ["gunicorn", "library_project.wsgi:application", "--bind", "0.0.0.0:8000"] 