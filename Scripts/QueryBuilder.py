class QueryBuilder:
    def __init__(self, base_query="SELECT * FROM images"):
        self.query = base_query
        self.conditions = {}
        self.order_by = None

    def add_condition(self, key, condition):
        self.conditions[key] = condition

    def remove_condition(self, key):
        if key in self.conditions:
            del self.conditions[key]

    def add_order_by(self, order_by):
        self.order_by = order_by
    
    def add_between_condition(self, key, column, start_value, end_value):
        condition = f"{column} BETWEEN '{start_value}' AND '{end_value}'"
        self.add_condition(key, condition)
    
    def build(self):
        query = self.query
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions.values())
        
        if self.order_by:
            query += " ORDER BY " + self.order_by

        print("Generated Query: ", query)  # Debug output
        return query


