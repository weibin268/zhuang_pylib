# import sys
#
# for a in sys.path:
#     print(a)
try:
    f = open("d:/test.sql1")

except FileNotFoundError as error:
    print("error"+error.strerror)
finally:
    print("end")
