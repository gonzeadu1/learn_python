package org;

public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        boolean swappedFlag = false;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swappedFlag = true;
                }
            }
            if (!swappedFlag) {
                break;
            }
        }

    }


    public static void printArr(int[] arr) {
        System.out.print("nums: ");
        for (int nums : arr) {
            System.out.print("\n" + nums);
        }
    }


    public static void main(String[] args) {
        int[] arr = {10, 3, 848, 722, 29, 33, 92, 982, 73, 439};
        bubbleSort(arr);
        printArr(arr);
    }
}
