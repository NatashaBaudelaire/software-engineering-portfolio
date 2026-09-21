package calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

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

    @Test
    @DisplayName("CT02: Subtract two positive integers")
    void subtractTwoPositiveIntegers_returnsDifference() {
        Calculator calculator = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 5.0;

        double obtainedResult = calculator.subtract(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT03: Multiply two positive integers")
    void multiplyTwoPositiveIntegers_returnsProduct() {
        Calculator calculator = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 50.0;

        double obtainedResult = calculator.multiply(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT04: Divide two positive integers")
    void divideTwoPositiveIntegers_returnsQuotient() {
        Calculator calculator = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 2.0;

        double obtainedResult = calculator.divide(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT05: Divide by zero throws ArithmeticException")
    void divideByZero_throwsArithmeticException() {
        Calculator calculator = new Calculator();
        double operand1 = 10, operand2 = 0;

        assertThrows(ArithmeticException.class, () -> calculator.divide(operand1, operand2));
    }
}