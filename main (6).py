import java.util.ArrayList;

import java.util.Collections;

import java.util.Comparator, import java.util.List;

// Define a Student class to represent a

student

class Student { String name;

String rollNumber,

double cgpa;

public Student(String name, String

rollNumber, double cgpa) {

this.name = name;

this.rollNumber = rollNumber,

this.cgpa = cgpa;
}
Collections.sort(students, new CGPAComparator());

}

public static void main(String[] args) {

// Create a list of student objects

List<Student> students = new

ArrayList<>();

students.add(new Student("Alice", "A123",

3.8));

students.add(new Student("Bob", "B456",

3.5));

students.add(new Student("Charlie",

"C789", 3.9)); students.add(new Student("David",

"D101", 3.2));

students.add(new Student("Eve", "E202",

4.0));

// Sort the list of students based on