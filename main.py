from datetime import datetime
import json

to_do_list = []
file_db = r"main_db.txt"

def save_file():
    json_to_do_list = json.dumps(to_do_list)
    with open(file_db, 'w') as file:
        file.write(json_to_do_list)

def read_file():
    with open(file_db, 'r') as file:
        file_read = json.loads(file.read())
        return file_read



while True:
    print('\n\n********** Welcome to my To Do List **********')
    print('1. Show tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Add/Change task deadline')
    print('5. Mark task as Done/Not Done')
    print('6. Exit and save')
    print('0. Change the DB file')

    choice = input('Enter your command number: ')

    to_do_list = read_file()

    # 1. Show tasks
    if choice == '1':
        print("\nTasks:")
        index = 0
        for i in to_do_list:
            index += 1

            status = "Not Done"
            if i["done"]:
                status = "Done"

            date_print = ''
            data_now = datetime.now()
            data_my = i["deadline"]
            if data_my != None:
                data_my_n = datetime.strptime(data_my, '%Y-%m-%d')
                if data_my_n > data_now:
                    total_seconds = (data_my_n - data_now).total_seconds()

                    days = int(total_seconds / 60 / 60 / 24)
                    hours = int((total_seconds / 60 / 60) % 24)
                    minutes = int((total_seconds / 60) % 60)

                    date_print = f" (Left: {days}days, {hours}hours, {minutes}min.)"

                else:
                    date_print = f" (Your task is overdue)"


            print(f'{index}. {i["task"]} --> (Deadline: {i["deadline"]}{date_print}) --> {status}')

    # 2. Add task
    elif choice == '2':
        add_task = input("Enter the new task: ")
        to_do_list.append({'task': add_task,
                           'done': False,
                           'deadline': None})

        save_file()

    # 3. Delete task
    elif choice == '3':
        number_task = int(input('Enter the task for delete: '))

        to_do_list.pop(number_task - 1)

        print(f'The task #{number_task} was deleted.')

        save_file()

    # 4. Add/Change task deadline
    elif choice == '4':
        number_task = int(input('Enter the task: ')) - 1

        if number_task <= len(to_do_list):
            to_do_list[number_task]["deadline"] = input("Please enter the deadline in the format (yyyy-mm-dd): ")
            save_file()
        else:
            print('\nThere is no such task.')

    # 5. Mark task as Done/Not Done
    elif choice == '5':
        number_task = int(input('Enter the task: ')) - 1

        if number_task <= len(to_do_list):

            if to_do_list[number_task]["done"]:
                to_do_list[number_task]["done"] = False
                save_file()
            else:
                to_do_list[number_task]["done"] = True
                save_file()

        else:
            print('\nThere is no such task.')

    # 6. Exit
    elif choice == '6':
        save_file()
        print("Exiting the To-Do List.")
        break

    # 0. Change the DB file
    elif choice == '0':
        file_db = input(r'Enter a new file name or file path: ')

    else:
        print("Invalid choice. Please try again.")






