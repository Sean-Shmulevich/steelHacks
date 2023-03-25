import datetime

class pastOrders:
    def __init__(self, oID, custName, busName, date, total, status):
        self._oID = oID
        self._custName = custName
        self._busName = busName
        self._date = date
        self._total = total #total price fo order
        self._status = status #past or pending order

    # uid
    def get_oID(self):
        return self._uid
    
    def set_oID(self, oID):
        self._oID = oID
    

    # busName
    def get_busName(self):
        return self._busName
    
    def set_busName(self, busName):
        self._busName = busName
    
    
    # date
    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date
    
    # total
    def get_total(self):
        return self._total
    
    def set_total(self, total):
        self._total = total
    
    # status
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status



order1 = pastOrders("2100", "Olivia Johnson", "Grandma's Edibles", datetime.datetime(2023, 3, 25, 12, 30, 0), "69.69", "pending")
order2 = pastOrders("4394", "Ethan Lee", "Grandma's Edibles", datetime.datetime(2021, 3, 25, 5, 50, 0), "36.72", "pending")
order3 = pastOrders("1267", "Sofia Rodriguez","Grandma's Edibles", datetime.datetime(2022, 9, 15, 19, 0, 0), "24.99", "pending")
order4 = pastOrders("5555", "Noah Davis", "Grandma's Edibles", datetime.datetime(2021, 7, 4, 14, 15, 0), "52.50", "past")
order5 = pastOrders("3210", "Ava Martinez", "Grandma's Edibles", datetime.datetime(2023, 2, 1, 18, 0, 0), "19.95", "past")
order6 = pastOrders("7777", "Lucas Thompson", "Grandma's Edibles", datetime.datetime(2021, 12, 10, 21, 30, 0), "31.20", "past")
order7 = pastOrders("2222", "Isabella Lewis","Grandma's Edibles", datetime.datetime(2022, 5, 3, 11, 45, 0), "16.85", "past")
order8 = pastOrders("8888", "Aiden Anderson", "Grandma's Edibles", datetime.datetime(2021, 11, 22, 19, 15, 0), "78.45", "past")
order9 = pastOrders("4444", "Mia Wright", "Grandma's Edibles", datetime.datetime(2022, 8, 8, 13, 0, 0), "42.75", "past")
order10 = pastOrders("9999", "Mason Scott", "Grandma's Edibles", datetime.datetime(2023, 1, 1, 8, 30, 0), "12.99", "past")

orders_list = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10]