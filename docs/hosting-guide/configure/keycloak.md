# How to configure SSO with Keycloak

!!! warning "DEMO CONFIGURATION" 

    This documentation includes examples from a demo environment for informational purposes only. Adapt the configuration values (domains, ports, credentials) to match your specific setup.

Reservium supports SSO via OpenID Connect (OIDC). This guide shows how to configure SSO with Keycloak as an example.

## How does it work?

Reservium SSO uses Keycloak OAuth2/OpenID Connect. When a user logs in through Keycloak, they unlock a server-side key needed to decrypt their secret key passphrase.

## Prerequisites

You need the following to configure Keycloak SSO with Reservium:

- A running Keycloak instance (version 26.4 or later)
- Access to Keycloak and Reservium server where they run

!!! info "KEYCLOAK VERSION" 

    This guide uses Keycloak 26.4. Use a specific version rather than latest for consistency: quay.io/keycloak/keycloak:26.4.

## Configuration

### Step 1: Configure Keycloak

**Create a Keycloak Realm**

1. Navigate to your Keycloak instance (e.g., ```https://keycloak.local:8443```)
2. Log in with the admin credentials:
    - **Username**: `admin`
    - **Password**: `admin`
3. Navigate to the dropdown in the top-left corner and click "`Create realm`"
4. Enter a realm name (e.g., "reservium")
5. Click "**Create**"

**Create a Keycloak Client**

1. In your newly created realm, go to "**Clients**" in the left menu
2. Click "**Create client**"
3. Configure the client:
    - Client type: OpenID Connect
    - Client ID: reservium-client (or your preferred name)
    - Click "Next"
    - Configure client settings:
4. Client authentication: On
    - Authorization: Off
    - Authentication flow: Standard flow
    - Click "Next"
5. Configure login settings:
    - Root URL: Leave empty
    - Home URL: Leave empty
    - Valid redirect URIs: Add your Reservium redirect URI (get this from Reservium's SSO configuration page)
    - Web origins: https://reservium.local
    - Click "Save"

**Configure Client Credentials**

1. In the client settings, go to the "**Credentials**" tab
2. Copy the **Client secret** value - you'll need this for Reservium configuration

**Create a Test User**

1. Go to "**Users**" in the left menu
2. Click "**Create new user**"
3. Fill in the user details:
    - Username: Choose a username
    - Email: Use an email that exists in Passbolt
    - First name and Last name: Fill as desired
    - Email verified: Toggle to "On"
    - Click "Create"
4. Set a password for the user:
    - Go to the "**Credentials**" tab
    - Click "**Set password**"
    - Enter a password and confirm it
    - Toggle "**Temporary**" to "Off"
    - Click "**Save**"