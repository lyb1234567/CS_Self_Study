#ifndef USED_FUNCTION
#define USED_FUNCTION
#include<string>
struct Account
{
    std::string username;
    std::string password;
};
void Add_Student();
Account Clean_username_password(std::string s1, std::string s2);
bool Check_password_requirement(char password[],int length);
bool Check_password_correct(std::string username,std::string password);
bool Check_exist(std::string name,std::string username, std::string password);
void Convert_to_csv();
void Delete_Student();
void Record_to_json(std::string s1,std::string s2,std::string s3,std::string s4,std::string s5,std::string s6 );
void Login_Admin();
void Register();
void Show_Single_Student();
void Show_All_Student();
void Show_Menu();
void Save_record();
void View_Student_Record();


#endif
#pragma once
