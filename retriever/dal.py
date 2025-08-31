from pymongo import MongoClient

class Dal:

    uri = "mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/"

    def open_connection(self):
        try:
            client = MongoClient(self.uri)
            database = client["IranMalDB"]
            collection = database["tweets"]
            return collection
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        
    
        
    

