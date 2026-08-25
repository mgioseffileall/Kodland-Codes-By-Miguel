import time

# O ciclo externo roda no contador de horas, de 0 a 23
for hora in range(24):
# O ciclo interno roda no contador de minutos, de 0 a 59
    for minuto in range(60):
# Exibindo a hora e o minuto atuais no formato H : M
        print(hora, ":", minuto)
        time.sleep(1)

        if hora == 0 and minuto == 10:
            break
    if hora == 0 and minuto == 10:
        break
