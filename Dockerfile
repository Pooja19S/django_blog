# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY blog/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY blog/ .
COPY . .
COPY manage.py /app/
#COPY tests/ /app/

# Expose the port the Django app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]