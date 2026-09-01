package single;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class CalculatorTest {

    @Test
    @DisplayName("CT01: Two positive integers")
    void testAddCT01() {

        Calculator calc = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 15.0;

        double obtainedResult = calc.add(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT02: Two positive integers")
    void testAddCT02() {

        Calculator calc = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 15.0;

        double obtainedResult = calc.add(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT03: Two positive integers")
    void testAddCT03() {

        Calculator calc = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 15.0;

        double obtainedResult = calc.add(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }

    @Test
    @DisplayName("CT04: Two positive integers")
    void testAddCT04() {

        Calculator calc = new Calculator();
        double operand1 = 10, operand2 = 5, expectedResult = 15.0;

        double obtainedResult = calc.add(operand1, operand2);

        assertEquals(expectedResult, obtainedResult);
    }
}