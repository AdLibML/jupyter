# FROM jupyterhub/jupyterhub:5.3.0
FROM jupyterhub/k8s-hub:4.2.0

# Install dependencies
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-kubespawner \
    jupyterhub-idle-culler \
    jupyterhub-firstuseauthenticator \
    oauthenticator \
    jupyterhub-ldapauthenticator \

# # Make the directory for the config
# RUN mkdir -p /srv/jupyterhub

# # Copy configuration
# COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# # Set environment variable to ensure config is loaded
# ENV JUPYTERHUB_CONFIG=/srv/jupyterhub/jupyterhub_config.py

# # Start command
# CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
