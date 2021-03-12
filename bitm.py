dt = []
while True:
    print('Menu:\n'
          '1. Add Data\n'
          '2. Display Data\n'
          '3. Search Data\n'
          '4. Update Data\n'
          '5. Delete Data\n'
          '6. Exit')

    choice = input('Enter the Choice: ')

    if choice == '1':
        while True:
            inp = input('Enter data (enter "*" to return to the menu):')
            if inp != '*':
                dt.append(inp)
            else:
                break
    elif choice == '2':
        print('Entered Data: ', dt)
    elif choice == '3':
        ch = input('Enter the data you wan to search for: ')
        try:
            print('\"{}\" exists at the index of {}'.format(ch, dt.index(ch)))
        except Exception as e:
            print(e)
    if choice == '4':
        idx = int(input('Enter the index of the element you want to update: '))
        data = input('Enter data: ')
        try:
            dt[idx] = data
            print('updated data: ', dt)
        except Exception as e:
            print(e)
    if choice == '5':
        ch = input('Enter the data you want to remove: ')
        try:
            dt.remove(ch)
        except Exception as e:
            print('Updated Data list: ', dt)
    if choice == '6':
        break
