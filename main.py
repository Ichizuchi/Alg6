data = {
  "start_time": [2 , 6 , 4 , 10 , 13 , 7],
  "finish_time": [5 , 10 , 8 , 12 , 14 , 15],
  "activity": ["Домашнее задание" , "Презентация" , "Курсовая работа" , "Тренировка по волейболу" , "Лекция по биологии" , "Тусовка"]
}

selected_activity =[]
start_position = 0
# сортировка элементов в порядке возрастания по времени завершения
tem = 0
for i in range(0 , len(data['finish_time'])):
   for j in range(0 , len(data['finish_time'])):
       if data['finish_time'][i] < data['finish_time'][j]:
           tem = data['activity'][i] , data['finish_time'][i] , data['start_time'][i]
           data['activity'][i] , data['finish_time'][i] , data['start_time'][i] = data['activity'][j] , data['finish_time'][j] , data['start_time'][j]
           data['activity'][j] , data['finish_time'][j] , data['start_time'][j] = tem

# по умолчанию первое действие добавляется в список действий, которые необходимо выбрать.

selected_activity.append(data['activity'][start_position])
for pos in range(len(data['finish_time'])):
   if data['start_time'][pos] >= data['finish_time'][start_position]:
       selected_activity.append(data['activity'][pos])
       start_position = pos

print(f"Студент может работать над следующими видами деятельности:{selected_activity}")
