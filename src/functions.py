# Calcula los puntos de cada jugador
def calcular_puntos(kills, assists, deaths):
    return (kills * 3) + (assists * 1) - (deaths)

# Inicializa las estadísticas
def inicializar_stats(jugadores):
    totales = {}
    for jugador in jugadores:
        totales[jugador] = {
            'kills': 0,
            'assists': 0,
            'deaths': 0,
            'puntos': 0,
            'mvps': 0
        }
    return totales

# Actualiza los totales de cada ronda y devuelve el MVP
def procesar_ronda(ronda, totales):
    ronda_puntos = {}

    for jugador, datos in ronda.items():
        kills = datos['kills']
        assists = datos['assists']
        deaths = 1 if datos['deaths'] else 0

        puntos = calcular_puntos(kills, assists, deaths)

        totales[jugador]['kills'] += kills
        totales[jugador]['assists'] += assists
        totales[jugador]['deaths'] += deaths
        totales[jugador]['puntos'] += puntos

        ronda_puntos[jugador] = puntos

    mvp = max(ronda_puntos, key=ronda_puntos.get)
    totales[mvp]['mvps'] += 1

    print(f"MVP de la ronda: {mvp}")

# Función para mostrar el ranking final ordenado por puntos
def mostrar_ranking(totales):
    print("\nRanking final:\n")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asist.':<8} {'Muertes':<8} {'MVPs':<5} {'Puntos':<6}")
    print("-" * 50)

    ranking = sorted(totales.items(), key=lambda x: x[1]['puntos'], reverse=True)

    for jugador, datos in ranking:
        print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<8} {datos['deaths']:<8} {datos['mvps']:<5} {datos['puntos']:<6}")