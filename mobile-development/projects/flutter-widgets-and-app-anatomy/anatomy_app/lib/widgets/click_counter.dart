import 'package:flutter/material.dart';

// ---------------------------------------------------------------------
// ClickCounter: a stateful widget.
// The number of clicks changes on every button tap, so the value lives
// in a State and the screen is redrawn with setState().
// ---------------------------------------------------------------------
class ClickCounter extends StatefulWidget {
  const ClickCounter({super.key});

  @override
  State<ClickCounter> createState() => _ClickCounterState();
}

class _ClickCounterState extends State<ClickCounter> {
  // Widget state: the current number of clicks.
  int _counter = 0;

  void _increment() {
    setState(() {
      _counter++;
    });
  }

  void _decrement() {
    // Never lets the number go negative: only decreases if it is > 0.
    if (_counter > 0) {
      setState(() {
        _counter--;
      });
    }
  }

  void _reset() {
    setState(() {
      _counter = 0;
    });
  }

  // Color of the number depending on how many clicks there are.
  Color _numberColor() {
    if (_counter == 0) {
      return Colors.grey;
    } else if (_counter >= 1 && _counter <= 9) {
      return Colors.blue;
    } else {
      return Colors.green;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        // Large, centered number.
        Text(
          '$_counter',
          style: Theme.of(context)
              .textTheme
              .displayLarge
              ?.copyWith(color: _numberColor(), fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 16),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // - button (decreases).
            IconButton.filled(
              onPressed: _decrement,
              icon: const Icon(Icons.remove),
            ),
            const SizedBox(width: 24),
            // + button (increases).
            IconButton.filled(
              onPressed: _increment,
              icon: const Icon(Icons.add),
            ),
          ],
        ),
        const SizedBox(height: 8),
        // Text button to go back to zero.
        TextButton(onPressed: _reset, child: const Text('Reset')),
      ],
    );
  }
}