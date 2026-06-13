import java.util.*;
public class AdoptPet {
    /**
     * SCRATCH WORK
     * String name = [sadie,woof,chirpy,lola];
     * String breed = [dog , cat,dog,dog];
     * int days = [4,7,2,1]
     * priorityQueue<days, Map<Name,breed>>
     * 
     * 
     * 
     * time complxity: time compxlioty O(n log n)
     * space o(n)
     * time spend 35min
     */
    static class Pet implements Comparable<Pet>{
        String name;
        String breed;
        int days;
        
        public Pet(String name,String breed, int days){
            this.name = name;
            this.breed = breed;
            this.days = days;
        

        }
        @Override
        public int compareTo(Pet other){
            return Integer.compare(this.days,other.days);
        }
    }
    public static Pet adoptPet(List<Pet> initialInput, String name, String type, String dogType){
       
        PriorityQueue<Pet> dog = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Pet> cat = new PriorityQueue<>(Collections.reverseOrder());
        if(!type.equals("Person")){
            initialInput.add(new Pet(name,dogType,0));
        }else{
             for(Pet pet: initialInput){
             
            if(pet.breed.equals("dog")){
                dog.add(pet);
            }else{
                cat.add(pet);
            }

        }
        if(dogType.equals("dog")){
              
            if(!dog.isEmpty()){
                initialInput.remove(dog.peek());
                return dog.poll();
               
            }
            if(!cat.isEmpty()){
                initialInput.remove(cat.peek());
                return cat.poll();
            }
        }else{
            
            if(!cat.isEmpty()){
                  initialInput.remove(cat.peek());
                return cat.poll();
            }
            if(!dog.isEmpty()){
                  initialInput.remove(dog.peek());
                return dog.poll();
            }
        }
        }
       
        return new Pet("","",0);
        

        
       

    }

    public static  void main(String[] args){
       
        List<Pet> intialInput = new ArrayList<>();
        Pet first = new Pet("Sadie","dog",4);
         Pet second = new Pet("Woof","cat",7);
          Pet third = new Pet("Chirpy","dog",2);
           Pet fourth = new Pet("Lola","dog",1);

        intialInput.add(first);
        intialInput.add(second);
        intialInput.add(third);
        intialInput.add(fourth);
        Pet result = adoptPet(intialInput, "Bob", "Person", "dog");
        Pet result1 = adoptPet(intialInput, "Floofy", "", "cat");
        
        Pet result2 = adoptPet(intialInput, "Sally", "Person", "cat");
        Pet result3 = adoptPet(intialInput, "Ji", "Person", "cat");
        Pet result4 = adoptPet(intialInput, "Ali", "Person", "cat");
        System.out.println( result.name + ", " + result.breed);
        System.out.println( result1.name + ", " + result1.breed);
        System.out.println( result2.name + ", " + result2.breed);
        System.out.println( result3.name + ", " + result3.breed);
        System.out.println( result4.name + ", " + result4.breed);
    }
}
