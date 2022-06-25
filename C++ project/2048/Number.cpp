#include"Number.h"
#include"board.h"
#include<Windows.h>
#include<string>
#include"list.h"
void gotoxy2(HANDLE hOut2, int x, int y)
{
	COORD pos;
	pos.X = x; //横坐标
	pos.Y = y; //纵坐标
	SetConsoleCursorPosition(hOut2, pos);
}
HANDLE hOut2 = GetStdHandle(STD_OUTPUT_HANDLE);//定义显示器句柄变量
Number::Number(Board& bd) :board(bd)
{

}
//设置随机的两个数字在游戏开始时候
void Number::setNumber()
{
	//为了保持数字在方格中间，使得数字坐标为3的奇数倍。
	int number[4] = { 3,9,15,21 };
	//棋盘出现的第二个数字随机从2或4中挑选
	int sample[2] = { 2,4 };
	int x1 = rand() % 4;
	int y1 = rand() % 4;
	int x2 = rand() % 4;
	int y2 = rand() % 4;
	if (board.check_full())
	{
		return;
	}
	while (true)
	{
		int x = rand() % 2;
		string n;
		string out;
		if (sample[x] == 2)
		{
			n = "2";
			out = "2";
		}
		if (sample[x] == 4)
		{
			n = "4";
			out = "4";
		}
		if (board.getnumber(number[x1], number[y1]) == " ")
		{
			board.setnumber(number[x1], number[y1], "2");
			//gotoxy2(hOut2,  number[y1]* 2, number[x1]);
			//cout << "2";
			if (board.getnumber(number[x2], number[y2]) == " ")
			{
				board.setnumber(number[x2], number[y2], n);
				//gotoxy2(hOut2, number[y2] * 2, number[x2]);
				//cout << out;
			}
			else
			{
				int a = number[x2];
				int b = number[y2];
				while (1)
				{
					x2 = rand() % 4;
					y2 = rand() % 4;
					if (number[x2] == a && number[y2] == b)
					{
						continue;
					}
					else if (number[x2] != a || number[y2] != b)
					{
						break;
					}

				}
				board.setnumber(number[x2], number[y2], n);
				gotoxy2(hOut2, number[y2] * 2, number[x2]);
				cout << out;
			}
			break;
		}


	}
}

//在棋盘上随机添加数字2
void Number::addNumber()
{
	int number[4] = { 3,9,15,21 };
	int x1 = rand() % 4;
	int y1 = rand() % 4;
	if (board.getnumber(number[x1], number[y1]) == " ")
	{
		board.setnumber(number[x1], number[y1], "2");
		return;
	}
	else if (board.getnumber(number[x1], number[y1]) != " ")
	{
		while (1)
		{
			x1 = rand() % 4;
			y1 = rand() % 4;
			if (board.getnumber(number[x1], number[y1]) == " ")
			{
				board.setnumber(number[x1], number[y1], "2");
				gotoxy2(hOut2, number[y1] * 2, number[x1]);
				break;
				return;
			}
			else
			{
				continue;
			}
		}
	}

}

