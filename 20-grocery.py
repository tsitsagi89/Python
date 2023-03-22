grocery_list = {}
while True:
        try:
          item = input().upper()
          if item in grocery_list:
               grocery_list[item] +=1
          else:
               grocery_list[item] = 1
        except (EOFError, KeyError):
              grocery_list = sorted(grocery_list.items())
              for i, c in grocery_list:
                   print(f"{c} {i}") 
