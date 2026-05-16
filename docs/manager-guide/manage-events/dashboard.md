---
icon: lucide/layout-dashboard
---

# Manager Dashboard :fontawesome-solid-table-columns:{ .main-color }

The **Manager Dashboard** provides a unified view of all reservation activity. It is designed to help you quickly identify requests that need your attention and keep track of confirmed bookings.

---

## :fontawesome-solid-layer-group: Dashboard Tabs

At the top of the page, you'll find navigation tabs that group reservations by their lifecycle state. These filters allow you to focus on specific management tasks.

| Tab | Purpose |
| :--- | :--- |
| **My Events** | Your personal reservations (same as the [User Dashboard](../../user-guide/basic-features/dashboard.md)). |
| **Not Approved** | High priority! Requests waiting for your initial confirmation. |
| **Update Requested** | Existing reservations where users have proposed a time change. |
| **Confirmed** | Future view of all active, approved bookings. |
| **Canceled** | Records of all events that were declined or withdrawn. |

---

## :fontawesome-solid-user-clock: My Events

The **My Events** tab functions just like the standard user dashboard, showing your own personal activity.

### Upcoming & Past Events
Track what you have booked personally. Each card provides a snapshot of the service, time, and status.

![Upcoming Events](assets/my-events.png)

---

## :fontawesome-solid-list-check: Status-Specific Tabs

### :fontawesome-solid-hourglass-half: Not Approved
This is your primary work queue. It contains reservations that **cannot be confirmed automatically** due to room rules (e.g., large groups or restricted hours).

![Not Approved](assets/not-approved-events.png)

- **Action Required**: Managers should [**Approve or Decline**](review-reservations.md#reviewing-pending-approvals) these as soon as possible.
- **Impact**: No access or confirmation is granted to the user until you take action.

---

### :fontawesome-solid-calendar-plus: Update Requested
Shows reservations where a user has requested a modification.

![Update Request](assets/update-events.png)

- **Grace Period**: The original reservation remains valid until you confirm the change.
- **Action**: You can [**Approve or Decline time changes**](review-reservations.md#reviewing-time-changes).

---

### :fontawesome-solid-calendar-check: Confirmed
A complete list of all successful bookings.

![Confirmed](assets/confirmed-events.png)

- **Visibility**: Essential for checking who is currently using a space.
- **Management**: Managers can still [**Edit or Cancel**](review-reservations.md#editing-and-canceling) these if organizational needs change.

---

## :fontawesome-solid-users-gear: Role Capabilities

| Feature | Regular User | Manager |
| :--- | :---: | :---: |
| View own reservations | :fontawesome-solid-check: | :fontawesome-solid-check: |
| Request time changes | :fontawesome-solid-check: | :fontawesome-solid-check: |
| **Review others' requests** | :fontawesome-solid-xmark: | :fontawesome-solid-check: |
| **Edit any reservation** | :fontawesome-solid-xmark: | :fontawesome-solid-check: |
| **Provide observations** | :fontawesome-solid-xmark: | :fontawesome-solid-check: |

!!! info "Observations"
    When you update a reservation, you can add a **Manager Observation**. This text is included in the automated email sent to the user, providing context for your decision.

---

## :fontawesome-solid-arrow-right-long: What’s Next?

Ready to take action? Learn the details of the review process:

- **[Reviewing Pending Approvals](review-reservations.md)**
- **[Handling Time Changes](review-reservations.md#reviewing-time-changes)**
