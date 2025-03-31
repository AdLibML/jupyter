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
c.Authenticator.allowed_users = ["user1", "user2"]
c.Authenticator.admin_users = ["user1"]

# Suppress the warning about no allow config
c.Authenticator.any_allow_config = True
# Alternative: allow any user who can authenticate
# c.Authenticator.allow_all = True

# Admin access
c.JupyterHub.admin_access = True

# API tokens
c.JupyterHub.api_tokens = {
    "user1-token": "user1",
    "user2-token": "user2",
}

# Docker spawner config
from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.image = "jupyter-lab"
c.DockerSpawner.remove_containers = True
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': '/home/jovyan/work'
}
c.DockerSpawner.network_name = "jupyterhub-network"
c.DockerSpawner.debug = True

# Explicitly set Docker client args
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {
    'network_mode': 'jupyterhub-network'
}

# Environment variables for spawned containers
c.DockerSpawner.environment = {
    'JUPYTER_ENABLE_LAB': 'yes',
    'GRANT_SUDO': 'no',
}

# Set the notebook directory
c.Spawner.notebook_dir = '/home/jovyan/work'
c.Spawner.default_url = '/lab'

# Debug logging
c.JupyterHub.log_level = 'DEBUG'