FROM python:3.9-slim
# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Streamlit DockerFile Stream


# Set up working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]

