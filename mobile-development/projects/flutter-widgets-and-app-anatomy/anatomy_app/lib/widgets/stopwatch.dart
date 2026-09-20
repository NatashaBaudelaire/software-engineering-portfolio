import 'package:flutter/material.dart';

// ---------------------------------------------------------------------
// Stopwatch: a stateless widget.
// It receives a number of seconds and simply renders the elapsed time
// formatted as MM:SS. Since nothing changes here, no State is needed.
// ---------------------------------------------------------------------
class Stopwatch extends StatelessWidget {
  const Stopwatch({super.key, required this.seconds});

  // Number of seconds received from the parent widget.
  final int seconds;

  @override
  Widget build(BuildContext context) {
    // Integer division with `~/`: 125 ~/ 60 = 2 (whole minutes).
    final minutes = seconds ~/ 60;

    // Remainder of the division: 125 % 60 = 5 (leftover seconds).
    final remainingSeconds = seconds % 60;

    // padLeft(2, '0') guarantees two digits: 2 becomes "02" and 5 "05".
    final formattedTime =
        '${minutes.toString().padLeft(2, '0')}:'
        '${remainingSeconds.toString().padLeft(2, '0')}';

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: ListTile(
        leading: const Icon(Icons.timer_outlined),
        title: Text(
          formattedTime,
          style: Theme.of(context)
              .textTheme
              .headlineSmall
              ?.copyWith(fontWeight: FontWeight.bold),
        ),
        subtitle: Text('$seconds seconds'),
      ),
    );
  }
}