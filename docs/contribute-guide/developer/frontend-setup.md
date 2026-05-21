---
icon: lucide/monitor
---

# Frontend Setup :fontawesome-solid-desktop:{ .main-color }

This guide will help you set up the **Reservium UI** (Frontend) for local development.

---

## :fontawesome-solid-list-check: Prerequisites

Before you begin, ensure you have the following tools installed:

*   :fontawesome-brands-node-js: **Node.js (v20+)**: For Frontend development.

---

## :fontawesome-solid-layer-group: 1. Clone the Repository

Fork and clone the frontend repository:

```bash
git clone https://github.com/YOUR_USERNAME/reservium-ui.git
cd reservium-ui
```

---

## :fontawesome-solid-play: 2. Set Up and Run

### Step A: Install Dependencies
Navigate to the project directory and install the required packages:

```bash
npm install
```

### Step B: Start Development Server
Launch the application:

```bash
npm start
```

The app will be available at [http://localhost:3000](http://localhost:3000).

---

## :fontawesome-solid-code-branch: 3. Branching & Commit Strategy

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

1.  **Create a branch**: Use a descriptive name starting with the type, e.g., `feat/ui-dashboard-fix`.
2.  **Commit changes**: Use the types above. This allows us to automatically generate changelogs and manage version tags.
3.  **Push to your fork** and create a **Pull Request**.

---

## :fontawesome-solid-circle-info: Need Help?

If you encounter any issues, please reach out via email.
