#include"used_function.h"
#include"Number.h"
#include"board.h"
#include<Windows.h>
#include<ctime>
#include<conio.h>
#include<fstream>
#include<vector>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
void gotoxy3(HANDLE hOut2, int x, int y)
{
	COORD pos;
	pos.X = x;
	pos.Y = y;
	SetConsoleCursorPosition(hOut2, pos);
}

void sort(vector<int>& array)
{
	int temp;
	for (int i = 0; i < array.size(); i++)
	{
		for (int j = i + 1; j < array.size(); j++)
		{
			if (array[i] < array[j])
			{
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
		}
	}
}

void show_score()
{
	ifstream inFile;
	string filename = "score.txt";
	inFile.open(filename);
	int Best;
	vector<int> score_array;
	while (inFile >> Best)
	{
		score_array.push_back(Best);
	}
	sort(score_array);
	for (int i = 0; i < score_array.size(); i++)
	{
		cout << score_array[i] << endl;
	}
}

int max_val(vector <int>& array)
{
	int max = array[0];
	for (auto i = array.begin(); i != array.end(); ++i)
	{
		if (max <= *i)
		{
			max = *i;
		}
	}
	return max;
}

void set_cursor(bool visible) {
	CONSOLE_CURSOR_INFO info;
	info.dwSize = 100;
	info.bVisible = visible;
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
}

HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
void game()
{
	ofstream outFile;
	ofstream out;
	ifstream inFile;
	string filename = "score.txt";
	string last = "last.txt";
	outFile.open(filename, std::ios_base::app);
	inFile.open(filename);
	int Best = 0;
	int new_Best = 0;
	vector<int> score_array;
	while (inFile.good())
	{
		inFile >> Best;
		score_array.push_back(Best);
	}

	Best = max_val(score_array);
	srand((unsigned int)time(NULL));
	Board board;
	board.initwall();
	Number number(board);
	int  i = 0;
	number.setNumber();
	board.drawall();
	bool game_over = number.game_over();
	while (!game_over)
	{
		set_cursor(true);
		gotoxy3(hOut, 0, 24);
		int c = _getch();
		if (c == 113)
		{
			out.open(last);
			int number_array[4] = { 3,9,15,21 };
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					int x = number_array[i];
					int y = number_array[j];
					if (board.getnumber(x, y) != " ")
					{
						out << x << " " << y << " " << board.getnumber(x, y);
						out << endl;
					}
				}
			}
			out << number.move_count() << " " << number.get_score() << " " << "end";
			break;
		}
		if (c == 224)
		{
			char key = _getch();
			number.moveNumber(key);
			set_cursor(false);
			gotoxy3(hOut, 0, 27);
			if (number.get_score() < Best)
			{
				cout << "Best:" << Best;
			}
			else
			{
				cout << "Best:" << number.get_score();
			}
			gotoxy3(hOut, 0, 0);
			board.drawall();
		}
		game_over = number.game_over();
	}
	gotoxy3(hOut, 0, 27);
	if (game_over == true)
	{
		cout << "game over";
	}
	else
	{
		cout << "Game saved!!";
	}
	int score = number.get_score();
	outFile << score << endl;
	outFile.close();
	Sleep(1000);
	system("cls");

}

void last_game()
{
	ofstream out;
	ifstream in;
	Board board;
	board.initwall();
	Number number(board);
	string a, b, c;
	in.open("last.txt");
	while (in.good())
	{
		in >> a >> b >> c;
		int a_int = stoi(a);
		int b_int = stoi(b);
		if (c == "end")
		{
			number.reset_move(a_int);
			number.reset_score(b_int);
		}
		else
		{
			board.setnumber(a_int, b_int, c);
		}
	}
	board.drawall();
	srand((unsigned int)time(NULL));
	bool game_over = number.game_over();
	string filename = "score.txt";
	ofstream Outfile;
	ifstream infile;
	Outfile.open(filename, std::ios_base::app);
	infile.open(filename);
	vector<int> score_array;
	int Best;
	while (infile.good())
	{
		infile >> Best;
		score_array.push_back(Best);
	}
	Best = max_val(score_array);
	while (!game_over)
	{
		set_cursor(true);
		gotoxy3(hOut, 0, 24);
		int c = _getch();
		if (c == 113)
		{
			out.open("last.txt");
			int number_array[4] = { 3,9,15,21 };
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					int x = number_array[i];
					int y = number_array[j];
					if (board.getnumber(x, y) != " ")
					{
						out << x << " " << y << " " << board.getnumber(x, y);
						out << endl;
					}
				}
			}
			out << number.move_count() << " " << number.get_score() << " " << "end";
			break;
		}
		if (c == 224)
		{
			char key = _getch();
			number.moveNumber(key);
			set_cursor(false);
			gotoxy3(hOut, 0, 27);
			if (number.get_score() < Best)
			{
				cout << "Best:" << Best;
			}
			else
			{
				cout << "Best:" << number.get_score();
			}
			gotoxy3(hOut, 0, 0);
			board.drawall();
		}
		game_over = number.game_over();
	}
	gotoxy3(hOut, 0, 27);
	if (game_over == true)
	{
		cout << "game over";
	}
	else
	{
		cout << "Game saved!!";
	}
	int score = number.get_score();
	Outfile << score << endl;
	in.close();
	out.close();
	Outfile.close();
	infile.close();
	Sleep(1000);
	system("cls");
}

inline bool exist(const std::string& name)
{
	struct stat buffer;
	return (stat(name.c_str(), &buffer) == 0);
}