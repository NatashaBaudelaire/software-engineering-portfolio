package glucoselevel;

public class GlucoseLevel {
    public int testId;
    public int glucoseLevel;

    public String getDiagnosis() {
        if (glucoseLevel < 100) {
            return "Normal";
        } else if (glucoseLevel <= 125) {
            return "Prediabetes";
        } else {
            return "Diabetes";
        }
    }
}
