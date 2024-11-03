package org;

public class InsertionSort {
   public static void insertionSort(int[] arr){
       for(int i = 0; i<arr.length; i++){
           int temp= arr[i], j = i;
           while (j>0 && arr[j-1]> temp){
               arr[j] = arr[j-1];
               j--;
           }
           arr[j] = temp;
       }
   }

    public static void printArr(int[] arr) {
        System.out.print("nums: ");
        for (int nums : arr) {
            System.out.print("\n" + nums);
        }
    }
    public static void main(String[] args) {
        int[] arr = {106372282, 20202023, 6348, 79672, 2737279, 94949333, 2202092, 98222, 73, 439};
        insertionSort(arr);
        printArr(arr);
    }
}
