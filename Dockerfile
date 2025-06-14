# using python3.10 image
FROM python:3.13.2

# set env
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv SVIRTUAL_ENV
ENV PATH="/$VIRTUAL_ENV/bin: $PATH"

# define in which folder we are going to store our application
s create new eny Var
ENV APP HOME=/app
# create the directory/folder
RUN mkdir SAPP_HOME
# create the folder for static files
RUN mkdir $APP_HOME/static

WORKDIR $APP_HOME

# make the s0e0 port of the container exposed to the laptop 8000 port
EXPOSE 8000

COPY requirements.txt $APP_HOME/requirements.txt

RUN pip install -r requirements.txt

COPY . SAPP_HOME/
