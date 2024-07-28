import java.util.*;

public class Main {
    public static void main(String[] args) {
      int[] unsorted = {1,5,7,4,10,8,3,2,0,6};
      System.out.print("Unsorted: ");
      for (int i = 0; i < unsorted.length; i++)  {
       System.out.print(unsorted[i] + ",");
     }
      for (int i = 0; i < unsorted.length; i++) {
        int insertion = i;
        while (insertion > 0) {
          if (unsorted[insertion-1] > unsorted[insertion])  {
            int temp = unsorted[insertion];
            unsorted[insertion] = unsorted[insertion-1];
            unsorted[insertion-1] = temp;
          }
          insertion--;
        }
      }
      System.out.print("\nSorted: ");
     for (int i = 0; i < unsorted.length; i++)  {
       System.out.print(unsorted[i] + ",");
     }
  }
}