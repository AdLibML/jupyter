FROM jupyterhub/jupyterhub:5.3.0
# FROM jupyterhub/k8s-hub:4.2.0

USER root
# RUN rm -rf /var/lib/apt/lists/* \
#  && mkdir -p /var/lib/apt/lists/partial \
#  && chmod 755 /var/lib/apt/lists \
#  && apt-get update \
#  && apt-get install -y --no-install-recommends nodejs npm \
#  && npm install -g configurable-http-proxy \
#  && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-kubespawner \
    jupyterhub-idle-culler \
    jupyterhub-firstuseauthenticator \
    oauthenticator \
    jupyterhub-ldapauthenticator 

# # Make the directory for the config
# RUN mkdir -p /srv/jupyterhub

# # Copy configuration
# COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# # Set environment variable to ensure config is loaded
# ENV JUPYTERHUB_CONFIG=/srv/jupyterhub/jupyterhub_config.py

# # Start command
# CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
