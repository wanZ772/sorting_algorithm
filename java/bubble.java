import java.util.*;

public class Main {
    public static void main(String[] args) {
      int[] unsorted = {1,5,7,4,10,8,3,2,0,6};
      
      for (int i = 0; i < unsorted.length; i++) {
        for (int j = 0; j < unsorted.length - 1; j++) {
          if (unsorted[j] > unsorted[j+1])  {
            int temp = unsorted[j];
            unsorted[j] = unsorted[j+1];
            unsorted[j+1] = temp;
          }
        }
      }
     for (int i = 0; i < unsorted.length; i++)  {
       System.out.print(unsorted[i] + ",");
     }
  }
}