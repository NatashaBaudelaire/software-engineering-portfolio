import 'package:flutter/material.dart';

// ---------------------------------------------------------------------
// StudentCard: a stateless widget.
// It only receives the student data and renders a card: since this data
// does not change while the app is running, no State class is needed.
// ---------------------------------------------------------------------
class StudentCard extends StatelessWidget {
  // `const` constructor: the card can be created as a constant.
  // The required fields use `required`, and the term is optional
  // (defaults to 5).
  const StudentCard({
    super.key,
    required this.name,
    required this.course,
    this.term = 5,
  });

  // `final` fields: they are set only once and never change.
  final String name;
  final String course;
  final int term;

  @override
  Widget build(BuildContext context) {
    // We use the app theme instead of hard-coding colors, so the card
    // follows the look of the rest of the application.
    final colorScheme = Theme.of(context).colorScheme;
    final textTheme = Theme.of(context).textTheme;

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            // Circular avatar with the first letter of the name.
            CircleAvatar(
              radius: 28,
              backgroundColor: colorScheme.primaryContainer,
              child: Text(
                name.isEmpty ? '?' : name[0].toUpperCase(),
                style: textTheme.titleLarge?.copyWith(
                  color: colorScheme.onPrimaryContainer,
                ),
              ),
            ),
            const SizedBox(width: 16),
            // Expanded makes the text fill the remaining Row space,
            // preventing a long name/course from overflowing the screen.
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Name highlighted (bold and larger).
                  Text(
                    name,
                    style: textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  // Format: course - term X.
                  Text(
                    '$course - term $term',
                    style: textTheme.bodyMedium?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}