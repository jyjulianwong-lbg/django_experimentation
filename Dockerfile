FROM python:3.8.19

# It’s often recommended to set this environment variable when running Python within Docker containers to ensure that Python doesn’t buffer the output..
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# Install dependences first to make caching more efficient.
COPY requirements.txt ./
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Copy the rest of the source code.
COPY . .

EXPOSE 8000
RUN python manage.py migrate --noinput
CMD [ "gunicorn", "django_experimentation.wsgi:application", "--bind", "0.0.0.0:8000" ]