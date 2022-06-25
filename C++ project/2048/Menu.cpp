#include "board.h"
#include"Number.h"
#include<iostream>
#include<Windows.h>
#include<ctime>
#include<conio.h>
#include<fstream>
#include<vector>
#include"list.h"
#include<iostream>
#include<string>
#include"Menu.h"
#include"used_function.h"
#include<stdlib.h>
HANDLE hOut1 = GetStdHandle(STD_OUTPUT_HANDLE);
string Menu::AsciiArt2048()
{
	constexpr auto title_card_2048 = R"(
   /\\\\\\\\\          /\\\\\\\                /\\\         /\\\\\\\\\
  /\\\///////\\\      /\\\/////\\\            /\\\\\       /\\\///////\\\
  \///      \//\\\    /\\\    \//\\\         /\\\/\\\      \/\\\     \/\\\
             /\\\/    \/\\\     \/\\\       /\\\/\/\\\      \///\\\\\\\\\/
           /\\\//      \/\\\     \/\\\     /\\\/  \/\\\       /\\\///////\\\
         /\\\//         \/\\\     \/\\\   /\\\\\\\\\\\\\\\\   /\\\      \//\\\
        /\\\/            \//\\\    /\\\   \///////////\\\//   \//\\\      /\\\
        /\\\\\\\\\\\\\\\   \///\\\\\\\/              \/\\\      \///\\\\\\\\\/
        \///////////////      \///////                \///         \/////////
  )";
	return title_card_2048;
}
Menu::Menu()
{

}
void Menu::start()
{
	string title = AsciiArt2048();
	char choice;

	do {
		cout << title;
		gotoxy3(hOut1, 30, 15);
		cout << "1:Start a new game(q to save)";
		gotoxy3(hOut1, 30, 16);
		cout << "2:Show the score ranking";
		gotoxy3(hOut1, 30, 17);
		cout << "3:Continue with the last game";
		gotoxy3(hOut1, 30, 18);
		cout << "4:Exit";
		gotoxy3(hOut1, 30, 19);
		cout << "Enter your choice:";
		cin >> choice;
		switch (choice)
		{
		case '1':
			gotoxy3(hOut1, 0, 0);
			game();
			break;
		case '2':
			system("cls");
			show_score();
			char key;
			cout << "Enter q to continue to return:";
			cin >> key;
			if (key == 'q')
			{
				system("cls");
				break;
			}
		case '3':
			system("cls");
			last_game();
			break;
		case '4':
			system("cls");
			exit(0);
			break;
		}

	} while (choice != '4');
}