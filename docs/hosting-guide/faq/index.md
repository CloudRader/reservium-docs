# Hosting FAQ :material-help-circle-outline:{ .main-color }

This section addresses common questions related to self-hosting and maintaining your Reservium instance. For general usage questions, please refer to the [User FAQ](../../user-guide/faq/index.md).

---

## :material-server-network: Server & Deployment

??? question "Can I run Reservium without Docker?"
    While Docker is the recommended method for its ease of use and isolation, you can theoretically run the Python backend and React frontend manually. However, this is not officially supported and requires manual dependency management.

??? question "What are the minimum hardware requirements?"
    Reservium is lightweight. A server with **1 vCPU and 2GB of RAM** is usually sufficient for small to medium organizations.

---

## :material-shield-lock-outline: Security & Auth

??? question "Is HTTPS required?"
    **Yes.** For security and proper function of SSO (Keycloak/Google), Reservium should always be served over HTTPS. We recommend using a reverse proxy like Nginx or Traefik with Let's Encrypt.

??? question "Can I use an external PostgreSQL database?"
    Absolutely. Simply update the `DB__*` environment variables in your `.env` file to point to your external database instance.
