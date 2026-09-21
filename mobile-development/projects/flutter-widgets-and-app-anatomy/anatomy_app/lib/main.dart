// ---------------------------------------------------------------------
// Main file of the app. This is the "root" of the Flutter application:
// the widget that Flutter receives to start painting everything.
//
// The import below loads "Material Design": the collection of ready-made
// visual components of Flutter (Scaffold, AppBar, Card, buttons, etc.).
// ---------------------------------------------------------------------
import 'package:flutter/material.dart';

// Imports the widgets we created separately in the lib/widgets/ folder.
import 'widgets/click_counter.dart';
import 'widgets/stopwatch.dart';
import 'widgets/student_card.dart';

// ---------------------------------------------------------------------
// `void main()`:
// The starting function (entry point) of the program.
// In Dart every program starts running from here; Flutter looks for this
// function first: without `main`, the app does not execute.
// The `void` states that this function does not return any value to its
// caller.
// ---------------------------------------------------------------------
void main() {
  // ---------------------------------------------------------------------
  // `runApp(const MyApp())`:
  // Hands the root widget over to Flutter and brings the app up.
  // runApp takes the widget we pass (MyApp) and makes it the first node
  // of the widget tree, triggering the first `build`.
  // The `const` means this MyApp is constant (immutable): it never
  // changes after being created, so Flutter can reuse it and save memory.
  // ---------------------------------------------------------------------
  runApp(const MyApp());
}

// ---------------------------------------------------------------------
// `class MyApp extends StatelessWidget`:
// MyApp is the root widget of the app and it is "Stateless": it holds no
// information that changes over time. Its only job is to "configure" the
// app (title, theme and home screen). Because that configuration never
// changes, it does not need a State class.
// ---------------------------------------------------------------------
class MyApp extends StatelessWidget {
  // Constructor. The `super.key` is the key Flutter uses to identify the
  // widget in the tree; always forwarding it is a good practice.
  const MyApp({super.key});

  // ---------------------------------------------------------------------
  // `Widget build(BuildContext context)`:
  // Every widget defines a `build` that returns what should be drawn.
  // The `context` is the widget's "address" inside the tree: through it
  // we can read the theme, navigation and other environment data.
  // ---------------------------------------------------------------------
  @override
  Widget build(BuildContext context) {
    // ---------------------------------------------------------------------
    // `return MaterialApp(...)`:
    // Returns the MaterialApp, the widget that gives the app its Material
    // Design look; it is the one that organizes the theme, navigation
    // between screens and the home screen.
    // ---------------------------------------------------------------------
    return MaterialApp(
      title: 'Flutter Anatomy',
      theme: ThemeData(
        // Main color of the app. From this seed Flutter derives all the
        // other theme colors (buttons, AppBar, texts...).
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      // ---------------------------------------------------------------------
      // `home: const MyHomePage(...)`:
      // Sets which widget appears when the app opens. The `home` says:
      // "as soon as it starts, show MyHomePage". It is also `const`,
      // because the home screen configuration never changes.
      // ---------------------------------------------------------------------
      home: const MyHomePage(title: 'Flutter Anatomy'),
    );
  }
}

// ---------------------------------------------------------------------
// `class MyHomePage extends StatefulWidget`:
// MyHomePage is a widget WITH state. Notice it has TWO classes:
//
//  1. The widget class (this one) only keeps the CONFIGURATION - the data
//     the parent passes, like `title`. This data never changes.
//  2. The State class (right below) keeps the STATE - the data that
//     changes while the app is being used, like `_counter`.
//
// Separating the two lets Flutter rebuild the widget without losing the
// current state.
// ---------------------------------------------------------------------
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // ---------------------------------------------------------------------
  // `final String title`:
  // An immutable widget field. It arrives through the constructor, passed
  // by the parent (in `home: ...`), and never changes again - which is
  // why it is `final`. In Dart, every field of a Widget class must be
  // `final`.
  // ---------------------------------------------------------------------
  final String title;

