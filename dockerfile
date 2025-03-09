FROM python:3.12-slim

ENV POETRY_VERSION=2.1.1
RUN pip install "poetry==$POETRY_VERSION"

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /project

COPY . .

RUN poetry install 

CMD ["poetry", "run", "python", "./app/main.py"]