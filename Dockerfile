FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into the container (Corrected the two dots)
COPY . .

# Start the application
CMD ["python", "app.py"]