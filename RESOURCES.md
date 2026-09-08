# Spring & Maven Resources

Sources for teaching are drawn from here, not from the model's memory. Spring
moves fast enough that recalled knowledge is frequently a version or two stale —
the Boot 4 test-slice move in [Lesson 01](lessons/0001-spring-boot-maven-first-service.html)
is a live example.

## Knowledge

- [Spring Boot reference documentation](https://docs.spring.io/spring-boot/)
  The primary source. Versioned — check you are reading the docs for the version
  in your `pom.xml`. Use for: anything where being right matters more than being quick.
- [System Requirements](https://docs.spring.io/spring-boot/system-requirements.html)
  Java, Maven and Gradle baselines per release. Use for: choosing versions at project start.
- [Spring Boot Maven Plugin docs](https://docs.spring.io/spring-boot/maven-plugin/index.html)
  What `spring-boot:run` and `repackage` actually do. Use for: build behaviour questions.
- [Spring Guides](https://spring.io/guides)
  Short official getting-started guides, maintained by the Spring team. Use for:
  a first pass at an unfamiliar area (REST, JPA, security).
- [Spring Boot 4.0 Migration Guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide)
  What changed from Boot 3. Use for: decoding older tutorials that no longer compile.
- [Maven: The Complete Reference / Maven docs](https://maven.apache.org/guides/)
  Use for: lifecycle, scopes, and dependency resolution rules.
- [Baeldung](https://www.baeldung.com/)
  Large, generally careful Spring tutorial site. Use for: a second explanation when
  the reference docs are terse. Always check the article's date and version.

## Wisdom (Communities)

- [r/java](https://reddit.com/r/java) and [r/SpringBoot](https://reddit.com/r/SpringBoot)
  Use for: sanity-checking an approach, and seeing what people actually run in production.
- [Stack Overflow: spring-boot tag](https://stackoverflow.com/questions/tagged/spring-boot)
  Use for: specific errors. Sort by newest when the answer might be version-dependent.
- [Spring Boot GitHub issues](https://github.com/spring-projects/spring-boot/issues)
  Use for: confirming whether surprising behaviour is a known bug. High signal.

## Gaps

- No book selected yet. Worth choosing one once the mission is concrete — a book
  gives a spine that scattered tutorials do not.
- No community preference recorded. Ask whether joining one is wanted at all.
- No source yet for the *architectural* side (service boundaries, testing strategy)
  that the tech-lead framing will eventually need.
