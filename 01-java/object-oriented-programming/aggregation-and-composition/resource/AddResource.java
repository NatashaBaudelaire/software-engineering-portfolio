package resource;

import java.util.ArrayList;
import java.util.List;

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
