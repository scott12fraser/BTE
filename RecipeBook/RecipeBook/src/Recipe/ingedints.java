package Recipe;

import java.io.Serializable;
import java.text.DecimalFormat;

public class ingedints implements Serializable {

    String ing;
    int amount;
    int yeildIng ;
    public ingedints(int amountOf, String ingredint, int yeild) {
      ing  = ingredint;
      amount = amountOf;
      yeildIng = yeild;
    }
   public String reconstrustor(int Yeild){

        int newYeild = Yeild;
        double amount2 = amount;
        double yeildIng2 = yeildIng ;
        double oneAmount = amount2 / yeildIng2;
        double newAmount = oneAmount * newYeild;
       DecimalFormat value = new DecimalFormat("#.#");
       String newAmount2 = value.format(newAmount);

        String newIng = newAmount2 + ing  ;
        return newIng;


   }
}