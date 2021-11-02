import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to) 

def main():
    access_token = 'P2zT3E0ZWVMAAAAAAAAAAYFOnxm60a9ql9LGL9bdVsMPdstEKqRCa3PhepSNpnsz'
    transferData = TransferData(access_token)

    f_from = input("Enter the file path: ")
    f_to = input("Enter file name in new destination: ")

    transferData.upload_file(f_from, f_to)
    print("Your file has been transfered!")

main()