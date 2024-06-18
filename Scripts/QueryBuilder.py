# QueryBuilder.py
class QueryBuilder:
    def __init__(self, base_query="SELECT * FROM images"):
        self.query = base_query
        self.conditions = []
        self.order_by = None

    def add_condition(self, condition):
        self.conditions.append(condition)

    def remove_condition(self, condition):
        if condition in self.conditions:
            self.conditions.remove(condition)

    def add_order_by(self, order_by):
        self.order_by = order_by

    def build(self):
        query = self.query
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)
        
        if self.order_by:
            query += " ORDER BY " + self.order_by

        print("Generated Query: ", query)  # Debug output
        return query
