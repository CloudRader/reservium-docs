---
icon: lucide/server
---

# Backend Setup :fontawesome-solid-server:{ .main-color }

This guide will help you set up the **Reservium API** (Backend) for local development.

---

## :fontawesome-solid-list-check: Prerequisites

Before you begin, ensure you have the following tools installed:

*   :material-docker: **Docker & Docker Compose**: To run the PostgreSQL database.
*   :fontawesome-brands-python: **Python (3.12+)**: We recommend using [**uv**](https://docs.astral.sh/uv/) for package management.

---

## :fontawesome-solid-layer-group: 1. Clone the Repository

Fork and clone the backend repository:

```bash
git clone https://github.com/YOUR_USERNAME/reservium-api.git
cd reservium-api
```

---

## :fontawesome-solid-gears: 2. Configuration

### Step A: Configure Environment
Create a `.env` file in the root of the repository.

!!! info "External Services"
    Reservium requires Keycloak for authentication and Google for calendar synchronization.

    - **Keycloak**: Follow the [**Keycloak Configuration Guide**](../../hosting-guide/configure/keycloak.md) to set up your realm and client.
    - **Google**: You need to create a Service Account in the [Google Cloud Console](https://console.cloud.google.com/). Search for "Google Service Account setup" for detailed instructions on obtaining your credentials.

```editorconfig
# Database
POSTGRES_DB=reservium
POSTGRES_USER=reservium
POSTGRES_PASSWORD=secretpassword

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

### Step B: Start Database
Run the following command to start the PostgreSQL container:

```bash
docker compose up -d db
```

---

## :fontawesome-solid-play: 3. Run the API

Install dependencies and start the FastAPI development server:

```bash
uv sync
source .venv/bin/activate
cd reservation-app/src
uv run main.py
```

!!! tip "API Documentation"
    Once the backend is running, you can access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## :fontawesome-solid-vial: 4. Quality Control

Always run tests and linters before submitting a Pull Request:

```bash
cd reservation-app/
uv run ./scripts/pytest.sh
uv run ./scripts/lint_ruff.sh
uv run ./scripts/mypy.sh
```

---

## :fontawesome-solid-code-branch: 5. Branching & Commit Strategy

To maintain a clean project history and automate our release process with [**Release Please**](https://github.com/googleapis/release-please), we follow the [**Conventional Commits**](https://www.conventionalcommits.org/) specification.

### Commit Types

Every commit message should follow this pattern: `type: description` (or `type(scope): description`).

| Type | Section | Icon |
| :--- | :--- | :---: |
| `feat` | New Features | :fontawesome-solid-wand-magic-sparkles: |
| `chore` | Updates & Improvements | :fontawesome-solid-toolbox: |
| `fix` | Fixes | :fontawesome-solid-wrench: |
| `refactor` | Refactors | :fontawesome-solid-broom: |
| `docs` | Documentation | :fontawesome-solid-file-lines: |
| `test` | Tests & Quality | :fontawesome-solid-vial: |
| `ci` | DevOps & CI/CD | :fontawesome-solid-gears: |

### Workflow

1.  **Create a branch**: Use a descriptive name starting with the type, e.g., `feat/add-google-sync`.
2.  **Commit changes**: Use the types above. This allows us to automatically generate changelogs and manage version tags.
3.  **Push to your fork** and create a **Pull Request**.

---

## :fontawesome-solid-circle-info: Need Help?

Refer to the [**Hosting Guide**](../../hosting-guide/introduction/index.md) or contact us via email if you encounter any issues.
