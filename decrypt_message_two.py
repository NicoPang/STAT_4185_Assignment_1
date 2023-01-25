encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
split_string = [*encrypted_message]
for i in range(1, len(split_string)//2 + 2, 2):
    temp = split_string[i]
    split_string[i] = split_string[i * -1 - 1]
    split_string[i * -1 - 1] = temp

print(''.join(split_string))
