Queue =  ["" for z in range(50)]
HeadPointer = -1
TailPointer = 0 

def Enqueue(ItemToAdd):
    global Queue,HeadPointer,TailPointer
    # print(ItemToAdd, "dgdfhewiuha")
    if TailPointer < 50:
        Queue[TailPointer] = ItemToAdd
        TailPointer = TailPointer + 1
        if HeadPointer == -1:
            HeadPointer = 0
    else:
        print("Queue is Full ....") 
        
def Dequeue():
    global Queue,HeadPointer,TailPointer

    if HeadPointer== -1 or HeadPointer==TailPointer:
        print("Queue is empty..")
        return  "Empty"
    else:
        return Queue[HeadPointer]
        HeadPointer +=1
        # print(Queue[HeadPointer])

def ReadData():
    try:
        GameFile = open("CAIE Practice/QueueData.txt","r")
        for i in GameFile:
            GameName = i.strip()
            Enqueue(GameName)
        GameFile.close()
    except FileNotFoundError:
        print("File not found")
# ReadData()
# print(Queue)
class RecordData:
    def __init__(self):
        #DECLARE Id: INTEGER
        #DECLARE Total : INTEGER
        self.Id = ""
        self.Total = 0
        

#DECLARE Records:ARRAY(0:50) OF RecordData
#DECLARE NumberRecord : INTEGER
Records = [RecordData() for e in range(50)]
NumberRecord = 0

def TotalData():
    global Records,NumberRecord
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecord == 0:
        Records[NumberRecord].Id = DataAccessed
        Records[NumberRecord].Total = 1
        NumberRecord += 1
        Flag = True
    else:
        for i in range(0, NumberRecord):
            if Records[i].Id == DataAccessed:
                Records[i].Total += 1
                Flag = True
                
    if Flag == False:
        Records[NumberRecord].Id = DataAccessed
        Records[NumberRecord].Total = 1
        NumberRecord += 1
        
def OutputRecords():
    for r in range(50):
        print("ID",Records[r].Id,"Total",Records[r].Total)
        
        
ReadData()
for i in range(23):
    TotalData()
OutputRecords()