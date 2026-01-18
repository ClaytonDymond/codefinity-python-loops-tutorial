# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

outerloop = 0

while outerloop < len(travel_costs):
    innerloop = 0
    print(f"Trip {outerloop+1} expenses: ", end='')
    temp_list = []
    while innerloop < len(travel_costs[outerloop]):
        
        if travel_costs[outerloop][innerloop] > 100:
            print(travel_costs[outerloop][innerloop], end=' ')
            temp_list.append(travel_costs[outerloop][innerloop])
        else:
            print('Cheap', end=' ')
            temp_list.append('Cheap')
        innerloop += 1
    processed_expenses.append(temp_list)
    print('')
    outerloop += 1

# Testing
print('Processed Travel Expenses:', processed_expenses)