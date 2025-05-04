'''
A variation of the standard backpack problem with an additional parameter - 
the ability to elastically stretch the backpack depending 
on the fragility of the items.
The solution is based on sorting objects from the strongest to the most 
fragile objects. The strongest object describes the maximum possible stretch
of the backpack and giving a more fragile object there is 100% confidence
that the previous object will not break.
'''
amount_tools, standart_capacity = map(int, input().split())
tools_inf = [0] * amount_tools
for i in range(amount_tools):
    tools_inf[i] = tuple(map(int, input().split())) + (i,)
tools_inf.sort(key=lambda x: x[2], reverse=True)
min_capacity = tools_inf[-1][2]
if standart_capacity + min_capacity >= 10**5:
    alt_MX = 0
    str_ans = ''
    for tool in tools_inf:
        alt_MX += tool[1]
    for i in range(1, amount_tools+1):
        str_ans += str(i) + ' '
    print(amount_tools, alt_MX)
    print(str_ans.strip())

else:
    lst_max_price = [[-1] * (10**5 + 1)]
    lst_max_price[0][0] = (0, 0)
    all_items_price = 0
    all_items_ind = []
    for tool in range(amount_tools):
        if tools_inf[tool][2] >= 10**5:
            limit = 10**5 - tools_inf[tool][0]
            all_items_price += tools_inf[tool][1]
            all_items_ind.append(tools_inf[tool][3])
        else:
            limit = standart_capacity + tools_inf[tool][2] - tools_inf[tool][0]
        for j in range(limit, -1, -1):
            if lst_max_price[tool][j] != -1:
                if lst_max_price[tool][j+tools_inf[tool][0]] == -1:
                    lst_max_price[tool][j+tools_inf[tool][0]] =\
                    (lst_max_price[tool][j][0] + tools_inf[tool][1], tool)
                else:
                    if lst_max_price[tool][j][0] + tools_inf[tool][1] >\
                        lst_max_price[tool][j+tools_inf[tool][0]][0]:
                        lst_max_price[tool][j+tools_inf[tool][0]] =\
                        (lst_max_price[tool][j][0] + tools_inf[tool][1], tool)
        if tool != amount_tools-1:
            lst_max_price.append(lst_max_price[tool].copy())

    MX = (0, 0)
    WEIGHT = 0
    for weight in range(len(lst_max_price[-1])):
        if lst_max_price[-1][weight] != -1:
            if MX[0] < lst_max_price[-1][weight][0]:
                MX = lst_max_price[-1][weight]
                WEIGHT = weight
    if MX == (0, 0):
        print(0, 0)
        print('')
    elif MX[0] < all_items_price:
        print(len(all_items_ind, all_items_price))
        print(*all_items_ind)
    else:
        ans = []
        TOOL = MX[1]
        ans.append(tools_inf[TOOL][3] + 1)
        WEIGHT -= tools_inf[TOOL][0]
        while WEIGHT > 0:
            TOOL = lst_max_price[TOOL - 1][WEIGHT][1]
            ans.append(tools_inf[TOOL][3] + 1)
            WEIGHT -= tools_inf[TOOL][0]

        print(len(ans), MX[0])
        print(*ans) 
