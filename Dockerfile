# using python3.13 image
FROM python:3.13.2

# set env
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="/$VIRTUAL_ENV/bin:$PATH"

# define in which folder we are going to store our application
ENV APP_HOME=/app

# create the directory/folder
RUN mkdir $APP_HOME
# create the folder for static files
RUN mkdir $APP_HOME/static

WORKDIR $APP_HOME

# expose the port of the container
EXPOSE 8000

COPY requirement.txt $APP_HOME/requirement.txt

RUN pip install -r requirement.txt

COPY . $APP_HOME/
