
public class testMain{
    Object obj = "H";
    public void check(){
        if (obj instanceof Character){
            System.out.println("True");
        }else{
            System.out.println("False");
        }
    }
    public static void main(String[] args){
       
       testMain t = new testMain();
       t.check();
    }
}