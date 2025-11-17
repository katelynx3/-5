cost_gas = 49.5

def calculated_fue_consumption (distance, gasoline_consumption):
    """расчет затраченного бензина на поездку
    args:
        distance, gasoline_consumption(float): расстояние и расход бензина на 100км
    returnes:
        float: затраченный бензин на поездку"""
    calculated_consmption_gas = distance * (gasoline_consumption / 100)
    return calculated_consmption_gas

def calculated_fue_cost (cost_gas, calculated_consmption_gas):
    """расчет стоимости бензина на поездку
      args:
          calculated_fue_consumption(func): затраченный бензин на поездку
      returnes:
          float: стоимость бензина за поедку"""
    calculated_cost_gas = calculated_fue_consumption(distance, gasoline_consumption) * cost_gas
    return calculated_cost_gas

distance, gasoline_consumption = map(float, input("введите расстояние и расход бензина на 100км через пробел").split())
print(f"""необходимо бензина {calculated_fue_consumption(distance, gasoline_consumption)}
стоимость бензина {calculated_fue_cost(cost_gas, calculated_fue_consumption)}""")
