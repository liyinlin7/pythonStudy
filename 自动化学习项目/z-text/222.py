
import uuid

for i in range(10):
    uuid_name = uuid.uuid4()
    haa = str(uuid_name).split('-')[3]
    print (haa)