# example of error handling
while True:
    try:
        2 + '2'
    except TypeError:
        print("Variables are of different type")
        break

