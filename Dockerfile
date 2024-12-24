FROM python:3.9-slim

# Install dependencies and upgrade pip
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc && \
    pip3 install --no-cache-dir -U pip && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Start the application
CMD ["bash", "start"]
