#include<json/json.h>
#include<iostream>
#include<string>
#include<fstream>
#include <conio.h>
#include<cctype>
#include<Windows.h>
#include<fstream>
#include<algorithm>
#include "Used_function.h"
#include <iomanip>
void Add_Student()
{
    std::string name;
    std::string height;
    std::string weight;
    std::string username;
    std::string password;
    std::string age;
    std::string line;
    std::ofstream Myfile_out("record.txt",std::ios_base::app);
    std::ifstream Myfile_in("record.txt");
    Json::Value m_event;
    Json::StyledWriter styledWriter;
    std::fstream m_file;
    std::string s1;
    std::string s2;
    std::string s3;
    std::string s4;
    bool find = false;
    do {
        system("CLS");
        std::cout << "name:";
        std::cin >> name;
        std::cout << "Height:";
        std::cin >> height;
        std::cout << "Weight:";
        std::cin >> weight;
        std::cout << "Age:";
        std::cin >> age;
        std::cout << "Username:";
        std::cin >> username;
        std::cout << "Password:";
        std::cin >> password;
        int i = 0;
        while (!Myfile_in.eof())
        {
            Myfile_in >> line;
        }
        Myfile_out << "\n";
        find = Check_exist(name, username, password);
        if (!find)
        {
            std::cout << "Can not find the student information,please try again";
        }
        else
        {
            Myfile_out << name << std::setw(8) << height << std::setw(8) << weight << std::setw(8) << age << std::setw(18) << username << std::setw(18) << password;
            Record_to_json(name, height, weight, age, username, password);
        }
    } while (!find);
    
}
Account Clean_username_password(std::string s1, std::string s2)
{
    std::string new_user_name = "";
    std::string new_password = "";
    for (int i = 0;i < s1.length();i++)
    {
        if (s1[i] != '"')
            new_user_name = new_user_name + s1[i];
    }
    for (int i = 0;i < s2.length();i++)
    {
        if (s2[i] != '"' && s2[i] != '\\' && s2[i] != 'r')
            new_password = new_password + s2[i];
    }
    Account account;
    account.password = new_password;
    account.username = new_user_name;
    account.username.erase(remove(account.username.begin(), account.username.end(), '\n'), account.username.end());
    account.password.erase(remove(account.password.begin(), account.password.end(), '\n'), account.password.end());
    return account;
}
bool Check_password_requirement(char password[],int length)
{
    int count_upper = 0;
    int count_lower = 0;
    int count_digit = 0;
    for (int i = 0;i < length;i++)
    {
        if (isdigit(password[i]))
        {
            count_digit++;
        }
        if (isupper(password[i]))
        {
            count_upper++;
        }
        if (islower(password[i]))
        {
            count_lower++;
        }
    }
    if (count_digit == 0 || count_lower == 0 || count_upper == 0)
    {
        std::cout << "The password should have at least one uppercase letter, one lowercase letter and one number!!" << std::endl;
        return false;
    }
    return true;
}
bool Check_password_correct(std::string username,std::string password)
{
    std::cout << "\n\n";
    Json::Value account;
    std::ifstream account_file("record.json", std::ifstream::binary);
    account_file >> account;
    int size = account.size();
    password.erase(std::remove(password.begin(), password.end(), '\r'), password.end());
    username.erase(std::remove(username.begin(), username.end(), '\n'), username.end());
    for (int i = 0;i < size;i++)
    {
        std::string s1 = account[i]["Username"].toStyledString();
        std::string s2 = account[i]["Password"].toStyledString();
        Account s3 = Clean_username_password(s1, s2);
        s3.username.erase(std::remove(s3.username.begin(), s3.username.end(), '\n'), s3.username.end());
        s3.password.erase(std::remove(s3.password.begin(), s3.password.end(), '\n'), s3.password.end());
        std::cout << username << "\t" << s3.username << "\n";
        if (s3.username == username)
        {
            if (s3.password == password)
            {
                return true;
            }
            else
            {
                std::cout << "\n\n";
                break;
            }
        }
    }
    std::cout << "The username/password doesn't exist or not correct!!" << std::endl;
    return false;
}
bool Check_exist(std::string name,std::string username, std::string password)
{
    bool find = false;
    std::ifstream Myfile("Account.json");
    Json::Value json_obj;
    Myfile >> json_obj;
    int json_size = json_obj.size();
    username.erase(remove(username.begin(), username.end(), '\n'), username.end());
    password.erase(remove(password.begin(), password.end(), '\n'), password.end());
    name.erase(remove(name.begin(), name.end(), '\n'), name.end());
    for (int i = 0;i < json_size;i++)
    {
        Json::Value json_sub = json_obj[i];
        std::string username_json = json_sub["Username"].toStyledString();
        std::string password_json = json_sub["Password"].toStyledString();
        std::string name_json = json_sub["Name"].toStyledString();
        name_json.erase(remove(name_json.begin(), name_json.end(), '\n'), name_json.end());
        name_json.erase(remove(name_json.begin(), name_json.end(), '"'), name_json.end());
        Account account = Clean_username_password(username_json, password_json);
        bool check_username = (username == account.username);
        bool check_password = (password == account.password);
        bool check_name = (name == name_json);
        if (check_password && check_username&&check_name)
        {
            find = true;
            break;
        }
    }
    return find;
    
}
void Convert_to_csv()
{
    using namespace std;
    const char comma = ',';
    string line, word;

    ifstream in("record.txt");   if (!in) { cerr << "Can't open file"; return ; }
    ofstream out("record.csv");

    while (getline(in, line))          // get successive line of text
    {
        stringstream ss(line);
        bool first = true;
        while (ss >> word)               // get successive words per line
        {
            if (!first) out << comma;     // second and later words need a separator
            out << word;
            first = false;
        }
        out << '\n';                      // end of line of output
    }

    in.close();
    out.close();
}
void Delete_Student();
void Register()
{
    char username[20] = { 0 };
    char password[20] = { 0 };
    std::string name;
    int len = 0;
    bool check;
    do {
        std::cout << "Name:";
        std::cin >> name;
        std::cout << "User name:";
        std::cin >> username;
        std::cout << "Create your password (It should have at least one uppcase, one  lower case and one number):";
        for (int i = 0;i < 20;i++)
        {
            password[i] = _getch();
            len = len + 1;
            _putch('*');
            if (password[i] == 13) break;
        }
        check = Check_password_requirement(password, len - 1);
        if (!check)
        {
            system("CLS");
        }
    } while (!check);
    std::fstream m_file;
    m_file.open("Account.json", std::ios::in);
    std::cout << "\n\n";
    Json::Reader reader;
    Json::Value json_obj;

    //read the json file, and append the input username and password
    if (!reader.parse(m_file, json_obj, true))
    {
        // json file must contain an array
        std::cerr << "could not parse the json file" << std::endl;
        return;
    }

    m_file.close();

    Json::Value m_event;
    m_event["Name"] = name;
    m_event["Username"] = username;
    m_event["Password"] = password;//msg;

    // append to json object
    json_obj.append(m_event);
    // write updated json object to file
    m_file.open("Account.json", std::ios::out);
    m_file << json_obj.toStyledString() << std::endl;
    m_file.close();
    return;
}
void Record_to_json(std::string s1, std::string s2, std::string s3, std::string s4, std::string s5, std::string s6)
{
    Json::Value my_event;
    Json::StyledWriter styledWriter;
    std::fstream m_file;
    m_file.open("record.json", std::ios::in);
    std::cout << "\n\n";
    Json::Reader reader;
    Json::Value json_obj;
    bool find = Check_exist(s1, s5, s6);
    //read the json file, and append the input username and password
    if (!reader.parse(m_file, json_obj, true))
    {
        // json file must contain an array
        std::cerr << "could not parse the json file" << std::endl;
        return;
    }

    m_file.close();
    if (find)
    {
        Json::Value m_event;
        m_event["Name"] = s1;
        m_event["height"] = s2;
        m_event["weight"] = s3;
        m_event["age"] = s4;
        m_event["Username"] = s5;
        m_event["Password"] = s6;
        // append to json object
        json_obj.append(m_event);
        // write updated json object to file
        m_file.open("record.json", std::ios::out);
        m_file << json_obj.toStyledString() << std::endl;
        m_file.close();
    }
    else
    {
        std::cout << "Your added student information doesn't exist!!";
    }
}
void Login_Admin()
{
    std::string username;
    char password[20] = { 0 };
    bool check_username;
    bool check_password;
    do {
        system("CLS");
        std::cout << "Username:";
        std::cin >> username;
        std::cout << "Password:";
        for (int i = 0;i < 20;i++)
        {
            password[i] = _getch();
            _putch('*');
            if (password[i] == 13) break;
        }
        std::ifstream Myfile;
        Myfile.open("Admin.json");
        Json::Value admin;
        Myfile >> admin;
        std::string s1 = admin["Admin"]["Username"].toStyledString();
        std::string s2 = admin["Admin"]["Password"].toStyledString();
        Account admin_account = Clean_username_password(s1, s2);
        std::string password_string = password;
        password_string.erase(std::remove(password_string.begin(), password_string.end(), '\r'), password_string.end());
        admin_account.username.erase(std::remove(admin_account.username.begin(), admin_account.username.end(), '\n'), admin_account.username.end());
        admin_account.password.erase(std::remove(admin_account.password.begin(), admin_account.password.end(), '\n'), admin_account.password.end());
        check_username = admin_account.username == username;
        check_password = admin_account.password == password_string;
        std::cout << "\n\n";
        if (check_username)
        {
            if (check_password)
            {
                break;
            }
            else
            {
                std::cout << "The username/password doesn't exist or not correct!!";
            }
        }
        else
        {
            std::cout << "The username/password doesn't exist or not correctsadsas!!";
        }
        
    } while (!check_password || !check_username);
    std::cout << std::endl;
    system("CLS");
    int choice;
    do{
        system("CLS");
        std::cout << "1.Add a student's information." << std::endl;
        std::cout << "2.Delete a student's information." << std::endl;
        std::cout << "3.Show all the student's information" << std::endl;
        std::cout << "4.Back to the main menu" << std::endl;
        std::cout << "\n\n";
        std::cout << "Enter your choice:" << std::endl;
        std::cin >> choice;
        switch (choice)
        {
        case 1:
            system("CLS");
            Add_Student();
            break;
        case 2:
            system("CLS");
            std::cout << "Delete!";
        case 3:
            system("CLS");
            Show_All_Student();
            break;
        default:
            break;
        }
    } while (choice == 1 || choice == 2 || choice == 3);

}
void Show_All_Student()
{
    std::ifstream Myfile;
    Myfile.open("record.txt");
    std::string line;
    while (std::getline(Myfile, line))
    {
        line.erase(std::remove(line.begin(), line.end(), ','), line.end());
        std::cout << line << std::endl;
    }
    char choice;
    std::cout << "\n\n";
    do {
        std::cout << "Back to the menu(press q):";
        std::cin >> choice;
    } while (choice != 'q');
    
}
void Show_Single_Student()
{
    using namespace std;
    char password[20] = { 0 };
    std::string name;
    std::string username;
    Json::Value json_obj;
    Json::Value target;
    std::ifstream Myfile_in("record.json");
    Myfile_in >> json_obj;
    int size = json_obj.size();
    bool check_name;
    bool check_username_password;
    bool find = false;
    char choice;
    do {
        system("CLS");
        std::cout << "Name:";
        std::cin >> name;
        std::cout << "Username:";
        std::cin >> username;
        std::cout << "Password:";
        for (int i = 0;i < 20;i++)
        {
            password[i] = _getch();
            _putch('*');
            if (password[i] == 13) break;
        }
        string new_password = password;
        name.erase(std::remove(name.begin(), name.end(), '\n'), name.end());
        for (int i = 0;i < size;i++)
        {
            Json::Value json_obj_sub = json_obj[i];
            string s1 = json_obj_sub["Name"].toStyledString();
            s1.erase(std::remove(s1.begin(), s1.end(), '\n'), s1.end());
            s1.erase(std::remove(s1.begin(), s1.end(), '"'), s1.end());
            check_username_password = Check_password_correct(username,password);
            check_name = (name == s1);
            if (check_name && check_username_password)
            {
                find = true;
                target = json_obj[i];
                break;
            }
        }
        if (!find)
        {
            cout << "\n";
            cout << "The information is not correct,try again(Y/N):";
            cin >> choice;
        }
        else
        {
            break;
        }
    } while (choice=='y');
    system("CLS");
    string name_ = target["Name"].toStyledString();
    string height_ = target["height"].toStyledString();
    string weight_ = target["weight"].toStyledString();
    string age_ = target["age"].toStyledString();
    name_.erase(std::remove(name_.begin(), name_.end(), '"'), name_.end());
    height_.erase(std::remove(height_.begin(), height_.end(), '"'), height_.end());
    weight_.erase(std::remove(weight_.begin(), weight_.end(), '"'), weight_.end());
    age_.erase(std::remove(age_.begin(), age_.end(), '"'), age_.end());
    name_.erase(std::remove(name_.begin(), name_.end(), '\n'), name_.end());
    height_.erase(std::remove(height_.begin(), height_.end(), '\n'), height_.end());
    weight_.erase(std::remove(weight_.begin(), weight_.end(), '\n'), weight_.end());
    age_.erase(std::remove(age_.begin(), age_.end(), '\n'), age_.end());
    cout << name_ << "\t" << height_ << "\t" << weight_ << "\t" << age_;
    char new_choice;
    do {
        cout << "\n";
        cout << "Press q to return:";
        char choice;
        cin >> new_choice;
    } while (new_choice != 'q');
}
void Student()
{ 
    std::string input_name;
    std::string input_password;
    int choice;
    do {
        system("CLS");
        std::cout << "1. Regiseter" << std::endl;
        std::cout << "2. Just login !!" << std::endl;
        std::cout << "3. Move to the main interface" << std::endl;
        std::cin >> choice;
        switch (choice)
        {
        case 1:
            system("CLS");
            Register();
            break;
        case 2:
        {
            system("CLS");
            Show_Single_Student();
            choice = 'q';
            break;
        }
        default:
            break;
        }
    } while (choice==1 || choice==2);
}
void Show_Menu()
{
    system("CLS");
    int choice;
    do {
        system("CLS");
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
            Student();
            break;
        default:
            system("CLS");
            Convert_to_csv();
            break;
        }
        std::cout << "\n\n";
    } while (choice == 1 || choice == 2);
}
