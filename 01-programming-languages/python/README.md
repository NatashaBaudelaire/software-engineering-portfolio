# Python Programming Exercises

This directory contains Python programming exercises covering fundamental programming concepts, algorithms, and practical applications. These exercises were completed as part of my learning journey in Python development.

## Directory Structure

### 📁 algorithms-and-logic
Basic programming concepts and algorithmic exercises.

#### conditionals
Exercises focusing on conditional statements and decision-making logic:
- **arithmetic_calculator**: Arithmetic operations with a match/case menu
- **athlete_age_classification**: Athlete age categorization
- **beer_song**: 99 Bottles of Beer algorithm
- **binary_search_book_manager**: Binary search for book management
- **character_classifier**: Character classification (vowel, digit, operator)
- **football_team_points**: Football team points mapping
- **kpop_band_genres**: K-pop band genre reference
- **maze_solver**: Maze solving with breadth-first search
- **minute_parity_checker**: Odd/even minute detection
- **opponent_battle**: Opponent battle simulation
- **extract_unique_vowels**: Unique vowel extraction from a word
- **highest_lowest_ping**: Highest and lowest player ping detection
- **kpop_band_genres**: K-pop band genre reference
- **maze_solver**: Maze solving with breadth-first search
- **minute_parity_checker**: Odd/even minute detection
- **opponent_battle**: Opponent battle simulation
- **ranking_tracker_quidditch**: Quidditch ranking event tracking
- **score_average_and_pass_fail**: Score average and pass/fail analysis
- **string_list_to_integer_converter**: String list to integer conversion with validation
- **student_assessment_records**: Student assessment record management
- **strongest_and_weakest_student**: Strongest and weakest student selection

#### functions
Function definition and usage exercises:
- **ic_class_schedule_lookup**: IC class schedule lookup by date
- **mathematical_verification**: Recursive mathematical sequence verification
- **simple_calculator**: Basic calculator with modular function design

#### loops
Iterative programming exercises:
- **among_us_voting_simulator**: Voting simulation with loops
- **graph_pathfinder**: Graph traversal with DFS visualization
- **medicine_battle_simulator**: Subarray sum problem with nested loops
- **odd_numbers**: Odd number summation between 1 and 100
- **skrull_invasion_simulator**: Event-driven simulation with loops
- **spider_vs_rhino_battle_simulator**: Turn-based battle simulation
- **square_calculator**: Square calculation
- **sum_positives_and_count_negatives**: Sum of positive numbers and count of negative numbers

#### mathematical-calculations
Mathematical and computational exercises:
- **arithmetic_functions**: Input-driven arithmetic calculations
- **arithmetic_operations**: Arithmetic operations with factorial and operation modes
- **avatar_frequency_counter**: Avatar name frequency counting
- **average_of_two_numbers**: Average of two numbers
- **basic_arithmetic_functions**: Core arithmetic function definitions
- **circle_area_and_circumference**: Circle area and circumference
- **creature_element_index**: Creature and element index lookup
- **degrees_to_radians**: Degrees to radians conversion
- **fibonacci_membership_checker**: Fibonacci sequence membership check
- **fuel_price_ratio**: Petrol and alcohol price ratio
- **hourly_wage_calculator**: Hourly wage calculation
- **largest_and_smallest**: Largest and smallest value tracking
- **matrix_add_multiply_sequence**: Matrix addition and multiplication sequence
- **point_vector_operations**: Point/vector operations with coordinate parsing
- **prime_factorisation_and_line_selection**: Prime factorisation
- **profit_calculator**: Profit calculation
- **random_number_generator**: Random integer generation
- **rectangle_area_and_perimeter**: Rectangle area and perimeter
- **sphere_volume**: Sphere volume
- **sum_of_two_numbers**: Sum of two numbers
- **temperature_converter**: Celsius, Kelvin and Fahrenheit conversion
- **uniform_random_generator**: Uniform random number generation

#### strings
String manipulation and processing:
- **cake_recipe**: Cake recipe instructions
- **chance_calculator**: Fishing chance calculation
- **primitive_type_checker**: Python primitive type inspection
- **race_results**: Race results processing
- **string_indexing_demo**: String indexing demonstration
- **string_list_slicing_demo**: String list slicing and joins
- **word_presence_checker**: Word presence check

