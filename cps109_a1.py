'''
This program offers a streamlined solution to the complexities found in modern to-do list applications. 
Designed with simplicity in mind, it aims to replicate the straightforward functionality of traditional paper to-do lists. 
Users can easily manage an unlimited number of tasks, mirroring the ease of jotting down tasks on paper and crossing them off. 
By embracing this familiar approach, the program provides an uncomplicated and user-friendly alternative to more intricate digital task management tools. 
The focus is on creating a straightforward yet efficient to-do list experience, reminiscent of the simplicity that comes with a handwritten task list.
'''

print('\n')
print('Welcome to simplist-do!' + '\n')

def read_num_lines():
    with open('tasks.txt', 'r') as file:
        existing_tasks = file.readlines()
        length_lines = len(existing_tasks)
    return length_lines

def display_todo_list():
    print('Your tasks: ' + '\n')
    with open('tasks.txt', 'r') as file:
        i = 0
        for line in file:
            index = str(i+1)
            print(index + '. ' + line)
            i += 1
    
def add_task(num_tasks):
    read_num_lines()

    with open('tasks.txt', 'a') as file:
        for i in range(num_tasks):
            task = input('Please enter the task: ')
            file.write(str(task) + '\n')
        print('\n' + '*********      Done, tasks were added!      *********' + '\n')



def mark_done(num_tasks):
        
    
    tasks = load_from_file('tasks.txt')
    
    for i in range(num_tasks):
        task_index = int(input('Enter the index of the task to be crossed out (integer): '))
        
        if 1 <= task_index <= len(tasks):
            del tasks[task_index - 1]
        else:
            print('Invalid index. Please enter a valid index.')
            continue
    
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

    print('\n' + '******   Done, the task(s) was/were removed!   ******' + '\n')




def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []



def delete_everything():
    while True:
        yes_or_no = input('Are you sure you want to clear-out all tasks (y/n): ')
        if yes_or_no == 'y':
            with open('tasks.txt', 'w'):
                pass  
                # This block is intentionally left empty
            print('\n' + '******   Tasks Cleared!   ******' + '\n')
            break
            
        elif yes_or_no == 'n':
            print('\n' + '******   Your tasks are safe, action canceled!   ******' + '\n')
            break
            
        else:
            print('Invalid index. Please enter a valid index.')
            
            
            


while True:
    
    print('--------- Menu ---------' + '\n')
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Save and Quit")
    print('5. Delete all tasks'+ '\n')
    
    menu_input = input('Enter a number (1-5): ')
    
    print('\n' + '------------------------' + '\n')
    
    
    if menu_input == "1":
        display_todo_list()
    elif menu_input == "2":
        num_tasks = int(input('Enter the number of tasks to be added (integer): '))
        add_task(num_tasks)
    elif menu_input == "3":
        print('\n' + 'Your current tasks: ')
        display_todo_list()
        print('\n')
        num_tasks = int(input('Enter the number of tasks to be crossed out (integer): '))
        mark_done(num_tasks)
        
        
    elif menu_input == "4":
        
        print("To-Do list saved. Exiting program.")
        break
    elif menu_input == "5":
        delete_everything()
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
