package Resource;

import java.util.ArrayList;
import java.util.List;


class Resource {
    private String name;
    private String type;

    public Resource(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }
}


class Lesson {
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
}


public class AddResource {
    public static void main(String[] args) {
        Resource resource1 = new Resource("Multimedia Projector", "D");
        Resource resource2 = new Resource("Computer", "D");
        Resource resource3 = new Resource("Microscope", "F");

        Lesson lesson = new Lesson("2025-05-04", "Biology Practical Class");

        lesson.addResource(resource1);
        lesson.addResource(resource2);
        lesson.addResource(resource3);

        lesson.showLesson();
    }
}
