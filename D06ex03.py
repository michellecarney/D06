"""
write a function that reads from roster.txt prints the following information to the command line:
a. how many **FIRST** names contain the letter ‘e’
b. then lists the FIRST names which contain the letter ‘e’
"""
##go in and print it all in a list, and then separate the ones that are /n and ' '
import os

def read_roster_first_e():
    count = 0
    index = 0
    with open('roster.txt') as roster:
        name_list = roster.read().splitlines()
        first_name_list = [i.split(' ', 1)[0] for i in name_list]
        first_name_list_e = []
    try:
        if 'e' in first_name_list[index]:
            first_name_list_e[count] = first_name_list_e + first_name_list_e[count]
            count = count + 1
            index = index + 1
    except ValueError:
        index = index + 1
    else:
        index = index + 1
        ##I Don't know why this doesn't work :(

    print(first_name_list_e)
    print("There are " + str(count) + " people with e in their name. That's a lot of e's!")
    
    #exercise 4
    sample_file = open('D06ex03.txt', 'w')
    sample_file.write(str(first_name_list_e))
    sample_file.close()


def main():
    read_roster_first_e()


if __name__ == '__main__':
    main()
    