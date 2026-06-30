def student_details(**details):
    print(type(details))
    # ana=> <class 'dict'>
    print(details)
    # ans=>{'name': 'Nigam', 'Grade': 'a', 'Roll_n': 20, 'age': 6}

student_details(name="Nigam",Grade='a',Roll_n=20,age=6)

"""Explanation=> On the above function all the key-word-argument are stored in a dictionary data-format"""