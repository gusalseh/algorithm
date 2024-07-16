def solution(routes):
    # routes.sort()
    routes.sort(key=lambda x: x[1])
    
    camera_position = routes[0][1]
    camera_count = 1
    
    for route in routes:
        if route[0] > camera_position:
            camera_count += 1
            camera_position = route[1]
    
    return camera_count