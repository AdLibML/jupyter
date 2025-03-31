FROM quay.io/jupyter/base-notebook:latest

USER root
# Install Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy poetry configuration
COPY pyproject.toml poetry.lock* /tmp/
WORKDIR /tmp

# Install dependencies directly using Poetry (with --no-root option)
RUN poetry install --no-interaction --no-ansi --no-root

# Switch back to notebook user
USER ${NB_UID}
WORKDIR ${HOME}

# Jupyter will now run without password authentication
# The authentication will be handled by JupyterHub instead
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
