FROM jupyterhub/k8s-singleuser-sample:4.2.0

USER root
RUN pip install uv poetry

COPY pyproject.toml poetry.lock* /tmp/
WORKDIR /tmp

# Configure Poetry to install into the system environment
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

ENV PATH="/usr/local/bin:${PATH}"

USER ${NB_UID}
WORKDIR ${HOME}
