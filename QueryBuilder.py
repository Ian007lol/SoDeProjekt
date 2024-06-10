class QueryBuilder:
    def __init__(self, base_query="SELECT * FROM images"):
        self.query = base_query
        self.conditions = []

    def add_condition(self, condition):
        self.conditions.append(condition)

    def remove_condition(self, condition):
        self.conditions.remove(condition)

    def build(self):
        if not self.conditions:
            return self.query
        return self.query + " WHERE " + " AND ".join(self.conditions)
