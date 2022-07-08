# Example 2
class SortedDict:
    def __init__(self) -> None:
        self.d = {}
        
    def add(self, key, value):
        if key in self.d or not self.d:
            self.d[key] = value
        else:
            self.d[key] = value   
            d2 = {}
            for k in self.d.keys():
                if not key in d2.keys() and key <= k:
                    d2[key] = value
                    d2[k] = self.d[k]
                elif k != key:
                    d2[k] = self.d[k]
            self.d = d2

    def __str__(self):
        s = ""
        for k in self.d.keys():
            s += f"{k}: {self.d[k]}, "
        if s != "":
            s = s[:-2]
        return "{" + s + "}"

    def remove(self, key):
        if(not key in self.d):
            raise IndexError
        else:
            del(self.d[key])

    def __add__(self, other):
        d_out = SortedDict()
        for k in self.d:
            d_out.add(k, self.d[k])
        for k in other.d:
            d_out.add(k, other.d[k])
        return d_out

    def __sub__(self, other):
        d_out = SortedDict()
        for k in self.d:
            d_out.add(k, self.d[k])
        for k in other.d:
            if k in d_out.d:
                d_out.remove(k)
        return d_out

