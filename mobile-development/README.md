# Mobile Development

Flutter coursework projects: two complete apps built as part of the course,
each with its own README and a set of exercise answers.

## Directory Structure

### `projects/getting-started-with-flutter`

- `my_first_app/` - a counter app built while learning the Flutter basics
  (widgets, `setState`, app anatomy). Code, tests and a full README included.
- `ANSWERS.md` - answered exercise sheet for the "Getting Started with
  Flutter" lesson.

### `projects/flutter-widgets-and-app-anatomy`

- `anatomy_app/` - an app that explores widget composition and app anatomy
  (student card, click counter and stopwatch widgets). Code, tests and README
  included.
- `screenshots/` - app screenshots of the exercises.
- `ANSWERS.md` - answered exercise sheet for the "Flutter Widgets and App
  Anatomy" lesson.

## How to Run

Each app is a standard Flutter project. With the Flutter SDK installed:

```bash
cd projects/getting-started-with-flutter/my_first_app
flutter pub get
flutter run
```

Run the widget tests with:

```bash
flutter test
```