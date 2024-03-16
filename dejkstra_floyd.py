from art import tprint## сборник приколов

def matrix_fill():## тут хуйня
    length = int(input('Введите размерность матрицы: \n'))
    print('Введите построчно элементы матрицы расстояний (через пробел, \n если непосредственной дороги нет, то 0):')
    length_matrix = []
    for i in range(0, length):
        row = input('Строка №' + str(i+1) +'\n')
        row = row.split(' ')
        row_l = []
        for j in range(0, len(row)):
            row_l.append(int(row[j]))
        length_matrix.append(row_l)
    print(length_matrix)
    return length_matrix


def path_identify(matrix, start, finish):
    temp = [finish+1]
    cur = finish
    while True: ##Тащемта тут ищем путь с конца
        if matrix[cur][1] == 0: ##[[0, 0], [4, 2], [3, 0], [8, 5], [6, 1], [7, 4], [11, 3]] так выглядит матрица, как на паре собсна
            matrix[cur][1] = start + 1 ##левое число длина маршрута, правое откуда пришли в вершину, а индекс элемента - номер вершины
            temp.append(matrix[cur][1]) ## т.е. [4,2] - картчайший маршрут от 1 до 2 вершины, попали мы в нее из 2 + 1 = 3
            break
        else:
            temp.append(matrix[cur][1] + 1)
            cur = matrix[cur][1]
    path ="" ## в итоге temp = [7, 4, 6, 5, 2, 3, 1]
    for i in range(len(temp)-1, -1, -1):
        path += str(temp[i])
        if i != 0:
            path += "->"
    return path
def dejkstra(start, finish):
    length_matrix = [[0, 5, 3, 0, 0, 0, 0], [5, 0, 1, 5, 2, 0, 0], [3, 1, 0, 7, 0, 0, 12], [0, 5, 7, 0, 3, 0, 3], [0, 2, 0, 3, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0], [0, 0, 12, 3, 0, 4, 0]]
    if (start > len(length_matrix)) or (finish > len(length_matrix)):
        print('Ошибка ввода вершин.')
        return 0
    shortest_len_matrix = [[i, 0]for i in length_matrix[start]] ##[[0, 0], [4, 2], [3, 0], [8, 5], [6, 1], [7, 4], [11, 3]] такую структуру сделать(числа офк начальные а не конечные)
    visited = [False] * len(shortest_len_matrix) ## список посещенных вершин чтоб знать когда стопать
    visited[start] = True ## стартовая сразу посещена
    while (False in visited):
        try: 
            min_range = min(shortest_len_matrix, key=lambda i: i[0] if (i[0] > 0 and visited[shortest_len_matrix.index(i)] != True) else 1000000)
            print(min_range)
            ## ищем минимальный непосещенный элемент массива который не равен нулю, возвращает офк [k, i]
            ## где k длина, i откуда пришли, изначально офк i = 0
        except:
            return shortest_len_matrix ## если не нашли то все
        cur_range = min_range[0] ## текущее расстояние до вершины которую пойдем исследовать
        cur_vertex = shortest_len_matrix.index(min_range) ## поиск индекс вершины по значению, vertex-вершина
        if cur_vertex == len(length_matrix):
            return shortest_len_matrix ##если вершина последняя то хули там исследовать уже
        cur_vertex_neighbours = length_matrix[cur_vertex] ## соседи исследуемой вершины 
        for i in range(0, len(cur_vertex_neighbours)):
            next_l = cur_vertex_neighbours[i] ##расстояние до вершины i
            if next_l != 0 and visited[i] != True: #ну нули это залупа, посещение должно быть не тру, хули
                if shortest_len_matrix[i][0] == 0 or shortest_len_matrix[i][0] > cur_range + next_l: ##если в нашем списке кратчайших расстояний можно чето улучшить
                    ## несомненно держа в уме, что, 0, где i != j это значит мы еще не нашли дорогу, а где i=j там дороги не будет никогда 
                    shortest_len_matrix[i][0] = cur_range + next_l ## если норм то меняем расстояние
                    shortest_len_matrix[i][1] = cur_vertex  ## и в соответствующей предыдущую вершину тоже
        visited[cur_vertex] = True #вершину исследовали - пошла нахуй со списка непосещенных
    return shortest_len_matrix

def steps_matrix_creation(length):# ну тут просто вроде
    matrix = []
    for i in range(0, length):
        temp = []
        for j in range(0, length):
            k = lambda j = j: j+1 if j != i else 0 #залупа просто индексацию делает с 1, там где i=j ставит 0
            temp.append(k(j))
        matrix.append(temp)
    return matrix

def matrix_print(matrix):# тут просто
    for i in range(0, len(matrix)):
        k = " "
        for j in range(0, len(matrix)):
            k += str(matrix[i][j])
            k += " "
        print(k)

def floyd(matrix):
    s_matrix = steps_matrix_creation(len(matrix)) ## матрица путей
    print('-----------------------------------------')
    k = 0
    while k != len(matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if k != i and k != j: ## столбцы и строки с индексом k вычеркиваем типа
                    if matrix[k][j] != 0 and matrix[i][k] != 0: # наличие нулей в вычеркнутых строках огорчает((
                        if (matrix[i][j] > matrix[k][j] + matrix[i][k] or matrix[i][j] == 0) and (i != j):
                            ##смотрим чтоб путь новенький короче был и i != j !!!!!
                            matrix[i][j] = matrix[k][j] + matrix[i][k] # заменяем на новый путь
                            s_matrix[i][j] = k + 1 ## перемены в матрице путей
        print('k = ', k + 1)
        print("Dk: \n")
        matrix_print(matrix) ##???????
        print("Sk: \n")
        matrix_print(s_matrix)
        k += 1
        print('-----------------------------------------')
    return(matrix, s_matrix)


def path_floyd(start, finish, s_matrix, mas):## исчадие ада
    mas = []
    if s_matrix[start-1][finish-1] != finish:
        k = mas.append([start, s_matrix[start-1][finish-1]])
        l = mas.append([[s_matrix[start-1][finish-1]], finish])## следующая строка вообще пиздец, рекурсия на поиск пути
        return [path_floyd(start, s_matrix[start-1][finish-1], s_matrix,k), path_floyd(s_matrix[start-1][finish-1], finish, s_matrix, l)]
    else:##главное что работает, сволочь
        return [start, finish]
def main():
    tprint("Dejkstra") ##кайфарики
    start = int(input('Введите начальную вершину: \n')) - 1
    finish = int(input('Введите конечную вершину: \n')) - 1
    ans = dejkstra(start=start, finish=finish)
    print(ans)
    path = path_identify(ans, start, finish)
    print("Кратчайший путь от {0} до {1} — ".format(start+1, finish+1), ans[finish][0])
    print("Итоговый путь — ", path)

    tprint("Floyd")## матрица ниже, с твоих фоток что на паре хуярили, если не впадлу можно с клавы вводить в целом
    matrix, s_matrix = floyd([[0, 5, 3, 0, 0, 0, 0], [5, 0, 1, 5, 2, 0, 0], [3, 1, 0, 7, 0, 0, 12], [0, 5, 7, 0, 3, 0, 3], [0, 2, 0, 3, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0], [0, 0, 12, 3, 0, 4, 0]])
    k = []# но мне впадлу 50000 раз вводить эту хуету
    print('Флойд путь: ', path_floyd(6, 7, s_matrix, k)) ## вывод хуевый, потому что заебался
    print('Длина пути: ', matrix[5][6])
if __name__ == "__main__":
    main()