package Resource;

public class Resource {
    private String name;
    private String type;

    public Resource(String name, String type) {
        this.name = name;
        this.type = type;
    }

    @Override
    public String toString() {
        return name + " (" + type + ")";
    }
}

