package resource;

import java.util.ArrayList;
import java.util.List;

public class Lesson {
    private String date;
    private String title;
    private List<Resource> resources;

    public Lesson(String date, String title) {
        this.date = date;
        this.title = title;
        this.resources = new ArrayList<>();
    }

    public void addResource(Resource resource) {
        resources.add(resource);
    }

    public void showLesson() {
        System.out.println("Lesson: " + title);
        System.out.println("Date: " + date);
        System.out.println("Resources:");
        for (Resource r : resources) {
            System.out.println("- " + r.getName() + " (Type: " + r.getType() + ")");
        }
    }

    public String getName() {
        return title;
    }

    public String getType() {
        return "Lesson";
    }

    @Override
    public String toString() {
        return title + " (Type: Lesson)";
    }
}
