def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class Ids:
    def __init__(self):
        self.id = 0
        self.ids = {}

    def add(self, key: str):
        if key not in self.ids:
            self.ids[key] = self.id
            self.id += 1

        return self.ids[key]

    def size(self):
        return self.id

    def get_map(self):
        return {v: k for k, v in self.ids.items()}