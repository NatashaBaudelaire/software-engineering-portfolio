import java.util.Scanner;

public class CandidateStatus {

    public String determineStatus(int essayScore, int correctAnswers) {

        if (essayScore < 0 || essayScore > 500 || correctAnswers < 0 || correctAnswers > 50) {
            throw new IllegalArgumentException(
                "Invalid input values. " +
                "Essay score must be between 0 and 500. " +
                "Number of correct answers must be between 0 and 50."
            );
        }

        if (essayScore < 250 || correctAnswers < 25) {
            return "Disqualified";
        }

        if (essayScore >= 400 && correctAnswers >= 40) {
            return "Qualified for Next Phase";
        }

        return "Waiting List";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CandidateStatus evaluator = new CandidateStatus();

        try {
            System.out.print("Enter the essay score (0-500): ");
            int score = scanner.nextInt();

            System.out.print("Enter the number of correct answers (0-50): ");
            int answers = scanner.nextInt();

            String status = evaluator.determineStatus(score, answers);
            System.out.println("Candidate status: " + status);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An input error occurred. Please enter integers only.");
        } finally {
            scanner.close();
        }
    }
}