class MyDict(dict):

    def get(self, key, default_value=0):
        if key in self.keys():
            return self[key]
        else:
            return default_value


new_dict = MyDict()
new_dict[1] = 10
new_dict[2] = 20
new_dict[3] = 30
print(new_dict.get(1))
print(new_dict.get(40))
