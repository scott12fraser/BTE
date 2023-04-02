package Recipe;

import java.io.Serializable;
import java.util.ArrayList;

public class Recipes implements Serializable {
    String repcipeName;
    String ingredintString;
    String[] ingedintsList ;
    int yeildAmount;
    // initliser method

    String recipeMethod;
    public Recipes(String name, String ingedints, int yeild, String method ) {
        repcipeName = name;
        ingredintString = ingedints;
        ingedintsList = ingStringToList(ingredintString);
        yeildAmount =yeild;
        recipeMethod = method ;
    }
   public String[] ingStringToList(String ingString){
        String[] ingredints = ingString.split(",");
        return ingredints;


   }
   public String getRecipeMethod(){
        return recipeMethod;

   }
    public String[] getIngedintsList(){
        return ingedintsList;
    }
    public int getYeildAmount(){
        return yeildAmount;

    }
    public String getRepcipeName() {
        return repcipeName;
    }

    public ArrayList<String> getNewYeild(int yeildNew){

        ArrayList<String> ingArray = new ArrayList<String>();
        for (int i=0;i < ingedintsList .length;i++){
            String ingEdit = ingedintsList [i] ;
            String Newingredint;
            if (ingEdit.replaceAll("[a-z,A-Z,\\s]","").equals("")){
                Newingredint = 1 + " x "+ ingEdit;
            }
            else {
                int amount = Integer.parseInt(ingEdit.replaceAll("[a-z,A-Z,\\s]", ""));
                String ing = ingEdit.replaceAll("[\\d]", "");

                ingedints currentIngerdint = new ingedints(amount, ing, yeildAmount);
                Newingredint = currentIngerdint.reconstrustor(yeildNew);
            }
            ingArray.add(Newingredint);



        }
        return ingArray;

   }
}



