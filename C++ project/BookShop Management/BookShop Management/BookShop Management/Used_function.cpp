#include "Used_function.h"
#include<iostream>
#include<string>
#include<fstream>
#include <conio.h>
struct Account
{
    std::string username;
    std::string password;
};
void Login_Admin()
{ 
    std::string input_name;
    std::string input_password;
    int choice;
    std::cout << "1. Regiseter" << std::endl;
    std::cout << "2. Just login !!" << std::endl;
    std::cin >> choice;
    switch (choice)
    {
    case 1:
        system("CLS");
        Register();
        break;
    case 2:
        system("CLS");
        std::cout << "User Name:";
        std::cin >> input_name;
        std::cout << "Password:";
        std::cin >> input_password;
        std::cout << "\n\n";
        std::string line;
        std::ifstream myfile("username_password.txt");
        if (myfile.is_open())
        {
            int count = 0;
            while (getline(myfile, line))
            {
                count++;
                if (count == 1 && input_name != line)
                {
                    std::cout << "The username or password is incorrect!!" << std::endl;
                    break;
                }
                if (count == 2 && input_password != line)
                {
                    std::cout << "The username or password is incorrect!!" << std::endl;
                    break;
                }
            }
            myfile.close();
        }
        else
        {
            std::cout << "Unable to open a file!!";
        }
        break;

    }
    

}
void Show_Menu()
{
    int choice;
    do
    {
        std::cout << "1.Admin" << std::endl;
        std::cout << "2.Student" << std::endl;
        std::cout << "3.Exit" << std::endl;
        std::cout << "\n\n";
        std::cout << "Enter your choice:" << std::endl;
        std::cin >> choice;
        switch (choice)
        {
        case 1:
            system("CLS");
            Login_Admin();
            break;
        case 2:
            system("CLS");
            std::cout << "bc" << std::endl;
            break;
        default:
            system("CLS");
            break;
        }
        std::cout << "\n\n";
    } while (choice != 3);

}
void Student()
void Register()
{
    char username[20] = { 0 };
    char password[20] = { 0 };
    Account account;
    std::ofstream MyFile("Register_1.txt");
    int i;

    std::cout << "Input your Username";
    for (int i = 0;i < 20;i++)
    {
        username[i] = _getch();
        _putch('*');
        if (username[i] == 13) break;
    }
    std::cout << "\n";
    std::cout << "Your Input Username is:" << username;

    
}