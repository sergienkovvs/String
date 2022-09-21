class String(str):
    entity = ""

    def __init__(self, entity):
        self.entity = str(entity)

    def __add__(self, other):
        return self.entity + str(other)

    def __sub__(self, other):
        return self.entity.replace(str(other), "", 1)

line = String("")
print(line)
print(String("New") + None)
print(String("rdtrdrtfvgutr45457")-5)