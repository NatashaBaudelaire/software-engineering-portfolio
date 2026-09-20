# Software Engineering Coursework

A personal portfolio of software engineering coursework: exercises, labs and
projects completed during a software engineering degree. Content is organized
by **knowledge domain** (software testing, database design, cloud computing,
…) and, within each domain, by content type (exercises, labs, notes, projects).

## Overview

This repository documents a progressive learning path across programming, data
modeling, testing, cloud infrastructure, data science and mobile development.
Everything is self-contained and source code is accompanied by its own tests
and documentation.

## Academic Context

The exercises and labs were completed during a Software Engineering degree
course. Folders follow the original course semantics (such as lesson topics),
and each area links to answers or solution notes where exercises were
answered. Original naming was kept where domain-appropriate so the work can be
traced back to the course curriculum.

## Technologies

- **Java** (JDK 8+) and **JUnit 5**
- **Python 3.10+** (including `match`/`case`)
- **SQL** and relational database modeling (conceptual, logical, physical)
- **Flutter / Dart** for mobile apps
- **Cloud tools**: Google Cloud Shell, Apache, FTP, HTTP traffic capture
- **Data science**: Jupyter, pandas, NumPy, Matplotlib, Seaborn
- **Artificial intelligence**: TensorFlow / Keras (practice with `.h5` models)

## Repository Structure

Top-level directories are **knowledge domains** of software engineering. Each
domain contains only the content types that exist for it (no empty folders).

```
artificial-intelligence/
  README.md             # Domain index
  exercises/            # Practice: working with .h5 / HDF5 ML models
  notes/                # Module notes and learning roadmap

cloud-computing/
  README.md             # Domain index
  labs/                 # Apache setup, FTP server, HTTP traffic analysis

database-design/
  README.md             # Domain index
  exercises/            # Conceptual, logical and physical data models

data-science/
  README.md             # Domain index
  datasets/             # Single source of truth for all notebooks' datasets
  projects/             # Jupyter notebooks: EDA, visualization, preprocessing

mobile-development/
  README.md             # Domain index
  projects/             # Flutter apps (counter app, widgets & app anatomy)

programming-languages/
  README.md             # Language-family index (languages ≠ frameworks)
  java/                 # Algorithms/logic + OOP (encapsulation, inheritance, ...)
  python/               # Algorithms/logic, functions, file handling

software-testing/
  README.md             # Domain index
  exercises/            # Manual testing, test case design, unit tests (JUnit 5)
```

Top-level directories are **knowledge domains** (or the programming-languages
family). Within each domain, content is organized by the activity type it
actually is (exercises, labs, projects, notes or datasets) — only the types
that exist are present. Each domain has a `README.md` indexing its contents.

## Areas of Study

| Area | Highlights |
| --- | --- |
| Java | Conditionals, loops, strings, mathematical calculations, OOP: encapsulation, inheritance, aggregation/composition |
| Python | Algorithms & logic, functions, file handling (`organize_files.py`) |
| Database design | Full modeling pipeline from ER diagram to executable SQL |
| Software testing | Manual test execution, boundary analysis, JUnit 5 unit tests |
| Mobile development | Two Flutter apps with widget tests: [My First App](mobile-development/projects/getting-started-with-flutter/my_first_app/README.md) and [Anatomy App](mobile-development/projects/flutter-widgets-and-app-anatomy/anatomy_app/README.md) |
| Cloud | Google Cloud Shell labs: Apache, FTP server, HTTP traffic capture |
| Data science | EDA and preprocessing notebooks over shared, deduplicated datasets |
| Artificial intelligence | Practice exercises: loading, inspecting and using Keras `.h5` models |

## Learning Progression

1. **Fundamental Programming** — algorithms and logic in Java and Python
2. **Object-Oriented Programming** — encapsulation, inheritance, composition
3. **Database Design** — conceptual → logical → physical modeling
4. **Software Quality** — manual and automated testing
5. **Cloud Infrastructure** — cloud shell, web servers, network traffic
6. **Mobile Development** — Flutter apps and widget testing
7. **Data Science** — exploration, visualization and preprocessing

## Getting Started

- **Java**: JDK 8+; JUnit 5 for the test suites
- **Python**: 3.10+
- **Jupyter**: `pip install jupyter pandas numpy matplotlib seaborn`
- **Flutter**: SDK installed; `flutter pub get`, then `flutter test` per app

See each folder's `README.md` for specific instructions.

## License

This repository is licensed under the [MIT License](LICENSE).

## Contact

For questions, suggestions, or feedback, please open an issue on the
repository or contact directly via GitHub.

---

**Note** — This repository represents a learning journey and contains
exercises from various courses and self-study projects. Some exercises are
simplified versions of real-world scenarios for educational purposes.