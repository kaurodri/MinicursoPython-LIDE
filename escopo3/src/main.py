from api.bacen_infla import getIPCA
from utils.valor_infla import infla_mensal

def main():
    mes_infla = getIPCA()

    decimal_infla = mes_infla / 100

    infla = infla_mensal(15000, decimal_infla)
    
    print(infla)

if __name__ == "__main__":
    main()


