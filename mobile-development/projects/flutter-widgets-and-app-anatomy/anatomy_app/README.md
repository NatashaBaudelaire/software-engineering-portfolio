# anatomy_app

Flutter project created for the "Anatomy of a Flutter project" mobile
development exercise.

```bash
flutter create --org br.edu.unit --platforms=android anatomy_app
```

## What it demonstrates

Three custom widgets, each in its own file under `lib/widgets/`:

| Widget       | File                              | Type            |
| ------------ | --------------------------------- | --------------- |
| `ClickCounter` | `lib/widgets/click_counter.dart`  | StatefulWidget  |
| `Stopwatch`  | `lib/widgets/stopwatch.dart`      | StatelessWidget |
| `StudentCard` | `lib/widgets/student_card.dart`  | StatelessWidget |

The home screen (`lib/main.dart`) is heavily commented in English and explains
the anatomy of a Flutter project: `void main()`, `runApp`, `StatelessWidget` vs
`StatefulWidget`, `build`, `setState`, `widget.title`, and the Scaffold/AppBar/
body/floatingActionButton structure.

## Running

```bash
flutter pub get
flutter run
```

## Tests

```bash
flutter test
```

Validated with `flutter analyze` and `dart format .`.