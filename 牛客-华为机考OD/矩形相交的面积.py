"""
# !/usr/bin/env 全部
# -*- coding: utf-8 -*-
@Time        : 2022/4/11 17:46
@File        : 矩形相交的面积.py
"""

public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a1 = input.nextInt();
        int a2 = input.nextInt();
        int a3 = input.nextInt();
        int a4 = input.nextInt();
        int b1 = input.nextInt();
        int b2 = input.nextInt();
        int b3 = input.nextInt();
        int b4 = input.nextInt();
        int c1 = input.nextInt();
        int c2 = input.nextInt();
        int c3 = input.nextInt();
        int c4 = input.nextInt();
        int[] a = {a1, a2, a3, a4};
        int[] b = {b1, b2, b3, b4};
        int[] c = {c1, c2, c3, c4};

        int[] m = commonSpace(a, b);
        int[] commonSpace = commonSpace(m, c);
        System.out.println(commonSpace[2] * commonSpace[3]);

    }

    public static int[] commonSpace(int[] a, int[] b){
        int x11 = a[0];
        int y11 = a[1];
        int x12 = a[0]+a[2];
        int y12 = a[1]-a[3];

        int x21 = b[0];
        int y21 = b[1];
        int x22 = b[0]+b[2];
        int y22 = b[1]-b[3];

        int xx = Math.max(x11,x21);
        int yy = Math.min(y11,y21);

        int x = Math.min(x12,x22);
        int y = Math.max(y12,y22);

        return new int[]{xx,yy,Math.abs(xx-x),Math.abs(yy-y)};
    }

