# file = open("test.txt")
#
# line = file.readline()
#
# # while line != "":
# #     print(line)
# #     line = file.readline()
#
# newline = file.readlines()
# print(newline)
#
# for i in newline:
#     print(i)
#
#
# file.close()

with open("test.txt", "r") as reader:
    content = reader.readlines()
    # for i in reversed(content):
    #     # print(i)

    with open('test.txt', "w") as writer:
        for i in reversed(content):
            writer.write(i)

with open("test.txt", "r") as reader:
    content = reader.readlines()

    for i in content:
        print(i)