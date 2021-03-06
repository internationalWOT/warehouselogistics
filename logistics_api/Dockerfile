# FROM python:3.7.1-alpine

# WORKDIR /opt/project

# RUN pip install --upgrade pip && pip --no-cache-dir install poetry

# COPY ./logistics_api/pyproject.toml .

# RUN poetry install --no-dev
###############################################
# Base Image
###############################################
FROM python:3.9-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0 \
    POETRY_HOME="/opt/poetry" \ 
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential 

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY ./logistics_api/poetry.lock ./logistics_api/pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

###############################################
# Production Image
###############################################
FROM python-base as production
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY ./logistics_api/ /src/
CMD ["uvicorn", "src.Setup.py:app", "--host", "0.0.0.0", "--port", "80"]

# COPY src run_flask_app.sh ./
# EXPOSE 8000
# CMD ["./run_flask_app.sh"]