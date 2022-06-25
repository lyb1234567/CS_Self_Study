#include <string>
#include <iostream>
using namespace std;
#ifndef LIST_H
#define LIST_H
class Node
{
public:
    string data = " ";
    Node *next = NULL;
    Node *prev = NULL;
};
class list
{
private:
    Node *head = NULL;
    Node *tail = NULL;

public:
    Node *get_end();
    void push_head(string new_data);
    void push_tail(string new_data);
    void display_head();
    void display_end();
    bool remove(string a);
    Node *get_head() { return head; };
    string find(int index);
    int len();
};
#endif