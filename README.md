<h1 align="center">
  Software Engineering Portfolio
</h1>

<p align="center">
  <strong>Personal portfolio of software engineering coursework</strong> — exercises, labs, and projects across 7 knowledge domains.
</p>

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Key Features](#key-features)
4. [Repository Structure](#repository-structure)
5. [Areas of Study](#areas-of-study)
6. [Learning Progression](#learning-progression)
7. [Installation and Execution](#installation-and-execution)
8. [Key Concepts Applied](#key-concepts-applied)
9. [Contact](#contact)


## Project Overview

Software Engineering Portfolio is a comprehensive personal portfolio documenting a progressive learning path across the core domains of software engineering. The repository contains exercises, labs, and projects completed during a Software Engineering degree, organized by **knowledge domain** and content type. Every module is self-contained with its own tests, documentation, and solution notes, making it easy to trace work back to the original curriculum.

The portfolio spans seven major domains: **Artificial Intelligence**, **Cloud Computing**, **Database Design**, **Data Science**, **Mobile Development**, **Programming Languages**, and **Software Testing** — covering everything from fundamental algorithms to production-ready mobile applications and machine learning pipelines.

## Technologies Used

- **Java** (JDK 8+) and **JUnit 5**
- **Python 3.10+** (including `match`/`case` pattern matching)
- **SQL** and relational database modeling (conceptual, logical, physical)
- **Flutter / Dart** for cross-platform mobile applications
- **Cloud tools**: Google Cloud Shell, Apache HTTP Server, FTP, HTTP traffic capture (tcpdump)
- **Data science**: Jupyter, pandas, NumPy, Matplotlib, Seaborn
- **Artificial intelligence**: TensorFlow / Keras (practice with `.h5` / HDF5 models)
- **Git** and **GitHub** for version control and collaboration

## Key Features

- **Seven Knowledge Domains**: Complete coverage of AI, Cloud, Databases, Data Science, Mobile, Programming Languages, and Testing
- **Self-Contained Modules**: Each domain includes exercises, labs, projects, and/or notes with dedicated README indexes
- **Progressive Learning Path**: Structured progression from fundamentals to advanced topics across 7 learning stages
- **Real-World Tools & APIs**: Google Cloud Shell, Flutter widget testing, Keras model serialization
- **Database Modeling Pipeline**: Full ER → logical → physical → executable SQL workflow
- **Deduplicated Datasets**: Single source of truth for all data science notebooks (diabetes, house prices, traffic accidents, water supply)
- **Flutter Mobile Apps**: Two complete apps with widget tests — "My First App" and "Widgets & App Anatomy"
- **Comprehensive Test Suites**: JUnit 5 unit tests, manual test cases, test case design documentation
- **Keras Model Practice**: Exercises for loading, inspecting, and running inference with `.h5` HDF5 models
- **Cross-Language Implementation**: Algorithms and data structures in both Java and Python

## Repository Structure

The directories at the root are the **knowledge domains** of software engineering. Each domain contains only the content types that exist for it (no empty folders).

```
├── artificial-intelligence/
│   ├── README.md                    # Domain index
│   ├── exercises/                   # Practice: working with .h5 / HDF5 ML models
│   │   ├── 01-h5-model-loading/
│   │   ├── 02-h5-model-inspection/
│   │   ├── 03-h5-model-prediction/
│   │   └── 04-h5-image-classification/
│   ├── labs/
│   ├── notes/                       # Module notes and learning roadmap
│   └── projects/
│
├── cloud-computing/
│   ├── README.md                    # Domain index
│   ├── labs/                        # Apache setup, FTP server, HTTP traffic analysis
│   │   ├── apache-cloud-shell/
│   │   ├── ftp-server/
│   │   └── http-traffic-analysis/
│   ├── exercises/
│   └── projects/
│
├── database-design/
│   ├── README.md                    # Domain index
│   ├── exercises/
│   │   ├── conceptual-model/        # ER diagrams (cleaning, order, pharmacy, physical-activity)
│   │   ├── logical-model/           # Relational schemas (cars, company, pharmacy, salesperson, seller, traffic, vehicle)
│   │   └── physical-model/          # Executable SQL (car, company, infraction, pharmacy, register, salesperson, seller, traffic, vehicle)
│   ├── labs/
│   └── projects/
│
├── data-science/
│   ├── README.md                    # Domain index
│   ├── datasets/                    # Single source of truth for all notebooks
│   │   ├── diabetes.csv
│   │   ├── house_prices.csv
│   │   ├── traffic_accident_severity_detection.csv
│   │   └── watersupply.csv
│   ├── projects/
│   │   ├── data-analysis-and-visualization/
│   │   │   └── diabetes.ipynb
│   │   ├── data-preprocessing/
│   │   │   ├── house_prices.ipynb
│   │   │   └── pima_diabetes.ipynb
│   │   └── exploratory-data-analysis/
│   │       └── traffic_accident_severity_detection.ipynb
│   └── exercises/
│
├── mobile-development/
│   ├── README.md                    # Domain index
│   ├── projects/
│   │   ├── getting-started-with-flutter/
│   │   │   └── my_first_app/        # Counter app with widget tests
│   │   └── flutter-widgets-and-app-anatomy/
│   │       └── anatomy_app/         # Widgets showcase with widget tests
│   ├── exercises/
│   └── labs/
│
├── programming-languages/
│   ├── README.md                    # Language-family index (languages ≠ frameworks)
│   ├── exercises/
│   │   ├── java/                    # Algorithms/logic + OOP
│   │   │   ├── algorithms-and-problem-solving/
│   │   │   │   ├── conditionals/
│   │   │   │   ├── loops/
│   │   │   │   ├── mathematical-calculations/
│   │   │   │   ├── strings/
│   │   │   │   └── variables-and-input/
│   │   │   └── object-oriented-programming/
│   │   │       ├── encapsulation/
│   │   │       ├── inheritance/
│   │   │       └── aggregation-and-composition/
│   │   └── python/                  # Algorithms/logic, functions, file handling
│   │       ├── algorithms-and-problem-solving/
│   │       │   ├── conditionals/
│   │   │   │   ├── functions/
│   │       │   │   ├── loops/
│   │   │   │   ├── mathematical-calculations/
│   │       │   │   ├── strings/
│   │       │   │   └── variables-and-input/
│   │       └── file-handling/
│   ├── labs/
│   └── projects/
│
└── software-testing/
    ├── README.md                    # Domain index
    ├── exercises/
    │   ├── manual-testing/          # CandidateStatus evaluation
    │   ├── test-case-design/        # VehicularDevice scenarios, Comments documentation
    │   └── unit-testing/            # Calculator JUnit 5 test suite
    ├── labs/
    └── projects/
```

## Areas of Study

| Area | Highlights |
| --- | --- |
| **Java** | Conditionals, loops, strings, mathematical calculations, OOP: encapsulation, inheritance, aggregation/composition |
| **Python** | Algorithms & logic, functions, file handling (`organize_files.py`), data structures |
| **Database Design** | Full modeling pipeline: ER diagram → logical schema → physical model → executable SQL |
| **Software Testing** | Manual test execution, boundary analysis, test case design, JUnit 5 unit tests |
| **Mobile Development** | Two Flutter apps with widget tests: [My First App](mobile-development/projects/getting-started-with-flutter/my_first_app/README.md) and [Anatomy App](mobile-development/projects/flutter-widgets-and-app-anatomy/anatomy_app/README.md) |
| **Cloud Computing** | Google Cloud Shell labs: Apache setup, FTP server, HTTP/FTP traffic capture with tcpdump |
| **Data Science** | EDA and preprocessing notebooks over shared, deduplicated datasets (diabetes, house prices, traffic accidents, water supply) |
| **Artificial Intelligence** | Practice exercises: loading, inspecting, predicting with Keras `.h5` models (CNN, LSTM) |

## Learning Progression

1. **Fundamental Programming** — algorithms and logic in Java and Python
2. **Object-Oriented Programming** — encapsulation, inheritance, composition
3. **Database Design** — conceptual → logical → physical modeling
4. **Software Quality** — manual and automated testing
5. **Cloud Infrastructure** — cloud shell, web servers, network traffic analysis
6. **Mobile Development** — Flutter apps and widget testing
7. **Data Science** — exploration, visualization and preprocessing
8. **Artificial Intelligence** — loading, inspecting, and running inference with Keras models

## Installation and Execution

### Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| **JDK** | 8+ | Java exercises and JUnit 5 tests |
| **Python** | 3.10+ | Python exercises, data science, AI notebooks |
| **Flutter SDK** | Latest stable | Mobile development projects |
| **Jupyter** | Latest | Data science notebooks |
| **Dart** | Bundled with Flutter | Flutter app development |

### Quick Start

```bash
# Clone the repository
git clone https://github.com/NatashaBaudelaire/software-engineering-portfolio.git
cd software-engineering-portfolio

# Java: run tests
cd programming-languages/exercises/java/...
# or use your IDE (IntelliJ/Eclipse) with JUnit 5

# Python: run exercises directly
python programming-languages/exercises/python/.../exercise.py

# Data Science: start Jupyter
pip install jupyter pandas numpy matplotlib seaborn
jupyter notebook data-science/projects/

# AI: install TensorFlow/Keras
pip install tensorflow keras h5py
python artificial-intelligence/exercises/01-h5-model-loading/load_model.py

# Flutter: run mobile apps
cd mobile-development/projects/getting-started-with-flutter/my_first_app
flutter pub get
flutter test
flutter run
```

See each domain's `README.md` for domain-specific instructions.

## Key Concepts Applied

- **Multi-language proficiency**: Java (OOP, algorithms) and Python (scripting, data science, AI)
- **Full database lifecycle**: Conceptual (ER) → Logical (relational) → Physical (SQL DDL)
- **Test-driven mindset**: Manual test cases, boundary analysis, automated JUnit 5 suites
- **Cross-platform mobile**: Flutter widgets, state management, widget testing
- **Cloud operations**: Google Cloud Shell, Apache configuration, network traffic analysis
- **Data science workflow**: EDA → preprocessing → visualization → modeling
- **ML model serialization**: Keras `.h5` / HDF5 loading, inspection, inference
- **Version control**: Conventional Commits, feature branching, structured history
- **Documentation**: Per-domain README indexes, inline code comments, solution notes

## Contact

For questions, suggestions, or feedback, please open an issue on the repository or contact directly via GitHub.