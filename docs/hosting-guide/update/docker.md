---
icon: lucide/refresh-cw
---

# Update Reservium :material-update:{ .main-color }

Regularly updating your Reservium instance ensures you have the latest features, bug fixes, and security patches. This guide explains how to update your Docker-based deployment.

---

## :material-docker: Updating with Docker

It is recommended that users pull tags pointing to specific Reservium versions when running in production environments.

### Step 1. Update Image Tags

To update Reservium, change the image tag in your `compose.yaml` file for both the API and the UI:

```yaml
services:
  reservium-api:
    image: ghcr.io/cloudrader/reservium-api:<IMAGE_TAG>

  reservium-ui:
    image: ghcr.io/cloudrader/reservium-ui:<IMAGE_TAG>
```

---

### Step 2. Pull and Relaunch

After updating the tags, pull the latest images and restart your containers:

```bash
docker compose pull
docker compose up -d
```

!!! warning "The 'latest' Tag"
    The `latest` tag does not automatically keep your container up to date. You must run `docker compose pull` to fetch the newest image version before relaunching.

---

## :material-check-circle-outline: What Happens During Update?

By following these steps:

- A new Reservium Docker image will be pulled.
- A new container will be created based on the updated image.
- Your data (stored in volumes) remains safe and will be automatically migrated if necessary by the backend API.
