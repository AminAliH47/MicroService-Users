FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV USER myuser

# Upgrade pip before create non-root user
RUN python -m pip install --upgrade pip

RUN adduser -D $USER --disabled-password
USER $USER

WORKDIR /home/$USER

# Create Database datafile
RUN mkdir /home/$USER/dbdata

COPY --chown=$USER:$USER requirements.txt requirements.txt
ENV PATH="/home/${USER}/.local/bin:${PATH}"
COPY --chown=$USER:$USER . .

# Install requirements
RUN pip install --user -r requirements.txt

CMD sleep 8 && \
    python3 manage.py makemigrations --no-input && \
    python3 manage.py migrate --no-input && \
    python manage.py grpcrunserver 0.0.0.0:5000