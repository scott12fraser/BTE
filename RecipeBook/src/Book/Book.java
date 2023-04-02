package Book;

import Recipe.Recipes;

import java.io.Serializable;
import java.util.ArrayList;


public class Book implements Serializable {
    ArrayList<Recipes> recipesBook= new ArrayList<Recipes>();
    Recipes recipe;
    public void addRecipe(String name, String ingedints, int yeild, String methos){
        recipe = new Recipes(name,ingedints,yeild, methos);

        recipesBook.add(recipe);


    }

    public ArrayList<Recipes> getRecipeBook() {
        return recipesBook;
    }

    public ArrayList<String> getRecipeNames(){
        ArrayList<String> names = new ArrayList<String>();
        for (int i =0;i < recipesBook.size();i++){
             String name = recipesBook.get(i).getRepcipeName();
             names.add(name);


         }
       return names;

    }
    public ArrayList<String> getNewYeild(int i ,int yeildNew) {
        ArrayList<String> ing = recipesBook.get(i).getNewYeild(yeildNew);
        return ing;
    }
    public int getIwithName(String name2){
        ArrayList<String> names = getRecipeNames();
        int i =0;
        for (String name1 : names){
            if (name1.equals(name2)){
                return i;
            }


            i++;



        }


       return 0;
    }

    public Recipes getRecipeBookI(int listI) {
        Recipes r = recipesBook.get(listI);
        return r;
    }
}
