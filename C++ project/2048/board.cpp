#include"board.h"
#include"list.h"
#include<iostream>
#include<string>
#include<conio.h>
#include<Windows.h>
#include<iomanip>
using namespace std;

void Board::initwall()
{
	int p = ROW / 4;
	int number[4] = { 3,9,15,21 };
	for (int i = 0; i < ROW; i++)
	{
		for (int j = 0; j < COL; j++)
		{
			//放墙壁的地方
			if (i == 0 || j == 0 || i == ROW - 1 || j == COL - 1 || (i % p) == 0 || (j % p) == 0)
			{
				gameborad[i][j] = '*';
				nodearray_horizontal[i][j].data = " ";
				nodearray_vertical[i][j].data = " ";
			}
			else
			{
				gameborad[i][j] = " ";
				//存放一个字符为空的结点
				nodearray_horizontal[i][j].data = " ";
				nodearray_vertical[i][j].data = " ";
			}
		}
	}
	int x;
	int y;
	int a;
	int b;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int x = number[i];
			int y = number[j];

			if (j == 0)
			{
				nodearray_horizontal[x][y].prev = NULL;
				nodearray_horizontal[x][y].next = &nodearray_horizontal[x][y + 6];
			}
			else if (j == 3)
			{
				nodearray_horizontal[x][y].next = NULL;
				nodearray_horizontal[x][y].prev = &nodearray_horizontal[x][y - 6];
			}
			else
			{
				nodearray_horizontal[x][y].next = &nodearray_horizontal[x][y + 6];
				nodearray_horizontal[x][y].prev = &nodearray_horizontal[x][y - 6];
			}
		}

	}
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int x = number[i];
			int y = number[j];
			if (i == 0)
			{
				nodearray_vertical[x][y].next = &nodearray_vertical[x + 6][y];
				nodearray_vertical[x][y].prev = NULL;
			}
			else if (i == 3)
			{
				nodearray_vertical[x][y].next = NULL;
				nodearray_vertical[x][y].prev = &nodearray_vertical[x - 6][y];
			}
			else
			{
				nodearray_vertical[x][y].next = &nodearray_vertical[x + 6][y];
				nodearray_vertical[x][y].prev = &nodearray_vertical[x - 6][y];
			}
		}
	}

}
HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
void Board::drawall()
{
	for (int i = 0; i < ROW; ++i)
	{
		for (int j = 0; j < COL; ++j)
		{
			//画的时候多加一个空格，看起来好看一些
			if (gameborad[i][j] == "2")
			{
				SetConsoleTextAttribute(hConsole, 2);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "4")
			{
				SetConsoleTextAttribute(hConsole, 12);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "8")
			{
				SetConsoleTextAttribute(hConsole, 13);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "16")
			{
				SetConsoleTextAttribute(hConsole, 14);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "32")
			{
				SetConsoleTextAttribute(hConsole, 6);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "64")
			{
				SetConsoleTextAttribute(hConsole, 3);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "128")
			{
				SetConsoleTextAttribute(hConsole, 3);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "256")
			{
				SetConsoleTextAttribute(hConsole, 5);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "512")
			{
				SetConsoleTextAttribute(hConsole, 11);
				cout << setw(3) << gameborad[i][j];
			}
			else if (gameborad[i][j] == "1024")
			{
				SetConsoleTextAttribute(hConsole, 12);
				cout << setw(3) << gameborad[i][j];
			}
			else
			{
				SetConsoleTextAttribute(hConsole, 7);
				cout << setw(3) << gameborad[i][j];
			}

		}
		if (i == 3)
		{
			cout << "Game:2048";
		}
		if (i == 4)
		{
			cout << "Version: 1.0";
		}
		if (i == 5)
		{
			cout << "Maker: Mirage";
		}
		if (i == 6)
		{
			cout << "a:left";
		}
		if (i == 7)
		{
			cout << "d:right";
		}
		if (i == 8)
		{
			cout << "w:up";
		}
		if (i == 9)
		{
			cout << "s:down";
		}
		cout << endl;
	}
}
void Board::setnumber(int x, int y, string n)
{

	gameborad[x][y] = n;
	nodearray_horizontal[x][y].data = n;
	nodearray_vertical[x][y].data = n;
}

string Board::getnumber(int x, int y)
{
	return gameborad[x][y];
}
bool Board::check_full()
{
	int count = 0;
	int number[4] = { 3,9,15,21 };
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (gameborad[number[i]][number[j]] != " ")
			{
				count = count + 1;
			}
		}
	}
	if (count == 16)
	{
		return true;
	}
	else
	{
		return false;
	}
}