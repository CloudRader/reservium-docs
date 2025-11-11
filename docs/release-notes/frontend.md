# Frontend Release Notes

## v2.0.0

### 🚀 Reservium Frontend v2.0.0 — Major Update

Complete frontend modernization featuring seamless Keycloak authentication, a faster Vite build system, and an
intuitive, enhanced interface for event and reservation management.

---

#### ✨ New Features

- ✅ **Manager Panel** — manage calendars, mini-services, and reservations in one unified workspace.
- ✅ **Event Dashboard** — view upcoming, past, and managed events, with tools to approve, decline, or request time
  changes.
- ✅ **Simplified Reservation Forms** — redesigned with dynamic fields, multi-checkbox support, and improved validation
  for smoother booking.
- ✅ **Improved Event Management** — users and managers can now track and modify event requests directly from the
  dashboard.
- ✅ **Public View Mode** — browse available calendars and services without logging in.
- ✅ **Enhanced Authentication Flow** — seamless login/logout via Keycloak with improved security.
- ✅ **Performance Upgrades** — faster load times, smoother transitions, and cleaner app flow.

---

#### ✴️ Updates & Improvements

- ✴️ Updated all service and calendar edit views with a consistent design and improved UX.
- ✴️ Improved data fetching using React Query and standardized API handling.
- ✴️ Unified time and date formatting for clarity across the UI.
- ✴️ Refined dashboard layout and responsiveness using Tailwind’s grid system.
- ✴️ Migrated build system from **CRA** to **Vite** for faster development and smaller bundles.
- ✴️ Added **ESLint** and **Prettier** for consistent code formatting.
- ✴️ Updated **TailwindCSS** configuration with custom utilities for layouts.
- ✴️ Improved caching and API proxy configuration for smoother data handling.
- ✴️ Updated folder structure and `.gitignore` for cleaner project organization.
- ✴️ Integrated frontend with GitHub Actions for automated builds and Docker image publishing.

---

#### 🧹 Refactoring

- 🧹 Reorganized the component structure for better maintainability and clarity.
- 🧹 Refactored form logic into reusable hooks (`useReservationFormLogic`, `useCreateFormLogic`, `useSlotSync`).
- 🧹 Streamlined route structure — separated logic for user, manager, and public views.
- 🧹 Cleaned codebase — removed unused components, optimized imports, and standardized naming.

---

#### 🛠️ Fixes

- 🛠️ Corrected API endpoints and environment variable handling.
- 🛠️ Fixed login, token refresh, and redirect issues.
- 🛠️ Resolved pagination, event filtering, and service display problems.
- 🛠️ Corrected registration form submission and validation errors.
- 🛠️ Reservation form no longer reloads on error — previously entered data now remains intact.
- 🛠️ Fixed event update and deletion logic for managers.
- 🛠️ Resolved minor layout issues across responsive breakpoints.

---

#### ❌ Removed / Deprecated

- ❌ **Legacy token management** replaced with Keycloak authentication.
- ❌ **Old reservation logic** in forms deprecated in favor of new hooks.
- ❌ **Deprecated components** removed: `useReservationLogic.js`, old `EventCard` mobile version, and unused helpers.
- ❌ **Old TailwindCSS configuration** replaced with updated custom utilities.
- ❌ **Commented-out routes and test components** removed from `App.js`.
- ❌ **Old form field handlers** deprecated; now consistently handled via `FormFieldRenderer` and associated hooks.

---

#### ⚙️ DevOps & CI/CD

- ✅ Automated **SemVer tagging** and image versioning
- ✅ Docker Hub publishing workflow integrated

---

#### 🏁 Summary

Reservium v2.0.0 is a **major milestone**, delivering:

- Modernized, maintainable frontend architecture
- Unified CI/CD pipelines with automated builds and Docker publishing
- Scalable authentication and permission management through Keycloak
- Enhanced event and reservation management with the **Manager Panel** and **Event Dashboard**
- Faster performance, improved UX, and consistent UI across all screens

---

**Released:** 25 October 2025  
**Maintainer:** [daniilk11]()

---

## v1.0.0

_No description_

---

