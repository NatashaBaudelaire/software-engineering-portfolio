# Answers - Lesson 03: Anatomy of a Flutter Project

Exercise developed in the `anatomy_app` project, created with:

```bash
flutter create --org br.edu.unit --platforms=android anatomy_app
```

---

## Part A - Commented anatomy

The explanations of each element (`void main()`, `runApp(...)`, the
`MyApp`/`MyHomePage` classes, `build`, `setState`, etc.) are written as
comments inside the `lib/main.dart` file itself. Below are the answers to the
4 questions.

### 1. Why does `StatefulWidget` need two classes?

Because it holds two "kinds" of information that must live apart:

- the **Widget** class keeps the immutable **configuration** (what the parent
  passes, like `title`);
- the **State** class keeps the **state** that changes during execution
  (like `_counter`).

Separating these lets Flutter **rebuild the widget** (for example, when the
parent changes a configuration) **without losing the current state**. If
everything lived in a single class, the counter value, a scroll position, etc.
would be thrown away on every rebuild.

### 2. Why is `_counter` in the `State` class and `title` in the `Widget` class?

Because one is state and the other is configuration:

- `_counter` **changes over time** (every time the user taps the button), so it
  is **state** data -> it must live in the **State**.
- `title` is **received ready-made from the parent** and **never changes** once
  defined -> it is **configuration** -> it must live in the **Widget** class,
  which is why it is `final`.

Rule of thumb from the lesson: *data that changes -> State; received and fixed
data -> Widget (final).*

### 3. What does the `_` at the start of `_MyHomePageState` and `_counter` mean in Dart?

The `_` makes the element **private**. In Dart, any identifier (class, variable,
method) that starts with `_` can only be used **inside the same file** (in this
case, `lib/main.dart`). It is Dart's own convention to indicate privacy, without
needing keywords such as `private`.

### 4. How many times can `build()` be called? What should never go inside it, and why?

`build()` can be called **many times** during the widget's life: on every
`setState`, on every theme/screen-size change, when entering a new route, on hot
reload, etc.

That is why `build()` must be a **"pure"** method: it should only "describe" the
interface. It should **never** contain heavy work or side effects, such as:

- network calls, database queries or file reads;
- long, slow computations;
- creation of objects with random values (which would change on every build);
- excessive `print` (debugging only).

The reason: since `build` runs every time something changes, heavy work there
would make the app slow and janky - on every tap Flutter would run it all again.
The ideal is for the interface to be **derived** from the current state, quickly
and predictably.

---

## Part B - Error catalog

For each error below, the following are recorded: **full message, where it
appeared, meaning in my own words, and how it was fixed**.

### B1 - `onPressed: _incrementCounter()`

- **Full message:**
  ```text
  The argument type 'void' can't be assigned to the parameter type 'void Function()?'.
  ```
- **Where it appeared:** in the `onPressed` property of the
  `FloatingActionButton` (and it would apply to any `onPressed`/`onTap`) in
  `lib/main.dart`.
- **Meaning:** `onPressed` expects a **function** (`void Function()?`), that is,
  a "command" to be executed **when the button is pressed**. By writing
  `_incrementCounter()` **with parentheses**, the function is **executed
  immediately**, at widget build time, and the value it returns is `void`
  (nothing). So Flutter receives `void` where a function was expected, the
  types do not match, and the analyzer reports the error.
- **How it was fixed:** removing the parentheses and passing only the
  **reference** to the function:
  ```dart
  onPressed: _incrementCounter
  ```

### B2 - Removing `setState`, leaving only `_counter++;`

- **Full message:** none, the code **compiles without errors**.
- **Where it appeared:** in the body of the `_incrementCounter` method.
- **Meaning:** the `_counter` value changes in memory (`0` becomes `1`,
  `2`...), but Flutter **is not notified** that something changed. The framework
  only redraws the widgets that were "marked" by `setState`. Without it, the
  interface keeps showing the old value and the app **appears** to not work,
  even though the variable is internally up to date.
- **How it was fixed:** restoring the `setState`:
  ```dart
  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }
  ```

### B3 - `Text(_counter)`

- **Full message:**
  ```text
  The argument type 'int' can't be assigned to the parameter type 'String?'.
  ```
  (in newer versions the message may vary slightly, but it always mentions the
  `int` -> `String` conflict)
- **Where it appeared:** when creating a `Text`, in the screen body.
- **Meaning:** the `Text` widget expects a **String** (the text to display).
  `_counter` is an **int** (integer number). The number must be **converted** to
  text before being shown.
- **How it was fixed:** converting with string interpolation (or `toString()`):
  ```dart
  Text('$_counter')
  // or:
  Text(_counter.toString())
  ```

