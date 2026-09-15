# Missions

This workspace runs **two tracks**, and therefore holds two missions.

> **Deviation from the skill, recorded deliberately.**
> `.claude/skills/teach/MISSION-FORMAT.md` states: "One mission per workspace. If
> the user wants to learn two unrelated things, that is two workspaces." The
> learner asked for both subjects on one published site, so this workspace keeps
> one repository and splits the mission per track instead. The rule's purpose —
> stopping an unfocused mission from producing abstract lessons — still holds,
> because each track below has its own goal and its own success criteria. Split
> into two repositories if a third track appears.

---

# Mission: Spring (with Maven)

> **Status: provisional.** Sharpen this once a concrete project exists.

## Why

Become fluent in Spring Boot, with Claude teaching in the register of a tech
lead: the reasons a thing is built this way, what to look for in review, and how
it fails in production. Starting from a solid Java base and no Spring experience.

## Success looks like

- Creates, runs and tests a Spring Boot service from scratch, without a tutorial.
- Reads an unfamiliar `pom.xml` and explains every element.
- Explains dependency injection to someone else, and why constructor injection wins.
- Diagnoses the common failures alone: 404 on a route, port in use, version
  conflicts, unresolved imports, migration checksum mismatches.
- Follows a request through an unfamiliar Spring codebase, from HTTP to database.

## Constraints

- **Maven, not Gradle.** Explicit preference.
- New to Spring; comfortable writing Java.

## Out of scope

- Gradle. Kotlin. Reactive Spring (WebFlux) until the servlet model is solid.

## Open question

Name the first Spring thing you want to exist — an API your team needs, a side
project, a service you are about to lead. That answer cuts the lesson queue
rather than extending it.

---

# Mission: Playwright (TypeScript, Angular)

## Why

Write end-to-end tests for an Angular application that fail only when the
application is genuinely broken. A suite that fails randomly gets ignored and
then deleted, so durability is the goal rather than coverage.

## Success looks like

- Writes a test for a new user journey without consulting a tutorial.
- Chooses locators that survive a component refactor.
- Diagnoses a CI-only failure from its trace rather than by re-running it.
- Judges which behaviour belongs in an end-to-end test and which belongs in an
  Angular component test.
- Keeps the suite fast enough that the team keeps reading its results.

## Constraints

- **TypeScript**, against an **Angular** front end. Angular Material components.
- Playwright's own test runner, not a third-party wrapper.

## Out of scope

- The Playwright Java binding. The learner chose TypeScript deliberately.
- Cross-browser matrices until one browser runs green reliably.
- Visual comparison testing until the functional suite is stable.

## Open question

Does this Angular application call the Spring service from the other track, or a
different back end? If the two connect, the tracks share a test environment and
the seed-data strategy from Spring Lesson 04 serves both.
