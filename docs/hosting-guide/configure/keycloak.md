---
icon: lucide/key-round
---

# Keycloak Configuration :fontawesome-solid-key:{ .main-color }

!!! warning "DEMO CONFIGURATION"
    This documentation includes examples from a demo environment for informational purposes only. Adapt the configuration values (domains, ports, credentials) to match your specific setup.

Reservium supports SSO via OpenID Connect (OIDC). This guide shows how to configure SSO with Keycloak as an example.

---

## :material-cog-outline: How does it work?

Reservium SSO uses Keycloak OAuth2/OpenID Connect. When a user logs in through Keycloak, they unlock a server-side key needed to decrypt their secret key passphrase.

---

## :material-clipboard-check-outline: Prerequisites

You need the following to configure Keycloak SSO with Reservium:

- A running **Keycloak instance** (version 26.4 or later).
- Access to the Keycloak admin panel and the Reservium server.

!!! info "Keycloak Version"
    This guide uses Keycloak 26.4. It is recommended to use a specific version rather than `latest` for consistency: `quay.io/keycloak/keycloak:26.4`.

---

## :material-format-list-numbered: Configuration Steps

### Step 1: Configure Keycloak

**Create a Keycloak Realm**

1. Navigate to your Keycloak instance (e.g., `https://keycloak.local:8443`).
2. Log in with admin credentials.
3. In the top-left dropdown, click **Create realm**.
4. Enter a realm name (e.g., `reservium`) and click **Create**.

**Create a Keycloak Client**

1. In your new realm, go to **Clients** -> **Create client**.
2. **Client type**: `OpenID Connect`.
3. **Client ID**: `reservium-client`.
4. **Client authentication**: `On`.
5. **Authentication flow**: `Standard flow`.
6. **Valid redirect URIs**: Add your Reservium redirect URI.
7. **Web origins**: `https://reservium.local`.
8. Click **Save**.

**Configure Client Credentials**

1. In the client settings, go to the **Credentials** tab.
2. Copy the **Client secret** - you will need this for Reservium configuration.

**Create a Test User**

1. Go to **Users** -> **Create new user**.
2. Fill in details (Username, Email, etc.) and set **Email verified** to `On`.
3. In the **Credentials** tab, click **Set password**.
4. Set a password and toggle **Temporary** to `Off`.

---

### Step 2: Configure Reservium Environment Variables

1. Connect to your Reservium server.
2. Open your `.env` file and add the following variables:

```editorconfig
KEYCLOAK__SERVER_URL=https://keycloak.example.com:8443
KEYCLOAK__REALM=your.realm
KEYCLOAK__CLIENT_ID=reservium-app
KEYCLOAK__CLIENT_SECRET=your-secret
```

3. Restart the Docker containers:

```bash
docker compose down
docker compose up -d
```

---

### Step 3: Verify Configuration

1. Open the Reservium login page and click the login button.
2. Confirm that you are redirected to Keycloak and can authenticate successfully.
3. Ensure you have access to the Reservium dashboard after logging in.
