package Book;

import Recipe.Recipes;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;


import static java.lang.Integer.parseInt;

public class GUI {
    ArrayList<JButton> buttons;
    Book  myRecipeBook = new Book();
    int ActionCounter;
    JLabel recipe;
    JLabel recipeName;
    JLabel recipYeild;
    JLabel recipeMethod;
    JTextField methodText;
    FileInputStream fin =null;
    FileOutputStream fos  =null;
    ObjectOutputStream oos =null;
    ObjectInputStream ois =null;
    public JFrame addButtons(JFrame frame, ArrayList<String> recipename, GUI thisGui) {
        buttons = new ArrayList<>();
        ArrayList<String> recipenames =recipename;

        for (int i = 0; i < recipenames.size(); i++) {

            JButton recipe1 = new JButton(recipenames.get(i));

            buttons.add(recipe1);

        }
        int i =0;
        ActionCounter =0;
        for (JButton recipe1 : buttons) {



            recipe = new JLabel();
            recipeName = new JLabel();
            recipYeild = new JLabel();
            recipeMethod = new JLabel();
            recipeName.setBounds(30,30, 1500,200);
            recipe.setBounds(50,50, 1500,200);
            recipYeild.setBounds(170,30, 1500,200);
            recipeMethod.setBounds(50,70, 1500,200);
            recipe1.addActionListener(new ActionListener() {

                public void actionPerformed(ActionEvent e) {

                    ActionCounter = myRecipeBook.getIwithName(e.getActionCommand());
                    String name =  myRecipeBook.getRecipeBookI(ActionCounter).getRepcipeName();
                    String ingredints =  Arrays.toString(myRecipeBook.getRecipeBookI(ActionCounter).getIngedintsList());
                    int yeild = myRecipeBook.getRecipeBookI(ActionCounter).getYeildAmount();
                    String method =  myRecipeBook.getRecipeBookI(ActionCounter).getRecipeMethod();
                    recipe.setText(ingredints);
                    recipeName.setText(name);
                    recipYeild.setText("Yeild: "+yeild);
                    recipeMethod.setText(method);

                }
            });

            int y = 20 + 22 * (i + 1);
            recipe1.setBounds(2000, y, 200, 20);
            frame.add(recipe1);frame.add(recipe);frame.add(recipeName);frame.add(recipYeild);frame.add(recipeMethod);
            i++;
           // ActionCounter++;

        }
        return frame;
    }



    public JFrame addyeild(JFrame frame, GUI thisGui) {


            JButton yeildButton = new JButton("change yeild");







            yeildButton.setBounds(10,10, 160,20);
            JTextField yeildNew = new JTextField();
            yeildNew.setBounds(170,10, 100,20);
            yeildButton.addActionListener(new ActionListener() {

                public void actionPerformed(ActionEvent e) {
                    System.out.println(recipeName.getText());
                    ActionCounter = myRecipeBook.getIwithName(recipeName.getText());
                    System.out.println(ActionCounter);


                    String ingredints =  myRecipeBook.getNewYeild(ActionCounter, parseInt(yeildNew.getText())).toString();
                    System.out.println(ingredints);
                    int yeild = parseInt(yeildNew.getText());
                    recipe.setText(ingredints);
                    recipYeild.setText("Yeild: "+yeild);

                }
            });
        frame.add(yeildNew);
        frame.add(yeildButton);
            return frame;
        }

    public void addrecipes(String name, String ing, int yeild, String method) {


        myRecipeBook.addRecipe(name, ing, yeild, method);
        try {
            FileOutputStream fos = new FileOutputStream("Recipes.txt");

            ObjectOutputStream oos = new ObjectOutputStream(fos);

            oos.writeObject(myRecipeBook);

            oos.close();
            fos.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Error initializing stream");
            e.printStackTrace();
        }
    }
    public void loadrecipes(){

        //myRecipeBook.addRecipe("nansCookies", "226g margarine, 226g granulated sugar, 340g SFflour, 2tbsp golden syrup, chocolate chips ", 12);
        //myRecipeBook.addRecipe("Tartiflette", "5 garlic cloves, 4 oinions, 20 potatoes, 250g baconlardons, 2 wheeels of reblochan,oil,250ml white wine ", 12);
        try{
         FileInputStream fin = new FileInputStream("Recipes.txt");
         ObjectInputStream ois = new ObjectInputStream(fin);
         Book myRecipeBook1 = (Book) ois.readObject();
         myRecipeBook = myRecipeBook1;
         ois.close();
         fin.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Error initializing stream");
            e.printStackTrace();
        } catch (ClassNotFoundException e) {

            e.printStackTrace();
        }

    }

    public void displayAddRecipe(JFrame frame, GUI thisGui){
        JButton addButton = new JButton("Add new recipe");
        addButton.setBounds(10,1000, 160,20);

        JLabel dish = new JLabel("Dish title");
        dish.setBounds(200,950, 100,50);
        JLabel ingerdintLable = new JLabel("Ingredients");
        ingerdintLable.setBounds(300,950, 100,50);
        JLabel yeildLable = new JLabel("Yeild");
        yeildLable.setBounds(400,950, 100,50);
        JLabel method = new JLabel("Method");
        method.setBounds(500,950, 100,50);

        JTextField dishTitle = new JTextField();
        dishTitle.setBounds(200,1000, 100,50);
        JTextField newIngredints = new JTextField();
        newIngredints.setBounds(300,1000, 100,200);
        JTextField yeild = new JTextField();
        yeild.setBounds(400,1000, 100,50);
        methodText = new JTextField();
        methodText.setBounds(500,1000, 150,200);

        addButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
              System.out.println(newIngredints.getText());
              String methodText1 = methodText.getText();
              if (methodText == null){
                  methodText1 = "";
              }
              addrecipes(dishTitle.getText(),newIngredints.getText(),parseInt(yeild.getText()),methodText1);
              displayRecipeNames(frame, thisGui);
              dishTitle.setText("");
              newIngredints.setText("");
              yeild.setText("");
              methodText.setText("");
              frame.invalidate();
              frame.validate();
              frame.repaint();
            }
        });

        frame.add(addButton);frame.add(dishTitle);frame.add(newIngredints);frame.add(yeild);frame.add(dish);frame.add(ingerdintLable);frame.add(yeildLable);frame.add(methodText);frame.add(method);

    }
    public JFrame displayRecipeNames(JFrame frame, GUI thisGui){

        frame = thisGui.addButtons(frame , myRecipeBook.getRecipeNames(),thisGui);
        frame= thisGui.addyeild(frame ,thisGui);
        return frame;

    }
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setSize(120, 80);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Create JFrame Example");
        GUI thisGui = new GUI();
        thisGui.loadrecipes();
        frame = thisGui.displayRecipeNames(frame, thisGui);
        thisGui.displayAddRecipe(frame, thisGui);







        frame.setSize(1000,1000);
        frame.setLayout(null);


        frame.setVisible(true);



    }

}
