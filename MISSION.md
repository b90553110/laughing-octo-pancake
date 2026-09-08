# Mission: Spring (with Maven)

> **Status: provisional.** Sharpen this once there is a concrete thing to build.
> A vague mission produces abstract lessons — see the note at the bottom.

## Why

Become genuinely fluent in Spring Boot, with Claude teaching in the register of a
tech lead: not just how to make it work, but why it is built this way, what to
look for in review, and where it breaks at 3am. Starting from a solid Java base
and no Spring experience.

## Success looks like

- Can create, run and test a Spring Boot service from scratch, without a tutorial.
- Can read an unfamiliar `pom.xml` and explain what every element is doing.
- Can explain dependency injection to someone else, and say why constructor
  injection is preferred.
- Can diagnose the common failures alone: 404 on a route, port in use, version
  conflicts, imports that will not resolve.
- Can read an existing Spring codebase and follow a request from HTTP to database.

## Constraints

- **Maven, not Gradle.** Explicit preference.
- Teaching voice: tech lead to new engineer. Reasons and trade-offs, not just steps.
- New to Spring; comfortable writing Java.
- Lessons are read on a phone as often as a laptop, via GitHub Pages.

## Out of scope

- Gradle.
- Kotlin.
- Reactive Spring (WebFlux) until the servlet model is solid.
- Cloud deployment specifics — first make it run locally and be understood.

---

## Open question for the next session

This mission says "learn Spring well", which is honest but weak: it gives no way
to choose between teaching REST APIs, data access, or security next, and it
cannot say when we are done. It gets much sharper with an answer to:

> **What is the first Spring thing you actually want to exist?**

An internal API your team needs, a side project, a service you are about to lead
work on. Once that is known, rewrite the Why and Success sections around it and
add a learning record noting the change.