#### variables-and-input
Variable handling and user input processing:
- **accessing_characters**: Character access by index
- **age_converter**: Age conversions in years, months and days
- **area_calculator**: Area calculations for multiple shapes
- **ascii_pair_message_decryptor**: ASCII pair message decryption
- **celsius_to_fahrenheit**: Celsius to Fahrenheit conversion
- **client_data**: Client data collection
- **echo_user_message**: User message echo
- **global_message_demo**: Global message variable demonstration
- **global_variable_demo**: Global variable scope demonstration
- **local_variable_demo**: Local variable scope demonstration
- **name_and_city**: Name and city greeting
- **name_and_surname**: Name and surname input
- **name_input_with_defaults**: Name and surname input with default values
- **ranking_tracker_alt_events**: Alternative ranking event tracking
- **returned_message_demo**: Returned message demonstration
- **shop_payment_calculator**: Shop payment calculation
- **student_grade_status**: Student grade status
- **swap_two_values**: Swapping two values
- **text_replacer**: Text replacement and word counting
- **ticket_revenue_calculator**: Ticket revenue calculation
- **topic_voting_results**: Topic voting results
- **treasure_hunt_simulator**: Treasure hunt simulation

### 📁 file-organization
Practical automation and file management scripts:
- **organize_files**: File organization automation script

## Exercise Distribution Note

The distribution of exercises across categories has been reorganized for better balance:
- **Variables & Input (22 exercises)**: Extensive practice with foundational concepts
- **Conditionals (17 exercises)**: Building decision-making skills through repetition
- **Functions (3 exercises)**: Function concepts with practical examples
- **Loops (8 exercises)**: Iteration and algorithmic thinking
- **Mathematical Calculations (22 exercises)**: Mathematical operations and algorithms
- **Strings (7 exercises)**: String manipulation and text processing

The reorganized distribution provides a more balanced learning experience while maintaining focus on fundamental concepts.

## How to Run the Exercises

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Basic Execution

```bash
# Navigate to the specific exercise directory
cd algorithms-and-logic/conditionals

# Run the Python script
python arithmetic_calculator.py

# Or using python3
python3 arithmetic_calculator.py
```

### Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Run the exercise
python arithmetic_calculator.py

# Deactivate when done
deactivate
```

### Using an IDE
1. Open the entire `02-python` directory in your IDE (VS Code, PyCharm, etc.)
2. Navigate to the specific exercise
3. Right-click on the `.py` file and select "Run Python File"

## Learning Objectives

These exercises cover fundamental Python concepts:

- **Basic Syntax**: Variables, data types, operators
- **Control Flow**: If-else statements, match/case statements, loops
- **Functions**: Function definition, parameters, return values
- **Data Structures**: Lists, dictionaries, sets, tuples
- **String Manipulation**: String methods, formatting, regex
- **File Operations**: Reading and writing files
- **Mathematical Operations**: Calculations and formulas
- **Input/Output**: Console input and output operations
- **Algorithm Design**: Problem-solving approaches
- **Game Logic**: Basic game mechanics and systems

## Python Features Demonstrated

- **Type Hints**: Modern Python type annotations
- **f-strings**: String formatting
- **Match/Case**: Pattern matching (Python 3.10+)
- **List Comprehensions**: Concise list creation
- **Dictionary Operations**: Key-value data handling
- **Error Handling**: Try-except blocks
- **File Management**: OS and shutil operations

## Common Issues

### Python Version
- Some exercises may require Python 3.10+ for match/case statements
- Check Python version: `python --version`

### Module Imports
- Ensure all required modules are installed
- Install missing packages: `pip install package_name`

### Input Handling
- Some exercises expect specific input formats
- Check for proper input validation
- Handle potential input errors gracefully

## Next Steps

After completing these exercises, consider:
- Exploring Python frameworks (Django, Flask, FastAPI)
- Learning about data science libraries (pandas, numpy, matplotlib)
- Studying object-oriented programming in Python
- Building complete applications with Python
- Exploring asynchronous programming
- Learning about testing frameworks (pytest, unittest)

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
