import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token =access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        fileName = open(file_from, "rb")
        dbx.files_upload(fileName.read(), file_to)

def main():
    access_token = "cmMNq0OX0TEAAAAAAAAAAd7V34G9VZ-vClTMQwn6XeDa0gEtMClbu8GwrGc7oHOS"
    transferData = TransferData(access_token) ##automatically goes to contructor
    file_from = input("Path of your orignal file to be transferred?")
    f = input("File name to upload to Dropbox:")
    file_to = "/Test101/" + f
    transferData.uploadFile(file_from, file_to)
    print("The file has successfully moved to Dropbox.")


main()

