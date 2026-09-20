package calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class CalculatorTest {

    @Test
    @DisplayName("CT01: Add two positive integers")
    void addTwoPositiveIntegers_returnsSum() {
        Calculator calculator = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 15.0;

        double obtainedResult = calculator.add(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }
}