# class MessageManager:
#     def __init__(self, consumer, handler=None):
#         self.consumer = consumer
#         self.handler = handler
#         self.messages = []
#
#     def run(self):
#         for msg in self.consumer:
#             value = msg.value
#             if self.handler:
#                 self.handler.handle(value)
#             else:
#                 self.messages.append(value)




class MessageManager:
    def __init__(self, consumer, handler):
        self.consumer = consumer
        self.handler = handler

    def run(self):
        for msg in self.consumer:
            print(msg.value)
            self.handler.handle(msg.value)