### B4 - Putting `children: [...]` directly inside a `Center`

- **Full message:**
  ```text
  The named parameter 'children' isn't defined.
  ```
  (apart from the invocation: `Center` has no `children`)
- **Where it appeared:** in the `body`, trying to put several widgets inside a
  `Center`.
- **Meaning:** `Center` is a **single-child** widget and only accepts `child:`.
  The widgets that group **multiple** children are `Column`/`Row` (they accept
  `children:` as a list). `Center` does not "know" how to group several widgets.
- **How it was fixed:** placing a `Column` inside the `Center`:
  ```dart
  Center(
    child: Column(
      children: [ ... ],
    ),
  )
  ```

### B5 - `Row` containing a very large `Text`, without `Expanded`

- **Full message** (at runtime, shown in the debug console):
  ```text
  RenderFlex overflowed by X pixels on the right.
  ```
  (the text appears with yellow/black stripes on the screen in debug mode)
- **Where it appeared:** inside the `Row` of a `StudentCard` (applies to any
  `Row` with content wider than the available width).
- **Meaning:** the `Row` lays out its children side by side using the **natural**
  size of each one. When the text is wider than the space available on the
  screen, it **does not fit** and "overflows": Flutter starts drawing the text
  outside and reports the error.
- **How it was fixed:** wrapping the text with `Expanded`, which makes the child
  occupy **only the remaining space** in the `Row`, so the text fits (wrapping
  lines if needed):
  ```dart
  Row(
    children: [
      Expanded(
        child: Text(name),
      ),
    ],
  )
  ```

### B6 - Replacing the `Scaffold` with a `Center` in `home:`

- **Full message:** no compilation error; the error is structural/missing
  components.
- **Where it appeared:** in the `home:` of the `MaterialApp`.
- **Meaning:** the `Scaffold` is what **organizes the whole screen**: it provides
  the `AppBar`, the `body`, the floating button, the background color and the
  safe-area handling (SafeArea). A bare `Center` only **centers a child**; it has
  no `AppBar` and no proper place for a screen body structure. Replacing the
  `Scaffold` removes the AppBar and all the page infrastructure.
- **How it was fixed:** keeping the `Scaffold` as the "page" (the first widget
  drawn inside the `MaterialApp`), with the `Center`/content inside its `body`:
  ```dart
  MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: ...),
      body: Center(child: ...),
    ),
  )
  ```

---

## Part C - Widgets

The `StudentCard`, `Stopwatch` and `ClickCounter` widgets were created in
separate files under `lib/widgets/`:

| Widget       | File                              | Type            |
| ------------ | --------------------------------- | --------------- |
| `StudentCard`  | `lib/widgets/student_card.dart`   | StatelessWidget |
| `Stopwatch`  | `lib/widgets/stopwatch.dart`      | StatelessWidget |
| `ClickCounter` | `lib/widgets/click_counter.dart`  | StatefulWidget  |

### Why does `ClickCounter` need to be a `StatefulWidget`?

Because it needs to **store and modify information over time**: the number of
clicks changes on every tap of `+`, `-` and `Reset`. That information is
**state** and, when it changes, the interface must be redrawn (`setState`).

The lesson criterion: widgets that **change while the app is being used** need a
`StatefulWidget` (state + `setState`); widgets that **only receive data and
display it without changing** are `StatelessWidget` - which is exactly the case
of `StudentCard` and `Stopwatch`.

---

## Part D - Widget Tree

Widget tree of this exercise's app (the same structure as the statement:
`Scaffold` -> `appBar`/`body`/`floatingActionButton`):

