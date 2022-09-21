class String(str):
    entity = ""

    def __init__(self, entity):
        self.entity = str(entity)

    def __add__(self, other):
        self.entity += str(other)
        return String(self.entity)

    def __sub__(self, other):
        return String(self.entity.replace(str(other), "", 1))

line = String("")
print(line)
print(String("New") + None)
print(String("rdtrdrtfvgutr45457")-5)