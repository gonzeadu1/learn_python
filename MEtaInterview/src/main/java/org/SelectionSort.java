package org;

public class SelectionSort {
    public static void selectionSort(int[] arr){
    for(int i = 0; i<arr.length;i++){
    int mindIndex = i;
    for(int j =i+1; j< arr.length; j++ ){
        if(arr[j] < arr[mindIndex]){
            mindIndex = j;
        }
    }
    if(mindIndex != i){
        int temp = arr[i];
        arr[i] = arr[mindIndex];
        arr[mindIndex] = temp;
    }}
    }

    public static void printArr(int[] arr) {
        System.out.print("nums: ");
        for (int nums : arr) {
            System.out.print("\n" + nums);
        }
    }


    public static void main(String[] args) {
        int[] arr = {10, 3, 848, 722, 29, 33, 92, 982, 73, 439};
        selectionSort(arr);
        printArr(arr);
    }
}
