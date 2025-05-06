c = get_config()

# Basic config
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Authentication
from jupyterhub.auth import DummyAuthenticator
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = "admin"
c.Authenticator.allow_all = True
# User list - use lists instead of sets to ensure proper serialization
c.Authenticator.allowed_users = ["gary", "nicho", "augusto"]
c.Authenticator.admin_users = ["gary"]

# Suppress the warning about no allow config
c.Authenticator.any_allow_config = True

# Admin access
c.JupyterHub.admin_access = True

# API tokens
c.JupyterHub.api_tokens = {
    "gary-token": "gary",
    "nicho-token": "nicho",
    "augusto-token": "augusto",
}

# Docker spawner config
import os
from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner

# Get the network name from environment variable or use default
network_name = os.environ.get("DOCKER_NETWORK_NAME", "jupyterhub-network")

c.DockerSpawner.image = "jupyter-lab"
c.DockerSpawner.remove_containers = True

# Remplacer cette section
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': {'bind': '/home/jovyan/work', 'mode': 'rw'},
}

# Container name pattern - fix the formatting
c.DockerSpawner.name_template = "jupyter-{username}"

# IMPORTANT: Use the correct network name here
c.DockerSpawner.network_name = network_name

# Use the Docker host's network - also update the network mode here
c.DockerSpawner.extra_host_config = {
    'network_mode': network_name
}

# Environment variables for spawned containers
c.DockerSpawner.environment = {
    'JUPYTER_ENABLE_LAB': 'yes',
    'GRANT_SUDO': 'yes',  # Accorder sudo aux utilisateurs
    'NB_UID': '1000',
    'NB_GID': '100',
}

# Vous pouvez aussi faire démarrer le conteneur en tant que root
c.DockerSpawner.container_user = 'root'  # Utilisez container_user au lieu de user

# Set the notebook directory
c.Spawner.notebook_dir = '/home/jovyan/work'
c.Spawner.default_url = '/lab'

# Debug logging
c.JupyterHub.log_level = 'DEBUG'

# Ensure data directory exists
data_dir = "/data"
os.makedirs(data_dir, exist_ok=True)

# Store data in the mounted volume
c.JupyterHub.cookie_secret_file = os.path.join(data_dir, 'jupyterhub_cookie_secret')
c.JupyterHub.db_url = 'sqlite:///' + os.path.join(data_dir, 'jupyterhub.sqlite')

# Configuration pour le proxy et routage des requêtes
# IMPORTANT: Changed this from the literal {username} to use string formatting
c.DockerSpawner.prefix = '/user/{username}'  # This is correct, DockerSpawner will replace {username}

c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.ConfigurableHTTPProxy.api_url = 'http://jupyterhub:8001'
c.ConfigurableHTTPProxy.should_start = True

# Important: assurez-vous que ces lignes sont activées
c.Spawner.default_url = '/lab'
c.Spawner.cmd = ['jupyter-labhub']

# Ajouter ceci à la fin de votre fichier de configuration
c.DockerSpawner.post_start_cmd = "chmod -R 777 /home/jovyan/work"

c.DockerSpawner.mem_limit = '2G'
c.DockerSpawner.cpu_limit = 2.0