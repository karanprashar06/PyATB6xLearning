def add_security(func):

    def wrapper():
        print("1. Before the function is called")
        print("2. Wear helmet,Dashcam,gloves,take liscene")
        func()
        print("3. After the function is called")
        print("secure driving\n")
    return wrapper


@add_security
def drive_ola_scooter():
    print('Driving ola scooter')
@add_security
def drive_zypp_scooter():
    print('Driving zypp scooter')

drive_ola_scooter()
drive_zypp_scooter()