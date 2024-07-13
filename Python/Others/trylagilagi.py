

class City:
    def __init__(self, name, state):
        self.__name = name
        self.__state = state

    def __str__(self):
        return f"City: {self.__name}, State: {self.__state}"

class State:
    def __init__(self, name, city_list):
        self.__name = name
        self.__city_list = city_list

    @property
    def city_list(self):
        return self.__city_list

    @city_list.setter
    def city_list(self, city_list):
        self.__city_list = city_list

    @property
    def name(self):
        return self.__name

    def __str__(self):
        city_names = ', '.join(city.__str__() for city in self.__city_list)
        return f"State: {self.__name}, Cities: [{city_names}]"
	
# from City import City
# from State import State

state_list = []
state_list.append(State("Tamilnadu", []))
state_list.append(State("Andhra", []))
state_list.append(State("Karnataka", []))
state_list.append(State("Kerala", []))

print("Enter City Details")
city_created_list = []
choice = "Yes"
while choice.lower() == "yes":
    city_name = input("Enter city name\n")
    state_name = input("Enter state name\n")
    state_found_flag = 0
    for state in state_list:
        if state_name == state.name:
            city = City(city_name, state_name)
            state.city_list.append(city)
            city_created_list.append(city)
            state_found_flag = 1
            break
    if state_found_flag == 0:
        state = State(state_name, [])
        state_list.append(state)
        city = City(city_name, state_name)
        city_created_list.append(city)
        state.city_list.append(city)
    choice = input("Do you want to add another city? Type Yes / No\n")

print("\nCity Details\n")
for city in city_created_list:
    print(city)

print("\nState Details\n")
for state in state_list:
    print(state)


