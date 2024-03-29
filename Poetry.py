from random import random, randint
poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''

my_poem = []

#TODO: get a list of strings that contains lines of poem

lines = poem.split("\n")
lines.reverse()

def lines_printed_backwards():
    '''This function takes in a list of strings containing the lines of your poem as 
    arguments and will print the poem lines out in reverse with the line numbers reversed.'''

line_count = len(lines)
for i in range(len(lines)):
    line = lines[i]
    print(line)
    print(line_count)
    line_count -= 1

def lines_printed_random():
    '''will randomly select lines from a list of strings and print them out in random order. 
    Repeats are okay and the number of lines printed should be equal to the original number of lines in the poem (line numbers don't need to be printed). 
    Hint: try using a loop and randint()'''

    random_lines = len(lines)
    for i in range(len(lines)):
        line_index = randint(1, random_lines-1)
        print(lines[line_index])

def my_own_rearrange():
    response = input("Do you want to see a poem? Y or N?")
    if response == "Y":
        print(poem)
    elif response == "N":
        print("Too bad, so sad.")
    else:
        print(response)
#prints out a user input that requests them to print a Y for yes or N for no to write out the poem
lines_printed_random()
my_own_rearrange()
#lines_printed_backwards(lines)
#Testing code
#lines_printed_backwards(poem_lines_list)