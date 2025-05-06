c = get_config()

# -- Basic JupyterHub settings --
c.JupyterHub.ip            = '0.0.0.0'
c.JupyterHub.port          = 8000
c.JupyterHub.admin_access  = True

# -- Authentication --
from jupyterhub.auth import DummyAuthenticator
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password     = "admin"
c.Authenticator.any_allow_config   = True
c.Authenticator.allowed_users      = ["gary", "nicho", "augusto"]
c.Authenticator.admin_users        = ["gary"]

# -- API tokens (optionnel) --
c.JupyterHub.api_tokens = {
    "gary-token":   "gary",
    "nicho-token":  "nicho",
    "augusto-token":"augusto",
}

# -- Use KubeSpawner to launch per-user pods in Kubernetes --
from kubespawner import KubeSpawner
c.JupyterHub.spawner_class = KubeSpawner

# Namespace & service account where pods will be created
c.KubeSpawner.namespace        = 'jupyterhub'
c.KubeSpawner.service_account  = 'jupyterhub'

# Image built locally in minikube / local cluster
c.KubeSpawner.image            = "jupyter-lab:local"
c.KubeSpawner.image_pull_policy = 'Never'

# Resource requests & limits
c.KubeSpawner.cpu_guarantee = 0.5
c.KubeSpawner.cpu_limit     = 2.0
c.KubeSpawner.mem_guarantee = '1G'
c.KubeSpawner.mem_limit     = '2G'

# Persistent storage: auto-create PVCs named jupyterhub-user-{username}-extra
c.KubeSpawner.user_storage_pvc_ensure = True
c.KubeSpawner.user_storage_capacity   = '5Gi'
c.KubeSpawner.pvc_name_template       = 'jupyterhub-user-{username}-extra'
c.KubeSpawner.volumes = [{
    'name': 'user-data',
    'persistentVolumeClaim': {
        'claimName': c.KubeSpawner.pvc_name_template
    }
}]
c.KubeSpawner.volume_mounts = [{
    'name':      'user-data',
    'mountPath': '/home/jovyan/work'
}]

# Environment variables in each spawned pod
c.KubeSpawner.environment = {
    'JUPYTER_ENABLE_LAB': 'yes',
    'GRANT_SUDO':         'yes',
    'NB_UID':             '1000',
    'NB_GID':             '100'
}

# Single-user server options
c.Spawner.default_url   = '/lab'
c.Spawner.notebook_dir  = '/home/jovyan/work'
c.Spawner.cmd           = ['jupyter-labhub']

# Debug logging
c.JupyterHub.log_level = 'DEBUG'