# Build stage
FROM python:3.10-slim-buster as builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=library_project.settings \
    DJANGO_DEBUG=False \
    PORT=8000

# Copy only necessary files from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY . .

# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Create a script to run the application
RUN echo '#!/bin/bash\n\
python manage.py migrate\n\
gunicorn library_project.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 2 --worker-class gthread --timeout 120 --access-logfile - --error-logfile - --capture-output --log-level info' > /app/start.sh && \
chmod +x /app/start.sh

# Run the start script
CMD ["/app/start.sh"] 