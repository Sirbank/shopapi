# Use slim Python image — smaller attack surface, smaller image size
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first (layer caching)
# If requirements.txt hasn't changed, Docker reuses this cached layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Run as non-root user for security
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Expose application port
EXPOSE 8000

# Start uvicorn ASGI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