```text
Scaffold
├── appBar: AppBar
│   └── title: Text(widget.title)
├── body: SingleChildScrollView
│   └── child: Column
│       ├── children: [
│       │   ├── Padding (default counter section)
│       │   │   └── child: Column
│       │   │       ├── children: [
│       │   │       │   ├── Text (counter phrase)
│       │   │       │   ├── SizedBox (spacing)
│       │   │       │   └── Text ('$_counter')
│       │   ├── Divider
│       │   ├── _SectionTitle('1. ClickCounter')
│       │   │   └── child: Padding
│       │   │       └── child: Text
│       │   ├── ClickCounter
│       │   │   ├── Text (number of clicks)
│       │   │   ├── Row
│       │   │   │   ├── children: [
│       │   │   │   │   ├── IconButton - (Icons.remove)
│       │   │   │   │   ├── SizedBox (spacing)
│       │   │   │   │   └── IconButton + (Icons.add)
│       │   │   │   └── ]
│       │   │   └── TextButton ('Reset')
│       │   │       └── child: Text
│       │   ├── Divider
│       │   ├── _SectionTitle('2. Stopwatch')
│       │   ├── Stopwatch (seconds: 0)
│       │   │   └── Card
│       │   │       └── child: ListTile
│       │   │           ├── leading: Icon (Icons.timer_outlined)
│       │   │           ├── title: Text ('00:00')
│       │   │           └── subtitle: Text (seconds)
│       │   ├── Stopwatch (seconds: 42)
│       │   ├── Stopwatch (seconds: 125)
│       │   ├── Divider
│       │   ├── _SectionTitle('3. StudentCard')
│       │   ├── StudentCard
│       │   │   └── Card
│       │   │       └── child: Padding
│       │   │           └── child: Row
│       │   │               ├── children: [
│       │   │               │   ├── CircleAvatar
│       │   │               │   │   └── child: Text (first letter)
│       │   │               │   ├── SizedBox (spacing)
│       │   │               │   └── Expanded
│       │   │               │       └── child: Column
│       │   │               │           ├── children: [
│       │   │               │           │   ├── Text (name)
│       │   │               │           │   └── Text (course, term N)
│       │   │               │           │   ]
│       │   │               │           └── ]
│       │   │               └── ]
│       │   ├── StudentCard
│       │   ├── StudentCard
│       │   └── SizedBox (final spacing)
│       │   ]
│       └── ]
└── floatingActionButton: FloatingActionButton
    └── child: Icon (Icons.add)
```

### 1. Which widgets receive `child:` and which receive `children:`?

They receive **`child:`** (a single child):

- `SingleChildScrollView` -> `child: Column`
- `Expanded` -> `child: Column`
- `Card` -> `child: Padding`
- `Padding` -> `child: Row` / `Text`
- `CircleAvatar` -> `child: Text`
- `FloatingActionButton` -> `child: Icon`
- `AppBar` -> `title: Text` (and the `Scaffold` uses `appBar:`, `body:`,
  `floatingActionButton:` - all are "slots" for a single widget)

They receive **`children:`** (a list of children):

- `Column` -> `children: [...]`
- `Row` -> `children: [...]`

Summary: group layout widgets (`Row`, `Column`) group several children;
"wrapping" widgets (`Card`, `Padding`, `Center`, `Expanded`) receive a single
child.

### 2. What is the role of `Expanded` inside the `Row`?

`Expanded` makes the child occupy **all the remaining space** of the `Row` (the
flexible space) instead of using the content's natural size. When there is more
than one `Expanded`, the total space is **distributed between them**. In
`StudentCard`, it is what guarantees the name/course text uses the available
width without invading the avatar.

### 3. What happens without `Expanded` when the text is very large?

The `Row` tries to draw the text at its natural size. If it is larger than the
available width, the text **does not fit**: Flutter raises the error
`RenderFlex overflowed by X pixels on the right` and, in debug mode, the area
shows yellow/black stripes. Visually, the content becomes cut off/overflowing.

### 4. Why use `SingleChildScrollView` wrapping the `Column`?

Because the `Column` contains a lot of content (the counter example, the 3
widgets and the 3 cards) and, on small screens, that content **does not fit in
the height**. The `SingleChildScrollView` allows **scrolling** the screen down
to see everything.

### 5. Which error does it help avoid?

The **vertical overflow** error:

```text
RenderFlex overflowed by X pixels on the bottom.
```

Without the scroll, the `Column` would be taller than the screen and the content
at the end would be cut off/overflowed. With `SingleChildScrollView`, the height
is no longer "limited" by the screen and becomes scrollable.

### 6. `Divider` is a widget. Which other elements of this tree could be considered properties in CSS/XML instead of widgets?

In CSS/XML, several things in this tree would be mere **style/layout
properties**, not elements. For example:

- **Spacing:** the `SizedBox` (space between items) and the `padding`/`margin`
  of the `EdgeInsets`;
- **Alignment:** the `Center` and the `mainAxisAlignment`/
  `crossAxisAlignment` of the `Row`/`Column`;
- **Space between list items:** the HTML equivalent of `Divider` is the `<hr>`
  tag, but in CSS it would be a `border-bottom`;
- **Colors and backgrounds:** `backgroundColor`, text `color`, the avatar
  `radius`;
- **Spacing/flexibility:** `Expanded` would be something like `flex: 1`;
- **Width/height:** the dimensional `SizedBox` and the `EdgeInsets`.

In other words: Flutter "elevates" many style properties to first-class widgets,
while CSS/XML usually treats them as attributes.

---

## Quality

The project was validated with:

```bash
flutter analyze
dart format .
```

No analyzer errors and formatted code.