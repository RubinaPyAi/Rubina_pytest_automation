def print_message(message):
    def message_sender():
        print(message)
    message_sender()    
print_message("some random message")