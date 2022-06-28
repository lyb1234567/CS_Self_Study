
#include <iostream>
void Show_Menu();
void Login_Admin();
int main()
{
    
    Show_Menu();
    return 0;
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
            std::cout << "sb" << std::endl;
            break;
        case 2:
            std::cout << "bc" << std::endl;
            break;
        default:
            break;
        }

    } while (choice != 3);

}


