FROM jupyterhub/jupyterhub:latest

# Install dependencies
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-idle-culler \
    jupyterhub-firstuseauthenticator \
    oauthenticator

# Make the directory for the config
RUN mkdir -p /srv/jupyterhub

# Copy configuration
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Set environment variable to ensure config is loaded
ENV JUPYTERHUB_CONFIG=/srv/jupyterhub/jupyterhub_config.py

# Start command
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
