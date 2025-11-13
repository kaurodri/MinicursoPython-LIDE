from api.apibacen import getSelic
from utils.calculo_selic import calcular_rendimento_selic

def main():
    resultadoAPI = getSelic()
    selic = resultadoAPI / 100

    resultado = calcular_rendimento_selic(16000, selic, 30)

    print(resultado)

if __name__ == "__main__":
    main()


