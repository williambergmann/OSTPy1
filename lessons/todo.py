#!/usr/local/bin/python3
"""File-based to-do list maintainer."""

otasks = open('open_tasks.txt','a')
otasks.close()
dtasks = open('done_tasks.txt','a')
dtasks.close()
options = ('add', 'done', 'quit')
string_input = 'Pick an option from the list (%s): ' % ', '.join(options)
while True:
    open_tasks = open('open_tasks.txt','r').readlines()
    if open_tasks:
        print('-' * 10)
        print('Open Tasks')
        print('-' * 10)
        for i, task in enumerate(open_tasks):
            print(i, task.strip())
    done_tasks = open('done_tasks.txt','r').readlines()
    print('-' * 12)
    print('Done Tasks')
    print('-' * 12)
    for i, task in enumerate(done_tasks):
        print(i, task.strip())
    
    inp = input(string_input)
    if inp not in options:
        print('Please pick a valid option')
        continue
    if inp == 'add':
        new_task = input('Enter new task: ')
        tasks = open('open_tasks.txt','a')
        tasks.write(new_task + '\n')
        tasks.close()
    if inp == 'done':
        while True:
            done_task = input('Please enter the number of your completed task: ').strip()
            if done_task.isdigit():
                done_task = int(done_task)
                break
            print('Please enter a task number')
        open_tasks = open('open_tasks.txt','r').readlines()
        for i, task in enumerate(open_tasks):
            if i == done_task:
                print('Task removed: {0}'.format(task))    
                open_tasks.remove(task)
                f = open('open_tasks.txt','w')
                f.writelines(open_tasks)
                f.close()
                f = open('done_tasks.txt','a')
                f.write(task)
                f.close()
                break
    if inp == 'quit':
        break