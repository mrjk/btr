# Development notes

### Command line

```
btr -c tests/data1.yml start fullhouse
btr -c tests/data1.yml stop fullhouse
```
### Resources

Useful resources:
* https://www.electricmonk.nl/docs/dependency_resolving_algorithm/dependency_resolving_algorithm.html

### Devel diary

Development time: 6h30

Phase 1: (2h15)
* 15:00:
  * Start the project, read the exercise and understand the problem
  * Look for a lib to solve the dependency problem: mixology adn python-graph-logger
  * Look for article about dependency algorithms
* 15:40:
  * Base python project created: setup.py
* 16:00:
  * Base command line implemented: CLI and Yaml import
  * Start poc about dependency resolution
* 16:30:
  * First version of resolver works
  * Clean and refactor the code
* 17:00:
  * First poc for multithreaded workers
* 17:15:
  * break

Phase 2: (1h15)
* 18:00:
  * Running into logging issues
* 18:30:
  * Resolved logging issues
  * Clean a bit the code
* 19:00:
  * Implement first version of the stop services
* 19:15:
  * Wip on stop


Phase 3: (3h00)
* 22:00:
  * Document project development
* 22:15:
  * Fix the stop process, implement the children and parent concept
* 23:00:
  * Both start and stop works as expected \o/
* 23:45:
  * Cleaned and refactorized the code
* 00:30:
  * Exception handling and tests
* 01:00:
  * Polishing project, readme and publish
