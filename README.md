# Software Engineering Coursework

A personal collection of self-contained coursework and exercises spanning programming fundamentals, database design, cloud computing, software testing, and data science. The repository documents a progressive learning path across multiple technologies, from basic algorithms and object-oriented programming in Java and Python, through relational database modeling and cloud services, to automated testing and exploratory data science.

## Repository Structure

```
software-engineering-coursework/
├── 01-programming-languages/
│   ├── java/
│   │   ├── algorithms-and-problem-solving/   # conditionals, loops, maths, strings, variables & input
│   │   └── object-oriented-programming/      # encapsulation, inheritance, aggregation & composition
│   └── python/
│       ├── algorithms-and-problem-solving/   # conditionals, functions, loops, maths, strings, variables & input
│       └── file-handling/                    # file organization automation
├── 02-databases/
│   ├── conceptual-model/                     # entity-relationship diagrams (PNG)
│   ├── logical-model/                        # logical schemas (PNG)
│   └── physical-model/                       # SQL DDL scripts
├── 03-cloud-computing/
│   ├── apache-cloud-shell-setup/
│   ├── ftp-server-practice/
│   └── http-traffic-capture-analysis/
├── 04-software-testing/
│   ├── manual-testing/
│   ├── test-case-design/
│   │   └── vehiculardevice/
│   └── unit-testing/
│       └── calculator/
├── 05-artificial-intelligence/               # module notes only (no implementation artifacts yet)
└── 06-data-science/
    ├── data-analysis-and-visualization/
    ├── data-preprocessing/
    └── exploratory-data-analysis/
```

## Technologies

- **Java** (JDK 8+) — exercise programs, with JUnit 5 for automated tests
- **Python** (3.10+) — scripts, including structural pattern matching (`match`/`case`)
- **SQL** — DDL schemas for the physical database model
- **Markdown** — module documentation and cloud computing guides
- **Jupyter Notebooks** — data science analysis (pandas, NumPy, Matplotlib, Seaborn)

## Coursework Modules

### 01 · Programming Languages

**Java** (`01-programming-languages/java/`) — 34 exercises in `algorithms-and-problem-solving/` across conditionals (10), loops (8), mathematical calculations (8), strings (3), and variables & input (5). The `object-oriented-programming/` area covers encapsulation (bank accounts, devices, digital thermometers, printers, vehicles), inheritance (ship hierarchy), and aggregation/composition (resource management). See `01-programming-languages/java/README.md`.

**Python** (`01-programming-languages/python/`) — 80 scripts: 79 exercises plus a file-handling automation script (`organize_files.py`). Covers conditionals (17), functions (3), loops (8), mathematical calculations (22), strings (7), variables & input (22), and file handling. See `01-programming-languages/python/README.md`.

### 02 · Databases

Database modeling at three levels of abstraction: conceptual models (4 entity-relationship diagrams), logical models (7 schemas), and physical models (9 SQL DDL scripts). See `02-databases/README.md`.

### 03 · Cloud Computing

Hands-on cloud and network exercises documented as text guides: Apache web server setup on Google Cloud Shell, FTP server practice, and HTTP traffic capture with tcpdump analysis. See `03-cloud-computing/README.md`.

### 04 · Software Testing

Testing practice across manual testing (candidate status evaluation logic), test-case design (a `VehicularDevice` domain model with a 16-case JUnit suite covering movement, door, and alarm scenarios), and unit testing (a simple calculator with JUnit tests). See `04-software-testing/README.md`.

### 05 · Artificial Intelligence

Module documentation and learning roadmap only; no implementation code is committed at this time. See `05-artificial-intelligence/README.md`.

### 06 · Data Science

Jupyter notebooks for data analysis and visualization (diabetes), data preprocessing (house prices, Pima Indian diabetes), and exploratory data analysis (traffic accident severity). Each notebook references a local CSV dataset that is excluded from version control. See `06-data-science/README.md`.

## Getting Started

Prerequisites:

- **Java**: JDK 8+ for the Java exercises, JUnit 5 for the test suites
- **Python**: 3.10+ (some scripts use `match`/`case`)
- **Jupyter**: for the notebooks — `pip install jupyter pandas numpy matplotlib seaborn`

## Usage

**Java exercise**

```bash
cd 01-programming-languages/java/algorithms-and-problem-solving/conditionals/weightedbillsplit
javac WeightedBillSplit.java
java weightedbillsplit.WeightedBillSplit
```

**Python exercise**

```bash
cd 01-programming-languages/python/algorithms-and-problem-solving/conditionals
python arithmetic_calculator.py
```

**JUnit 5 tests**

```bash
cd 04-software-testing/test-case-design/vehiculardevice
javac VehicularDevice.java VehicularDeviceTest.java VehicularDeviceTestSuite.java
java -jar junit-platform-console-standalone.jar --class-path . --select-class vehiculardevice.VehicularDeviceTestSuite
```

**Jupyter notebooks**

```bash
cd 06-data-science/exploratory-data-analysis
jupyter notebook
```

## Documentation

Each module ships its own `README.md` describing the exercises and how to run them:

- `01-programming-languages/java/README.md`
- `01-programming-languages/python/README.md`
- `02-databases/README.md`
- `03-cloud-computing/README.md`
- `04-software-testing/README.md`
- `05-artificial-intelligence/README.md`
- `06-data-science/README.md`

## Contributing

This is a personal coursework repository, but suggestions and corrections are welcome via issues or pull requests. Please keep changes consistent with the repository conventions: lowercase package/class names matching their folder names, snake_case Python module names, and self-contained exercises.

## License

This repository is licensed under the [MIT License](LICENSE).