FROM python:3.9-alpine3.13
LABEL maintainer="nemati.ai"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt


COPY ./app /app
WORKDIR /app

EXPOSE 8000


ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = true ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    # Clean up unnecessary files to reduce image size
    rm -rf /tmp && \
    adduser -D -H django-user

# Add virtual environment to PATH
ENV PATH="/py/bin:$PATH" 

# Switch to the non-root user for security
USER django-user