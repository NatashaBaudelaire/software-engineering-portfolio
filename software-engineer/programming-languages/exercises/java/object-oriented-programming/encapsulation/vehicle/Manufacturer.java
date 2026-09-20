package vehicle;

/**
 * Represents a vehicle manufacturer with a company name and country of origin.
 */
public class Manufacturer {

    private final String companyName;
    private final String country;

    /**
     * Constructor to create a Manufacturer.
     * @param companyName Name of the manufacturer company.
     * @param country Country where the manufacturer is based.
     */
    public Manufacturer(String companyName, String country) {
        this.companyName = companyName;
        this.country = country;
    }

    /**
     * @return The name of the manufacturer.
     */
    public String getCompanyName() {
        return companyName;
    }

    /**
     * @return The country of the manufacturer.
     */
    public String getCountry() {
        return country;
    }

    /**
     * Returns a string representation of the manufacturer.
     */
    @Override
    public String toString() {
        return companyName + " (" + country + ")";
    }
}
