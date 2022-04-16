package leetcode.sort;

public class SelectionSort {


    // 基础实现的选择排序（O（n^2）, O(1)） 不稳定 可以修改位稳定
    public static void selectionSort1(int[] arr){
        int minIndex;
        for (int i=0; i < arr.length -1; i++){
            minIndex = i;
            for (int j = i + 1; j < arr.length; j++){
                if (arr[minIndex] > arr[j]){
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    // 二元选择排序
    public static void selectionSort2(int[] arr){
        int minIndex, maxIndex;
        for(int i=0; i < arr.length/2; i++){
            minIndex = i;
            maxIndex = i;
            for (int j = i + 1; j < arr.length - i; j++){
                if (arr[minIndex] > arr[j]){
                    minIndex = j;
                }
                if (arr[maxIndex] < arr[j]){
                    maxIndex = j;
                }
            }
            if (minIndex == maxIndex) break;
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;

            if(maxIndex ==i ) maxIndex = minIndex;
            int lastIndex = arr.length - 1 -i;
            temp = arr[lastIndex];
            arr[lastIndex] = arr[maxIndex];
            arr[maxIndex] = temp;
        }
    }
}
