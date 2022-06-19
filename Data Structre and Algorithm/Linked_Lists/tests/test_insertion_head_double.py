from Linked_Lists.Implementation.Double_Linked_List import double_linked_list

if __name__ == "__main__":
    a = double_linked_list()
    a.insertion_head(3)
    a.insertion_head(4)
    a.insertion_head(5)
    a.insertion_head(6)
    a.print_list()
    a.print_list_reverse()
