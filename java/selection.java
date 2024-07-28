import java.util.*;

public class Main {
    public static void main(String[] args) {
      int[] unsorted = {1,5,7,4,10,8,3,2,0,6};
      System.out.print("Unsorted: ");
      for (int i = 0; i < unsorted.length; i++)  {
       System.out.print(unsorted[i] + ",");
     }
      for (int i = 0; i < unsorted.length; i++) {
        int selected = 0;
        for (int j = 1; j < unsorted.length; j++) {
          if (unsorted[selected] > unsorted[j])  {
            int temp = unsorted[selected];
            unsorted[selected] = unsorted[j];
            unsorted[j] = temp;
          }
          selected++;
        }
      }
      System.out.print("\nSorted: ");
     for (int i = 0; i < unsorted.length; i++)  {
       System.out.print(unsorted[i] + ",");
     }
  }
}