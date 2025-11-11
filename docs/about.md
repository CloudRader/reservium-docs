# About Reservium

Reservium is a **custom reservation system** originally developed for the **Buben Club (BUK)** dormitory, designed to streamline room booking and reduce administrative workload.  
It has since evolved from a semester project to a **Bachelor's thesis project** and is now a fully functional application with ambitions to grow into a **cloud-native SaaS platform**.

---

## 🎓 Origins

- Initially developed as a **Python semester project**.  
- Evolved into a **Bachelor’s thesis project**.  
- Currently maintained as a **personal project**, with ambitions to expand. 
- **Teamwork:** Backend developed by  [DarkRader](https://github.com/DarkRader); frontend fully developed by [](https://github.com/daniilk11). 

> 💡 The project demonstrates a natural progression from academic exercise to real-world application and sets the foundation for future SaaS expansion.

---

## 🌐 Key Features

Reservium provides an end-to-end solution for room reservations, with features including:

- **Authentication** through [Keycloak](https://www.keycloak.org)  
- **Event scheduling** with automatic **Google Calendar synchronization**  
- **Role-based access** and reservation rules  
- **Email notifications** for members and managers  
- Planned **RFID-based access control** for approved reservations  

> 🔮 Future plans include developing both **self-hosted and SaaS versions**, with cloud-native architecture and multi-tenant support.

---

## 🏗️ Architecture & Stack

- **Backend:** Python + FastAPI  
- **Frontend:** React-based UI ([Reservium UI](https://github.com/CloudRader/reservium-ui))  
- **Database:** PostgreSQL  
- **Authentication:** Keycloak (OAuth2/OpenID Connect)  
- **Scheduling:** Google Calendar API integration  
- **Access Control:** Future integration with RFID-based dormitory system  
- **DevOps:** Docker, Docker Compose, GitHub Actions, automated CI/CD  

> ⚠️ Current version is functional but still in **active development**; planned refactors will focus on SaaS readiness.

---

## 🏛️ Workflow Overview

1. **User Authentication:** Members login through Keycloak.  
2. **Reservation Creation:** Users select a room and timeslot via the intuitive web interface.  
3. **Automatic Scheduling:** Events are synced to Google Calendar.  
4. **Approval & Access:** Reservations are approved automatically or manually depending on rules. Future versions will include RFID access.  
5. **Notifications:** Email notifications sent to users and managers.

> 📌 The system ensures **role-specific rules**, **conflict prevention**, and **easy management** of reservations.

---

## 🚀 Project Vision

Reservium aims to become a **cloud-native SaaS** that provides:

- Self-hosted and cloud-hosted versions  
- Multi-tenant architecture for organizations of any size  
- Modular and scalable backend with API-first design  
- Advanced analytics, reporting, and automation features  

> 🔧 Currently, the platform is expanding beyond student dormitories to general-purpose organizational use.

---

## 📌 Notes

- Reservium is actively maintained and under continuous development.  
- Integration with additional services (RFID access, third-party APIs) is part of the long-term roadmap.  
- Contributions and suggestions are welcome!  

> 💡 Tip: For developers exploring the system, start with the [Getting Started](index.md) guide and the [API Reference]().