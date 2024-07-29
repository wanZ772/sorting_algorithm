import java.util.*;

public class Main {
    public static void main(String[] args) {
      int[] unsorted = {1,5,7,4,10,8,3,2,0,6};
      System.out.print("Unsorted array: ");
      for (int i = 0; i < unsorted.length; i++) {
        System.out.print(unsorted[i] + ",");
      }
      
      int[] sorted= new int[10];
      sorted = merge(unsorted);
      
      System.out.print("\nSorted array: ");
      for (int i = 0; i < sorted.length; i++) {
        System.out.print(sorted[i] + ",");
      }
  }
  static int[] merge(int[] array) {
    int n = array.length;
    if (n == 1) {
      return array;
    } else  {
      int mid = n / 2;
      int[] left = new int[mid];
      int[] right = new int[n-mid];
      
      for (int i = 0; i < n; i++) {
        if (i < mid)  {
          left[i] = array[i];
        } else  {
          right[i-mid] = array[i];
        }
      }
      
        left = merge(left);
        right = merge(right);

      int left_point = 0, right_point = 0, i = 0;
      int left_length = left.length, right_length = right.length;
      
      int[] sorted_array = new int[n];
      
      while ((left_point < left_length) && (right_point < right_length))  {
        if (left[left_point] < right[right_point])  {
          sorted_array[i] = left[left_point];
          left_point++;
        } else  {
          sorted_array[i] = right[right_point];
          right_point++;
        }
      
        i++;
        
      }
      
      while (left_point < left_length) {
        sorted_array[i] = left[left_point];
        left_point++;
        i++;
      }
      while (right_point < right_length) {
        sorted_array[i] = right[right_point];
        right_point++;
        i++;
      }
      return sorted_array;
    }
  }
}