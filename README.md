<p align="center">
  <img src="./.github/assets/intro.gif" alt="mirac — terminal intro" width="760">
</p>

Software Engineering student at Hochschule Esslingen, 4th semester.
Java and Spring Boot as the foundation, Go as the thing I'm currently learning
properly rather than superficially. I'd rather understand a system before using it,
and write something small that works than something clever that impresses.

**Looking for an internship or working student position in the Stuttgart area from WS26.**

<br>

## Projects

### [VentoryGo](https://github.com/Mirac61/Invoice) — Invoice backend in Go

REST API built with Gin and PostgreSQL. Database access through pgx instead of an ORM,
migrations handled by golang-migrate. Money is stored as `int64` cents and VAT rates as
integer basis points — no floating point anywhere near the money logic. Cancellations
go through credit notes rather than deletions, so the document chain stays intact.

The biggest lesson was how much weight sits in decisions you can't reverse later.
Choosing against an ORM cost me two days of reading and turned out to be right.

### [mysh](https://github.com/Mirac61/mysh) — Unix shell in C++

Built from scratch: process management, pipes, redirects, signal handling, tab
completion. Straight against the syscalls — `fork()`, `exec()`, `pipe()`, `dup2()`,
no framework in between. Cold start around 9ms, no memory leaks under Valgrind.

Signal handling was the hard part. What is a single slide in a lecture turns into race
conditions that show up every twentieth run.

<br>

## Stack

**Daily:** Go · Java · Spring Boot · PostgreSQL · Docker
**Alongside:** TypeScript · Vue · Kotlin · C++
**Tooling:** Neovim · Git · GitHub Actions · Linux

<br>

## Connect

<p>
  <a href="https://www.linkedin.com/in/mirac-sancak-47917238b/"><img src="https://img.shields.io/badge/LinkedIn-1F1F28?style=flat-square&logo=linkedin&logoColor=7FB4CA" alt="LinkedIn" /></a>
</p>
