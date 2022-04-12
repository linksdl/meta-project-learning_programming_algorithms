
#include <iostream>

using namespace std;

void FindFront(int* nodes, int rows, int cols, int* fronts,int aim) {
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++) {
			if (nodes[i*rows+j]==aim)
			{
				fronts[i] = 1;
			}
			else if (nodes[i * rows + j] == -1)
			{
				break;
			}
		}
	}
}

struct nodeInfo {
	int index;
	int sum;
};
int MinActingTime(int* nodes, int rows, int cols) {
	if (nodes==nullptr||rows<=0||cols<=0)
	{
		return 0; // 处理异常情况
	}
	nodeInfo* maxArray = new nodeInfo[rows];
	for (int i = 0; i < rows; i++)
	{
		maxArray[i].index = -1;
		maxArray[i].sum = -1;
	} //初始化矩阵
	int maxSumAll = 0;

	int* fronts = new int[rows]; //建立一个front表，用于保存当前遍历节点的前序节点
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < rows; j++)
		{
			fronts[j] = 0;
		} //遍历一个节点前， 初始化front表数据
		FindFront(nodes, rows, cols, fronts, i);
		int maxFrontSum = -1;
		int maxFrontIndex = -1;
		for (int j = 0; j < rows; j++)
		{
			if (fronts[j]==1&&(maxArray[j].sum>maxFrontSum))
			{
				// 找到了前序节点，而且前序节点值比之前找到的前序节点还大，进行替换
				maxFrontSum = maxArray[j].sum;
				maxFrontIndex = j;
			}
		}
		if (maxFrontIndex==-1)
		{
			// 无前继节点的节点,最大值就是它自己
			maxArray[i].index = -1;
			maxArray[i].sum = nodes[i * rows];
			maxSumAll = maxArray[i].sum;
		}
		else {
			maxArray[i].index = maxFrontIndex;
			maxArray[i].sum = maxFrontSum + nodes[i * rows];
			if (maxSumAll<maxArray[i].sum)
			{
				maxSumAll = maxArray[i].sum;
			}
		}
	}
	delete[] maxArray;
	delete[] fronts;
	return maxSumAll;
}


int main()
{
    //测试用例1：复杂有向图求解
    // 答案：71
	int nodes[7][7] = {
				{10,1,2,3,-1,-1,-1},
				{9,3,4,5,-1,-1,-1},
				{22,4,5,-1,-1,-1,-1},
				{20,-1,-1,-1,-1,-1,-1},
				{19,-1,-1,-1,-1,-1,-1},
				{18,6,-1,-1,-1,-1,-1},
				{21,-1,-1,-1, - 1,-1,-1 } };
	cout<< MinActingTime((int*)nodes, 7, 7)<<endl;
	// 测试用例2：简单有向图求解
	// 答案：40
	int nodes2[7][7] = {
			{10,1,2,3,-1,-1,-1},
			{9,4,5,6,-1,-1,-1},
			{22,-1,-1,-1,-1,-1,-1},
			{20,-1,-1,-1,-1,-1,-1},
			{19,-1,-1,-1,-1,-1,-1},
			{18,-1,-1,-1,-1,-1,-1},
			{21,-1,-1,-1, -1,-1,-1 } };
	cout << MinActingTime((int*)nodes2, 7, 7)<<endl;
	// 测试用例3：前序节点为空的节点有2个
	// 答案：48
	int nodes3[7][7] = {
			{10,2,3,4,-1,-1,-1},
			{9,4,5,-1,-1,-1,-1},
			{22,-1,-1,-1,-1,-1,-1},
			{8,6,-1,-1,-1,-1,-1},
			{19,-1,-1,-1,-1,-1,-1},
			{18,6,-1,-1,-1,-1,-1},
			{21,-1,-1,-1, -1,-1,-1 } };
	cout << MinActingTime((int*)nodes3, 7, 7)<<endl;
	// 测试用例4：输入节点为1
	// 答案 10
	int nodes4[1][1] = { {10}};
	cout << MinActingTime((int*)nodes4, 1, 1) << endl;
	// 测试用例5：输入空，鲁棒性测试
	// 答案：0
	int** nodes5 = nullptr;
	cout << MinActingTime((int*)nodes5, 1, 1) << endl;
}
