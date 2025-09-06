sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)
  file.close()


with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)
  
  unsent_message = 'This message has been unsent.'
  file.truncate(0)  # Clear the file content
  file.write(unsent_message)
  file.seek(0)  # Move the cursor back to the beginning of the file to read the updated content
  line = file.readlines()
  print(line)
