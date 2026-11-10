class Inheritance {
    void show(){
        System.out.println("hello");
    }
    
}
    public static void main(String[] args){
        B obj = new B();
        obj.show();
    }
}
class B extends Inheritance{

}