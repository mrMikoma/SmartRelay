# Using python 3.10.12-slim-buster as base image
FROM python:3.10.12-slim-buster

# Set the working directory in the container
WORKDIR /backend

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /backend/

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/backend/venv/bin:$PATH"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /backend/

# Create a non-root user
RUN useradd -m nonrootuser
USER nonrootuser

# Run main.py when the container launches
CMD ["python3", "main.py"]