  // ---------------------------------------------------------------------
  // `State<MyHomePage> createState()`:
  // The method Flutter calls to create the screen's State class.
  // Notice the return type is `State<MyHomePage>`, and the implementation
  // returns `_MyHomePageState` (which is a State<MyHomePage>).
  // ---------------------------------------------------------------------
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

// ---------------------------------------------------------------------
// `class _MyHomePageState extends State<MyHomePage>`:
// The second class of the StatefulWidget. The leading `_` makes it
// private (it only exists within this file). It is the one that holds the
// mutable state (`_counter`) and the `build` method. When the state
// changes, Flutter calls `build` again to redraw the screen with the new
// values.
// ---------------------------------------------------------------------
class _MyHomePageState extends State<MyHomePage> {
  // ---------------------------------------------------------------------
  // `int _counter = 0`:
  // The counter of the Flutter default example. It is a STATE field and,
  // therefore, lives in the State class: it changes while the app runs.
  // The leading `_` says the variable is private (only visible inside
  // this file).
  // ---------------------------------------------------------------------
  int _counter = 0;

  void _incrementCounter() {
    // ---------------------------------------------------------------------
    // `setState(() { _counter++; })`:
    // Tells Flutter the state changed. It marks the widget as "needs to
    // be rebuilt" and calls `build` again, showing the new value on the
    // screen. Without `setState`, `_counter` would change in memory, but
    // the interface would keep showing the old value.
    // ---------------------------------------------------------------------
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // ---------------------------------------------------------------------
    // The Scaffold is the "structure" of a Material Design screen: it
    // organizes the AppBar, the body and the floating button. Think of
    // it as the skeleton of a page.
    // ---------------------------------------------------------------------
    return Scaffold(
      // ---------------------------------------------------------------------
      // `appBar: AppBar(title: Text(widget.title))`:
      // The AppBar is the top bar of the screen. Its `title` receives a
      // Text. Notice `widget.title`: inside the State class, the word
      // `widget` is the reference to the Widget class that originated
      // this State - that is how we read the `title` the parent passed
      // further above.
      // ---------------------------------------------------------------------
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      // The screen body. Because the content is taller than the screen,
      // the SingleChildScrollView lets the user scroll the column down.
      body: SingleChildScrollView(
        child: Column(
          children: [
            // ---------------------------------------------------------------
            // Default Flutter example, kept functional: shows how many
            // times the floating button (FloatingActionButton) was tapped.
            // ---------------------------------------------------------------
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  const Text(
                    'You have pushed the floating button this many times:',
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '$_counter',
                    style: Theme.of(context).textTheme.headlineMedium,
                  ),
                ],
              ),
            ),
            const Divider(),
            const _SectionTitle('1. ClickCounter'),
            const ClickCounter(),
            const SizedBox(height: 8),
            const Divider(),
            const _SectionTitle('2. Stopwatch'),
            const Stopwatch(seconds: 0),
            const Stopwatch(seconds: 42),
            const Stopwatch(seconds: 125),
            const SizedBox(height: 8),
            const Divider(),
            const _SectionTitle('3. StudentCard'),
            // Term not informed: uses the default 5.
            const StudentCard(
              name: 'Adriely Martins',
              course: 'Information Systems',
            ),
            const StudentCard(
              name: 'Natasha Andrade',
              course: 'Software Engineering',
              term: 3,
            ),
            const StudentCard(
              name: 'Ana Beatriz',
              course: 'Computer Science',
              term: 7,
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
      // ---------------------------------------------------------------------
      // The FloatingActionButton is the typical circular floating button
      // of Material Design, positioned at the corner of the screen.
      // ---------------------------------------------------------------------
      floatingActionButton: FloatingActionButton(
        // ---------------------------------------------------------------------
        // `onPressed: _incrementCounter`:
        // Receives the FUNCTION to run when the button is pressed. Notice
        // we pass only the function name (_incrementCounter) without
        // calling it: if we wrote `_incrementCounter()` (with
        // parentheses), the function would run at build time - and the
        // `void` it returns is not a valid "action on press".
        // ---------------------------------------------------------------------
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}

// ---------------------------------------------------------------------
// Auxiliary (private) widget used in the screen body: it just shows a
// section title, keeping the interface organized.
// ---------------------------------------------------------------------
class _SectionTitle extends StatelessWidget {
  const _SectionTitle(this.text);

  final String text;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
      child: Text(
        text,
        textAlign: TextAlign.left,
        style: Theme.of(context)
            .textTheme
            .titleMedium
            ?.copyWith(fontWeight: FontWeight.bold),
      ),
    );
  }
}