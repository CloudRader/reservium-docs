# Manager FAQ :fontawesome-solid-circle-question:{ .main-color }

This section addresses common questions specific to the manager role. If you have a general question about using the system, please check the [User FAQ](../../user-guide/faq/index.md).

---

## :fontawesome-solid-clipboard-check: Reservation Management

??? question "How quickly should I approve reservations?"
    While there is no system-enforced limit, we recommend reviewing "Not Approved" requests within **24 hours**. Prompt responses improve the user experience and allow people to plan their events effectively.

??? question "Can I approve a reservation that has a time conflict?"
    The system will warn you if a collision is detected. While managers have the authority to override some rules, it is generally recommended to resolve the conflict by communicating with the users involved via **Manager Observations**.

??? question "What happens if I decline a time change request?"
    If you decline a time change, the reservation **reverts to its original time slot**. The user will receive an email notification explaining the decision (if you provided an observation).

---

## :fontawesome-solid-sliders: Service Configuration

??? question "I am a manager, but I can't edit my service metadata. Why?"
    Top-level service metadata (like the room name or public visibility) is restricted to **Superusers** to maintain system-wide consistency. If you need to change these details, please contact your system administrator.

??? question "Can one calendar belong to multiple services?"
    No. Each calendar is strictly tied to a single parent service. However, you can create similar calendars across multiple services if needed.

??? question "How do I temporarily disable a room for maintenance?"
    The best way is to **Soft Delete** the associated calendars. This prevents new bookings immediately while preserving all historical data and existing reservations.

---

## :fontawesome-solid-envelope-open-text: Communication

??? question "Do users see my 'Manager Observations'?"
    **Yes.** Observations are explicitly designed for communication. They are included in the automated emails sent to users after you approve, decline, or edit their reservations.

??? question "Can I send a custom email to all users of my service?"
    Reservium currently handles automated transactional emails. For bulk communication, we recommend using your organization's standard mailing lists.
