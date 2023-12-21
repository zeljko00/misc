import pickle
import shelve
class TestClass:
    def __init__(self,data):
        self.value=data

def serialize_pickle(object):
    with open("objects.bin","wb") as file:
        pickle.dump(object,file)
def deserialize_pickle():
    with open("objects.bin","rb") as file:
        return pickle.load(file)

# serializing object in dictionary-like file with shelve module
# key must be a string
def serialize_shelve(key,object):
    dict=shelve.open("dictionary.bin")
    dict[str(key)]=object
    dict.close()
def deserialize_shelve(key):
    dict = shelve.open("dictionary.bin")
    return dict[str(key)]

test=TestClass("VALUE")
key="object"
serialize_pickle(test.value)
serialize_shelve(key,test)
print("pickle:",deserialize_pickle())
print("shelve:",deserialize_shelve(key).value)
