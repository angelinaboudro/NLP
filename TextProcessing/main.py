"""
Name: Angelina Boudro
Date: August 25th, 2020
Class: Human Language Technologies
"""

# import regress and picke into IDE
import re
import pickle

class Person:
# person class defined to get data. last, first, middle name, id, and phone number.
    def __init__(self, data):

        parsed_data = self.input_process(data)
        self.last_name = parsed_data[0]
        self.first_name = parsed_data[1]
        self.middle_initial = parsed_data[2]
        self.id = parsed_data[3]
        self.phone = parsed_data[4]

    def display(self):
# This is how it will be displayed in that order.
        print(self.last_name, self.first_name, self.middle_initial, self.id, self.phone)
        return self.first_name, self.middle_initial, self.last_name, self.id, self.phone

    def input_process(self, inputs):
        print(inputs)
        tokens = inputs.strip().split(',')        # Useing tokens to strip the ','

        for ind in range(len(tokens[:3])):
            if tokens[ind]:
                tokens[ind] = tokens[ind].lower()
                tokens[ind] = tokens[ind][0].upper() + tokens[ind][1:] # display for index
            else:
                tokens[ind] = ' N/a '  # if data missing, then leave N/a in its space.

        # pattern for id.
        id_pattern = "^[A-Za-z]{2}[0-9]{4}$"
        while not re.match(id_pattern, tokens[3]):
            print('Entered ID is invalid', tokens[3])
            print('ID is 2 letters, then 4 numbers, Please enter right format: ')
            tokens[3] = input()
            tokens[3] = tokens[3].upper()

        """
            phone number patter
            non-numeric objects will given an error. 
        """
        phone_pattern = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
        if not re.match(phone_pattern, tokens[4]):
            tokens[4] = re.sub('[^0-9]', '', tokens[4])

            tokens[4] = ''.join(tokens[4][:3]) + '-' + ''.join(tokens[4][3:6]) + '-' + ''.join(tokens[4][6:])
        return tokens # correct format for phone number token, seperated by the "-"


def main():
   #read data from the directory it is saved in. Must be saved in the same directory.
    with open('data.csv', 'r') as f:
        data = f.readlines()[1:] #hdeader is ignored.

    persons = {} # multiple people error, if the personal already exisit.
    for person in data:
        p = Person(person)
        if not p.id in persons.keys():
            persons[p.id] = p
        else:
            print("~~~~ Error!~~~ - person {} exists.".format(p.id))

# using pickle to verify and open close.
    with open('persons', 'wb') as file:
        pickle.dump(persons, file)
        file.close()

    with open('persons', 'rb') as file:
        persons = pickle.load(file)
        file.close()

    # lPerson class loop.
    for id, person in persons.items():
        print('Employee id: {}'.format(person.id))
        print('\t', person.first_name, person.middle_initial, person.last_name)
        print('\t', person.phone)
       #priint main.
if __name__ == '__main__':
    main()

'''
First run will show the first person with the correct ID, then search for the another correct ID, which will show the matching 
ID of the employee, the third time entering the same ID will list all the emplloyees that have the correct format ID 
'''