try:

    f = open("test_file.py")

    lines = f.readlines()

    for line in lines:
        print(line,end='')

except FileNotFoundError as error:

    print("error"+error.strerror)

finally:
    print("end")

