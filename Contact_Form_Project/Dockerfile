# Create Base image
FROM python:3.13-slim

# Set the Working Directory
WORKDIR /app

# Copy over dependencies
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app contents over
COPY . /app

# Expose port
EXPOSE 5000

# Run application
CMD [ "python3", "run.py" ]