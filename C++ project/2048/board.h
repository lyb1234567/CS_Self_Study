#ifndef BOARD_H_
#define BOARD_H_
#include"list.h"
class Board
{
public:
	enum
	{
		ROW = 24, //行数
		COL = 25//列数
	};
	list a;
	void initwall();
	void drawall();
	void setnumber(int x, int y, string n);
	string getnumber(int x, int y);
	bool check_full();
	Node nodearray_horizontal[ROW][COL];
	Node nodearray_vertical[ROW][COL];
private:
	string gameborad[ROW][COL];



};
#endif // !BOARD_H_

#pragma once