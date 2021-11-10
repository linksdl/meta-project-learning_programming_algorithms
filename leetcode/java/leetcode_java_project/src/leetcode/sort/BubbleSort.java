package leetcode.sort;

import java.util.Arrays;

public class BubbleSort {

    public static void main(String[] args) {
        int[] arr = new int[]{6, 2, 1, 3, 5, 4};
//        bubbleSort(arr);
//        bubbleSort1(arr);
        bubbleSort2(arr);
        // 输出: [1, 2, 3, 4, 5, 6]
        System.out.println(Arrays.toString(arr));
    }

    // 基础的冒泡排序
    public static void bubbleSort(int[] arr){
        for (int i=0; i< arr.length; i++){
            for (int j=0; j< arr.length - 1- i; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                }
            }
        }
    }

    // 加入判断 提前终止排序
    public static void bubbleSort1(int[] arr){
        boolean swapped = true;
        for (int i=0; i < arr.length -1; i++){
            if (!swapped) break;

            swapped = false;
            for (int j=0; j< arr.length - 1 - i; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                    swapped = true;
                }
            }
        }
    }

    public static void bubbleSort2(int[] arr){
        boolean swapped = true;
        int indexOfLastUnsortedElement = arr.length - 1;
        int swappedIndex = -1;
        while(swapped) {
            swapped = false;
            for (int i = 0; i < indexOfLastUnsortedElement; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                    swapped = true;
                    swappedIndex = i;
                }
            }
            indexOfLastUnsortedElement = swappedIndex;
        }
    }


    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void swap1(int[] arr, int i, int j){
        arr[j] = arr[i] + arr[j];
        arr[i] = arr[j] - arr[i];
        arr[j] = arr[j] - arr[i];
    }

    public static void swap2(int[] arr, int i, int j){
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
        arr[j] = arr[j] + arr[i];
    }

    public static void swap3(int[] arr, int i, int j){
        // 通过位运算
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[j] ^ arr[i];
        arr[i] = arr[i] ^ arr[j];
    }

}
