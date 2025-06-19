FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir transformers torch pillow

# Copy app files
COPY image_classification.py /app/image_classification.py

# Create assets folder
RUN mkdir /app/assets

# Copy assets
COPY ../assets /app/assets

CMD ["python", "image_classification.py"]
