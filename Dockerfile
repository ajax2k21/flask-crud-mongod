FROM python:3.9-slim


WORKDIR /app

# Copy the required files
COPY app.py .
COPY requirements.txt .

# Install required packages inside the container
RUN pip install --no-cache-dir -r requirements.txt

# port 5000 for Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]


