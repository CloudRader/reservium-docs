# Docker

## Docker Compose

The easiest and recommended way to deploy your reservium stack is to use docker compose.

### Step 1. Install Docker and Docker Compose

The way that you install Docker and Docker Compose depends on your Linux distribution. You can find specific instructions for each component in the links below:

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/linux/)

After following the installation instructions, verify that Docker and Docker Compose are available by typing:

```bash
docker --version
docker compose version
```

### Step 2. Create an ```.env``` file

Create a project directory to store your n8n environment configuration and Docker Compose files and navigate inside:

```bash
mkdir reservium
cd reservium
```

Inside the ```reservium``` directory, create an ```.env``` file to customize your reservium instance's details. Change it to match your own information:

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

# SpiceDB
SPICEDB__CLIENT_SECRET=myspicedbsecret

# Google
GOOGLE__CLIENT_ID=example.apps.googleusercontent.com
GOOGLE__CLIENT_SECRET=example-secret

# Dormitory Access System
DORMITORY_ACCESS_SYSTEM__API_KEY=ABCDEFG1234567890
```

### Step 3. Create a ```token.json``` file

Inside your project directory, create a file named `token.json`.  
This file is used to authenticate with Google Calendar and allows the application to access and manage calendar data.

The access token is refreshed automatically, so in most cases you do not need to update this file manually after the initial setup.

#### **Example ```token.json```**:

```json
{
  "token": "...",
  "refresh_token": "...",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "...",
  "client_secret": "...",
  "scopes": ["https://www.googleapis.com/auth/calendar"],
  "expiry": "2025-12-31T23:59:59Z"
}
```

**Initial setup**

For the first setup, you can copy the example above and replace only the following fields with values from Google Cloud Console:

- client_id
- client_secret

All other fields can remain unchanged for initial testing and will be updated automatically by the application during authentication.

### Step 4. Create a Docker Compose file

Create a ```docker-compose.yaml``` file. Paste the following in the file:

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
    image: darkrader/reservium-api:latest
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
      MAIL__DORMITORY_HEAD_EMAIL: develop@buk.cvut.cz

      KEYCLOAK__SERVER_URL: ${KEYCLOAK__SERVER_URL}
      KEYCLOAK__REALM: ${KEYCLOAK__REALM}
      KEYCLOAK__CLIENT_ID: ${KEYCLOAK__CLIENT_ID}
      KEYCLOAK__CLIENT_SECRET: ${KEYCLOAK__CLIENT_SECRET}

      SPICEDB__CLIENT_SECRET: ${SPICEDB__CLIENT_SECRET}

      GOOGLE__CLIENT_ID: ${GOOGLE__CLIENT_ID}
      GOOGLE__CLIENT_SECRET: ${GOOGLE__CLIENT_SECRET}

      DORMITORY_ACCESS_SYSTEM__API_KEY: ${DORMITORY_ACCESS_SYSTEM__API_KEY}
    volumes:
      - ./token.json:/usr/src/app/src/token.json
    depends_on:
      - db
    restart: on-failure
    ports:
      - "8000:8000"
    networks:
      - internal

  reservium-ui:
    container_name: reservium-ui
    image: darkrader/reservium-ui:latest
    ports:
      - "3000:3000"
    networks:
      - internal

networks:
  internal:

volumes:
  postgres_data:
```

!!! warning 

    Add information about containers and ENVS!!!


### Step 5. Start Docker Compose

Start reservium by typing:

```bash
docker compose up -d
```

**🚀 The system will automatically:**

- Start PostgreSQL
- Run database migrations
- Launch the backend API on port 8000
- Launch the frontend on port 3000

**You can access:**

- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:3000

To stop the containers, type:

```bash
docker compose stop
```
