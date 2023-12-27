# This is an interface. There is no function implementations inside.
# Only the function signature and pass keyword.

# Another class that extends this class has to implement all interface's functions.

# 因為我們的子類別需繼承 db.Model，這裡無法繼承 abc.ABC 做限制
class Jsonifiable():
    def jsonify(self):
        return NotImplemented
