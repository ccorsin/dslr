class Column:
    def __init__(self, data, i, count, titles, err):
        j = 0
        col = []
        try:
            float(data[0][i])
            self.type = 'Num'
        except:
            self.type = 'Str'
        while j < count:
            if self.type == 'Num':
                try:
                    col.append(float(data[j][i]))
                    j += 1
                except:
                    if j not in err:
                        err.append(j)
                    col.append(0)
                    j += 1
            else:
                col.append((data[j][i]))
                j += 1
        self.data = col
        self.len = len(self.data)
        self.name = titles[i]