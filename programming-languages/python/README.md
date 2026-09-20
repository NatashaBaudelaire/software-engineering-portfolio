# Python Programming Exercises

Self-contained Python exercises covering fundamental programming concepts,
algorithms and practical file-handling scripts. Completed as part of
undergraduate software engineering coursework.

## Directory Structure

### `algorithms-and-problem-solving`

Basic programming concepts and algorithmic exercises.

| Category | Exercises |
| --- | --- |
| `conditionals` | arithmetic_calculator, athlete_age_classification, beer_song, binary_search_book_manager, character_classifier, extract_unique_vowels, football_team_points, highest_lowest_ping, kpop_band_genres, maze_solver, minute_parity_checker, opponent_battle, ranking_tracker_quidditch, score_average_and_pass_fail, string_list_to_integer_converter, student_assessment_records, strongest_and_weakest_student |
| `functions` | ic_class_schedule_lookup, mathematical_verification, simple_calculator |
| `loops` | among_us_voting_simulator, graph_pathfinder, medicine_battle_simulator, odd_numbers, skrull_invasion_simulator, spider_vs_rhino_battle_simulator, square_calculator, sum_positives_and_count_negatives |
| `mathematical-calculations` | arithmetic_functions, arithmetic_operations, avatar_frequency_counter, average_of_two_numbers, basic_arithmetic_functions, circle_area_and_circumference, creature_element_index, degrees_to_radians, fibonacci_membership_checker, fuel_price_ratio, hourly_wage_calculator, largest_and_smallest, matrix_add_multiply_sequence, point_vector_operations, prime_factorisation_and_line_selection, profit_calculator, random_number_generator, rectangle_area_and_perimeter, sphere_volume, sum_of_two_numbers, temperature_converter, uniform_random_generator |
| `strings` | cake_recipe, chance_calculator, primitive_type_checker, race_results, string_indexing_demo, string_list_slicing_demo, word_presence_checker |
| `variables-and-input` | accessing_characters, age_converter, area_calculator, ascii_pair_message_decryptor, celsius_to_fahrenheit, client_data, echo_user_message, global_message_demo, global_variable_demo, local_variable_demo, name_and_city, name_and_surname, name_input_with_defaults, ranking_tracker_alt_events, returned_message_demo, shop_payment_calculator, student_grade_status, swap_two_values, text_replacer, ticket_revenue_calculator, topic_voting_results, treasure_hunt_simulator |

### `file-handling`

Practical file automation scripts:

- **organize_files**: automatic file organization script (see its own
  [README](file-handling/README.md)).

## How to Run

### Prerequisites

- Python 3.10 or higher (some exercises use match/case statements)

### Basic Execution

```bash
cd algorithms-and-problem-solving/conditionals
python arithmetic_calculator.py
```

### Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
python arithmetic_calculator.py
```

### Using an IDE

Open the `python` directory in your IDE (VS Code, PyCharm, etc.), navigate to
an exercise, and run the `.py` file.

## Notes

- Each exercise is self-contained and runs independently.
- Type hints and f-strings are used throughout.
- Some exercises expect console input with a specific format.

## Learning Objectives

- Basic syntax, control flow and match/case pattern matching
- Functions: definition, parameters, return values
- Data structures: lists, dictionaries, sets, tuples
- String manipulation and text processing
- File reading/writing and OS automation
- Algorithm design and game logic