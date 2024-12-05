class Student {
    int roll;
    String name;
    float marks;
        public  Student(){
            this.roll = 0;
            this.name = "N/A";
            this.marks = 0.0f;
        }
        
        public Student(int roll, String name, float marks){
            this.roll = roll;
            this.name = name;
            this.marks = marks;
        }
        
        public void show(){
            System.out.println("Student Roll:" + this.roll);
            System.out.println("Student Name:" + this.name);
            System.out.println("Student Marks:" + this.marks);
        }
}
public class Main{
    public static void main(String[] args){
        Student[] students = new Student [3];
        students[0] = new Student (4, "Soham", 85.0f);
        students[1] = new Student (7, "Sayak", 92.0f);
        students[2] = new Student (10, "Sayan", 77.0f);
        
        for (int i=0; i<students.length; i++){
            students[i].show();
            
        }
    }
}
