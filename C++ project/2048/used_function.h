#ifndef USED_H_
#define USED_H_
#include<Windows.h>
#include<ctime>
#include<conio.h>
#include<fstream>
#include<vector>
#include<iostream>
using namespace std;
void gotoxy3(HANDLE hOut2, int x, int y);
void sort(vector<int>& array);
void show_score();
int max_val(vector <int>& array);
void set_cursor(bool visible);
void game();
void last_game();
inline bool exist(const std::string& name);
#endif // !USED_H_

#pragma once
