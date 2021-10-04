# функция поиска маршрутов
from trains.models import Train


def dfs_paths(graph, start, goal):
    """
    Функция поиска всех возможных маршрутов из одного гороа в другой.
    Вариант посещения одного и того же города не рассматривается.
    Реализация с помошью генератора, чтобы сразу определить хотя бы один маршрут.
    :param graph: непосредственно qs
    :param start: from_city город откуда мы хотим выехать
    :param goal: to_city город куда попасть
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('Маршрута, удовлетворяющего условиям не существует')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрут, через указанные города не найден')

    return context
