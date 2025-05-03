# Use official Python image with Alpine Linux for a small footprint
FROM python:3.9-alpine3.13
LABEL maintainer="nemati.ai"

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Copy requirements file to a temporary location in the image
COPY ./requirements.txt /tmp/requirements.txt
# Copy application code to /app directory in the image
COPY ./app /app
# Set the working directory to /app
WORKDIR /app

# Expose port 8000 for the application
EXPOSE 8000

# Install dependencies and create a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 

# Add virtual environment to PATH
ENV PATH="/py/bin:$PATH" 

# Switch to the non-root user for security
USER django-user