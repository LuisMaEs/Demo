def funcion(ciudad):
    import swowpy
    if ciudad.pressure()<990:
        A="Aviso de tormenta"
    elif ciudad.current_weather("Description")=="stormy" or ciudad.current_weather("Description")=="storm":
        A="Aviso de tormenta"
    else:
        A="No hay avisos"
    return A

    