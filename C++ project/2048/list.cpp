#include "list.h"
#include <iostream>
#include <string>
using namespace std;
int list::len()
{
    int i = 0;
    Node *temp = head;
    while (temp != NULL)
    {
        i = i + 1;
        temp = temp->next;
    }
    return i;
}
void list::push_head(string new_data)
{
    Node *new_node = new Node();
    new_node->data = new_data;
    new_node->next = head;
    new_node->prev = NULL;
    if (head)
    {
        head->prev = new_node;
    }
    head = new_node;
}
void list::push_tail(string new_data)
{
    Node *temp = new Node();
    temp->data = new_data;
    temp->next = NULL;
    if (head == NULL)
    {
        push_head(new_data);
    }
    else
    {
        Node *p = head;
        while (p->next != NULL)
        {
            p = p->next;
        }
        p->next = temp;
        temp->prev = p;
        return;
    }
}
void list::display_end()
{
    tail = get_end();
    Node *temp = tail;
    while (temp)
    {

        cout << temp->data << "<==>";
        temp = temp->prev;
    }
    cout << "NULL";
    return;
}
void list::display_head()
{
    Node *temp = head;
    while (temp)
    {
        cout << temp->data << "<==>";
        temp = temp->next;
    }
    if (temp == NULL)
    {
        cout << "NULL";
    }
}
string list::find(int index)
{
    int count = 0;
    Node *temp = head;
    int l = len();
    if (l == 1)
    {
        if (count == index)
        {
            return temp->data;
        }
    }
    while (temp)
    {
        count = count + 1;
        if (count == index)
        {
            return temp->data;
        }
    }
    return " ";
}

bool list::remove(string a)
{
    if (len() == 0)
    {
        return false;
    }
    else
    {
        Node *temp = head;
        if (len() == 1 && temp->data == a)
        {
            head = NULL;
            return true;
        }
        else if (len() == 1 && head->data != a)
        {
            return false;
        }
        else
        {
            Node *prev = temp;
            if (temp->data == a)
            {
                head = temp->next;
                temp->next = NULL;
            }
            else
            {
                while (temp != NULL)
                {
                    if (temp->data == a)
                    {
                        prev->next = temp->next;
                        temp->next = NULL;
                        return true;
                    }
                    prev = temp;
                    temp = temp->next;
                }
                return false;
            }
        }
    }
}
Node *list::get_end()
{
    Node *temp = head;
    while (temp->next)
    {
        temp = temp->next;
    }
    return temp;
}