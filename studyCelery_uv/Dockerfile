FROM python:3.12

# ensures that the python output 
# i.e. the stdout and stderr streams are sent straight to terminal 
ENV PYTHONUNBUFFERED 1

ARG DEV=false

RUN apt-get update && apt-get install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

RUN uv --version

#COPY requirements.txt /app/
#COPY requirements.dev.txt /app/
COPY .python-version .
COPY pyproject.toml .
COPY uv.lock .
COPY app /app/

WORKDIR /app

RUN uv sync
RUN uv pip list

# install this only if it is dev mode
#RUN #if [ $DEV = true ]; then pip install -r requirements.dev.txt; fi

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.wsgi"]
CMD [ "uv", "shell"]
