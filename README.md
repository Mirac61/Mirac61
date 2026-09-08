<p align="center">
  <img src="./.github/assets/mirac.svg" alt="mirac" width="420">
</p>

Software engineering student at Hochschule Esslingen, 5th semester. I mostly write
backend services in Go and Java/Spring Boot, and I gravitate towards the parts where
being wrong is expensive: money, state, things you can't quietly get wrong.

**Suche eine Werkstudentenstelle (20 h/Woche) im Raum Stuttgart, idealerweise mit der Option, dort ab Sommersemester 2027 auch das Pflichtpraktikum (ca. 5 Monate) zu absolvieren.**

## Projects

**[VentoryGo](https://github.com/Mirac61/VentoryGo)** | invoicing backend · Go, Gin, PostgreSQL, Docker

Invoicing service for small businesses. Amounts are stored as `int64` cents and VAT
as basis points, so no float ever touches the money, and invoices are never deleted —
a cancellation writes a credit note, which keeps the books auditable. The document
model leaves room for ZUGFeRD/XRechnung output. Sessions use Argon2id with rate
limiting on the auth endpoints; PDFs are generated server-side.
Unit tests cover the money paths: rounding, VAT calculation, credit notes.

**[Aktivitätstracker](https://github.com/Mirac61/activitytracker)** | Android client and Spring Boot backend · Kotlin, Java, Keycloak

Team project for 5 people over one semester. Offline-first: the client writes
locally and reconciles through WorkManager, so the app stays usable without network.
Auth via Keycloak, CI builds and signs release APKs on tag. I worked on the offline sync between the local and remote database, the statistics feature, and the release pipeline.

**[mysh](https://github.com/Mirac61/mysh)**  | Unix shell · C++

Interactive shell built directly on `fork()`, `exec()`, `pipe()` and `dup2()`.
Pipelines, redirections, signal handling, tab completion. No leaks reported under Valgrind.

## Stack

<p>
    Almost daily:
  <img src="https://img.shields.io/badge/Go-1F1F28?style=flat-square&logo=go&logoColor=7E9CD8" alt="Go" />
  <img src="https://img.shields.io/badge/Gin-1F1F28?style=flat-square&logo=gin&logoColor=98BB6C" alt="Gin" />
  <img src="https://img.shields.io/badge/PostgreSQL-1F1F28?style=flat-square&logo=postgresql&logoColor=E6C384" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-1F1F28?style=flat-square&logo=docker&logoColor=E6C384" alt="Docker" />
  <img src="https://img.shields.io/badge/Linux-1F1F28?style=flat-square&logo=linux&logoColor=957FB8" alt="Linux" />
</p>

<p>
    Used in projects:
  <img src="https://img.shields.io/badge/Java-1F1F28?style=flat-square&logo=openjdk&logoColor=7E9CD8" alt="Java" />
  <img src="https://img.shields.io/badge/Kotlin-1F1F28?style=flat-square&logo=kotlin&logoColor=7E9CD8" alt="Kotlin" />
  <img src="https://img.shields.io/badge/TypeScript-1F1F28?style=flat-square&logo=typescript&logoColor=7E9CD8" alt="TypeScript" />
  <img src="https://img.shields.io/badge/C%2B%2B-1F1F28?style=flat-square&logo=cplusplus&logoColor=7E9CD8" alt="C++" />
  <img src="https://img.shields.io/badge/Spring_Boot-1F1F28?style=flat-square&logo=springboot&logoColor=98BB6C" alt="Spring Boot" />
  <img src="https://img.shields.io/badge/Vue.js-1F1F28?style=flat-square&logo=vuedotjs&logoColor=98BB6C" alt="Vue.js" />
</p>

## Contact

<p>
  <a href="mailto:mi.sancak@proton.me"><img src="https://img.shields.io/badge/Email-1F1F28?style=flat-square&logo=maildotru&logoColor=E6C384" alt="Email" /></a>
  <a href="https://www.linkedin.com/in/mirac-sancak-47917238b/"><a href="https://www.linkedin.com/in/mirac-sancak-47917238b/"><img src="https://img.shields.io/badge/LinkedIn-1F1F28?style=flat-square&logo=linkedin&logoColor=7FB4CA" alt="LinkedIn" /></a>
</p>
