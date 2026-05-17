---
icon: lucide/container
---

# Docker :material-docker:{ .main-color }

The easiest and recommended way to deploy your Reservium stack is to use Docker Compose. This method ensures that all dependencies are correctly configured and isolated.

---

## :material-tray-arrow-down: Docker Compose

### Step 1. Install Docker and Docker Compose

The way that you install Docker and Docker Compose depends on your Linux distribution. You can find specific instructions for each component in the links below:

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/linux/)

After following the installation instructions, verify that Docker and Docker Compose are available by typing:

```bash
docker --version
docker compose version
```

---

### Step 2. Create an `.env` file

Create a project directory to store your environment configuration and Docker Compose files, then navigate inside:

```bash
mkdir reservium
cd reservium
```

Inside the `reservium` directory, create an `.env` file to customize your Reservium instance's details. Change it to match your own information:

```editorconfig
# Database
POSTGRES_DB=reservium
POSTGRES_USER=reservium
POSTGRES_PASSWORD=secretpassword

# Mail
MAIL__USERNAME=reservium@buk.cvut.cz
MAIL__PASSWORD=exampleapp123
MAIL__FROM_NAME=Reservium System

# Keycloak
KEYCLOAK__SERVER_URL=https://auth.buk.cvut.cz
KEYCLOAK__REALM=reservium
KEYCLOAK__CLIENT_ID=reservium-api
KEYCLOAK__CLIENT_SECRET=supersecret

# Google
GOOGLE__CLIENT_ID=example.apps.googleusercontent.com
GOOGLE__CLIENT_SECRET=example-secret

GOOGLE__PROJECT_ID=example-project-id
GOOGLE__PRIVATE_KEY_ID=example-private-key
GOOGLE__PRIVATE_KEY='-----BEGIN PRIVATE KEY-----\nexample-private-key\n-----END PRIVATE KEY-----\n'
GOOGLE__CLIENT_EMAIL=example-client-email
GOOGLE__CLIENT_ID=example-client-id
GOOGLE__CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/example-client-email.iam.gserviceaccount.com
```

!!! info "Initial Setup"
    For the first setup, you can copy the example above and replace only the `client_id` and `client_secret` fields with values from Google Cloud Console. All other fields can remain unchanged for initial testing and will be updated automatically by the application during authentication.

---

### Step 3. Create a Docker Compose file

Create a `compose.yaml` file and paste the following content:

```yaml
---
services:
  db:
    container_name: db
    image: postgres:latest
    restart: on-failure
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql
    networks:
      - internal

  reservium-api:
    container_name: reservium-api
    image: ghcr.io/cloudrader/reservium-api:latest
    environment:
      ORGANIZATION_NAME: "Your organization name"

      DB__POSTGRES_USER: ${POSTGRES_USER}
      DB__POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      DB__POSTGRES_DB: ${POSTGRES_DB}
      DB__POSTGRES_SERVER: db

      MAIL__USERNAME: ${MAIL__USERNAME}
      MAIL__PASSWORD: ${MAIL__PASSWORD}
      MAIL__FROM_NAME: ${MAIL__FROM_NAME}
      MAIL__SENT_DORMITORY_HEAD: true  # defalt false
      MAIL__DORMITORY_HEAD_EMAIL: example@gmail.com

      KEYCLOAK__SERVER_URL: ${KEYCLOAK__SERVER_URL}
      KEYCLOAK__REALM: ${KEYCLOAK__REALM}
      KEYCLOAK__CLIENT_ID: ${KEYCLOAK__CLIENT_ID}
      KEYCLOAK__CLIENT_SECRET: ${KEYCLOAK__CLIENT_SECRET}

      GOOGLE__PROJECT_ID: ${GOOGLE__PROJECT_ID}
      GOOGLE__PRIVATE_KEY_ID: ${GOOGLE__PRIVATE_KEY_ID}
      GOOGLE__PRIVATE_KEY: ${GOOGLE__PRIVATE_KEY}
      GOOGLE__CLIENT_EMAIL: ${GOOGLE__CLIENT_EMAIL}
      GOOGLE__CLIENT_ID: ${GOOGLE__CLIENT_ID}
      GOOGLE__CLIENT_X509_CERT_URL: ${GOOGLE__CLIENT_X509_CERT_URL}

    depends_on:
      - db
    restart: on-failure
    ports:
      - "8000:8000"
    networks:
      - internal

  reservium-ui:
    container_name: reservium-ui
    image: ghcr.io/cloudrader/reservium-ui:latest
    ports:
      - "3000:3000"
    networks:
      - internal

networks:
  internal:

volumes:
  postgres_data:
```

---

## :material-layers-outline: Component Breakdown

The Docker Compose file defines **three containers** that form the Reservium stack:

**1. `db` (PostgreSQL)**
- Stores all application data (reservations, services, users, etc.)
- Data is persisted in the `postgres_data` Docker volume.

**2. `reservium-api`**
- The backend API responsible for business logic, authentication, and integrations.
- Handles database connections, email settings, and external sync (Keycloak, Google Calendar).

**3. `reservium-ui`**
- The frontend web interface.
- Communicates internally with the API container.

!!! warning "Security"
    All sensitive values should be defined in a `.env` file and **must not be committed to version control**.

---

### Step 4. Start Docker Compose

Start Reservium by running:

```bash
docker compose up -d
```

**🚀 The system will automatically:**

- Start PostgreSQL and run database migrations.
- Launch the backend API on port 8000.
- Launch the frontend on port 3000.

**You can access:**

- **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Frontend**: [http://localhost:3000](http://localhost:3000)

To stop the containers, use:
```bash
docker compose stop
```