//在棋盘上减少数字
bool Number::deleteNumber(int x, int y)
{
	if (board.getnumber(x, y) == " ")
	{
		return false;
	}
	else
	{
		board.setnumber(x, y, " ");
		gotoxy2(hOut2, y * 2, x);
		return true;
	}
}
/*
2048的基本逻辑就是，假如按键向上，有数字的一列中，先判断是否最顶端有数字，假如没有数字则跑到最顶端，假如有数字则判断两个数字是否一致，数字一致就叠加，数字不一致，则
该列中每一个数字都会根据列排开。其他方向一次类推
*/
void Number::moveNumber(char key)
{
	int number[4] = { 3,9,15,21 };
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int x = number[i];
			int y = number[j];
			if (board.getnumber(x, y) != " ")
			{
				if (key == UP)
				{
					move_UP(x, y);
				}
				else if (key == DOWN)
				{
					move_DOWN(x, y);
				}
				else if (key == LEFT)
				{
					move_LEFT(x, y);
				}
				else if (key == RIGHT)
				{
					move_Right(x, y);
				}
			}
		}
	}
	move++;
	addNumber();
	gotoxy2(hOut2, 0, 26);
	cout << "Move:" << move;
	gotoxy2(hOut2, 10, 26);
	cout << "Score:" << score;
}
bool Number::move_UP(int x, int y)
{
	int number[4] = { 3,9,15,21 };
	int temp_x = x;
	int temp_y = y;
	Node* temp = &board.nodearray_vertical[x][y];
	Node* cur;
	string str = temp->data;
	int n = 0;
	while (temp->prev)
	{
		temp = temp->prev;
		cur = temp->next;
		if (temp->data == " ")
		{
			deleteNumber(temp_x, y);
			temp_x = temp_x - 6;
			board.setnumber(temp_x, temp_y, str);
		}
		else if (temp->data != " ")
		{
			if (temp->data != cur->data)
			{
				break;
			}
			else
			{
				int a = stoi(temp->data);
				int b = stoi(cur->data);
				int c = a + b;
				score = score + c;
				string d = to_string(c);
				temp_x = temp_x - 6;
				board.setnumber(temp_x, temp_y, d);
				deleteNumber(temp_x + 6, y);
				break;

			}
		}

	}
	return true;
}
bool Number::move_DOWN(int x, int y)
{
	int number[4] = { 3,9,15,21 };
	int temp_x = x;
	int temp_y = y;
	Node* temp = &board.nodearray_vertical[x][y];
	Node* cur;
	string str = temp->data;
	while (temp->next)
	{
		temp = temp->next;
		cur = temp->prev;
		if (temp->data == " ")
		{
			deleteNumber(temp_x, y);
			temp_x = temp_x + 6;
			board.setnumber(temp_x, temp_y, str);
		}
		else if (temp->data != " ")
		{
			if (temp->data != cur->data)
			{
				break;
			}
			else if (temp->data == cur->data)
			{
				int a = stoi(temp->data);
				int b = stoi(cur->data);
				int c = a + b;
				score = score + c;
				string d = to_string(c);
				temp_x = temp_x + 6;
				board.setnumber(temp_x, temp_y, d);
				deleteNumber(temp_x - 6, y);
				break;
			}
		}

	}
	return true;
}
bool Number::move_Right(int x, int y)
{
	int number[4] = { 3,9,15,21 };
	int temp_x = x;
	int temp_y = y;
	Node* temp = &board.nodearray_horizontal[x][y];
	Node* cur;
	string str = temp->data;
	while (temp->next)
	{
		temp = temp->next;
		cur = temp->prev;
		if (temp->data == " ")
		{
			deleteNumber(x, temp_y);
			temp_y = temp_y + 6;
			board.setnumber(temp_x, temp_y, str);
		}
		else if (temp->data != " ")
		{
			if (temp->data != cur->data)
			{
				break;
			}
			else if (temp->data == cur->data)
			{
				int a = stoi(temp->data);
				int b = stoi(cur->data);
				int c = a + b;
				score = score + c;
				string d = to_string(c);
				temp_y = temp_y + 6;
				board.setnumber(temp_x, temp_y, d);
				deleteNumber(x, temp_y - 6);
				break;
			}
		}
	}
	return true;
}
bool Number::move_LEFT(int x, int y)
{
	int number[4] = { 3,9,15,21 };
	int temp_x = x;
	int temp_y = y;
	Node* temp = &board.nodearray_horizontal[x][y];
	Node* cur;
	string str = temp->data;
	while (temp->prev)
	{
		temp = temp->prev;
		cur = temp->next;
		if (temp->data == " ")
		{
			deleteNumber(x, temp_y);
			temp_y = temp_y - 6;
			board.setnumber(temp_x, temp_y, str);
		}
		else if (temp->data != " ")
		{
			if (temp->data != cur->data)
			{
				break;
			}
			else
			{
				int a = stoi(temp->data);
				int b = stoi(cur->data);
				int c = a + b;
				score = score + c;
				string d = to_string(c);
				temp_y = temp_y - 6;
				board.setnumber(temp_x, temp_y, d);
				deleteNumber(x, temp_y + 6);
				break;
			}
		}

	}
	return true;
}
bool Number::check_2048()
{
	int number[4] = { 3,9,15,21 };
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int x = number[i];
			int y = number[j];
			if (board.getnumber(x, y) == "2048")
			{
				return true;
			}
		}
	}
	return false;
}
void Number::reset_move(int n)
{
	move = n;

}
void Number::reset_score(int n)
{
	score = n;
}
bool Number::game_over()
{
	if (check_2048())
	{
		return true;
	}
	if (!board.check_full())
	{
		return false;
	}
	else if (board.check_full())
	{
		int number[4] = { 3,9,15,21 };
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (i == 0)
				{
					if (j == 0)
					{
						int x = number[i];
						int y = number[j];
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].next->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					else if (j == 3)
					{
						int x = number[i];
						int y = number[j];
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					else
					{
						int x = number[i];
						int y = number[j];
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;
						string str3_hor = board.nodearray_horizontal[x][y].next->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor) || (str1_hor == str3_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
				}
				else if (i == 3)
				{
					if (j == 0)
					{
						int x = number[i];
						int y = number[j];

						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].next->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					else if (j == 3)
					{
						int x = number[i];
						int y = number[j];
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					else
					{
						int x = number[i];
						int y = number[j];
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;
						string str3_hor = board.nodearray_horizontal[x][y].next->data;
						if ((str1_ver == str2_ver) || (str1_hor == str2_hor) || (str1_hor == str3_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
				}
				else
				{
					int x = number[i];
					int y = number[j];
					if (j == 1 || j == 2)
					{
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str3_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;
						string str3_hor = board.nodearray_horizontal[x][y].next->data;
						if ((str1_ver == str2_ver) || (str1_ver == str3_ver) || (str1_hor == str2_hor) || (str1_hor == str3_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					if (j == 0)
					{
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str3_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].next->data;;
						if ((str1_ver == str2_ver) || (str1_ver == str3_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}
					if (j == 3)
					{
						string str1_ver = board.nodearray_vertical[x][y].data;
						string str2_ver = board.nodearray_vertical[x][y].next->data;
						string str3_ver = board.nodearray_vertical[x][y].prev->data;
						string str1_hor = board.nodearray_horizontal[x][y].data;
						string str2_hor = board.nodearray_horizontal[x][y].prev->data;;
						if ((str1_ver == str2_ver) || (str1_ver == str3_ver) || (str1_hor == str2_hor))
						{
							return false;
						}
						else
						{
							continue;
						}
					}

				}
			}
		}
		return true;
	}

}