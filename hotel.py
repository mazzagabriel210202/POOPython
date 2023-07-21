from datetime import datetime

class Reserva:
    def __init__(self, cpf, numero_hotel, checkin, checkout):
        self.cpf = cpf
        self.numero_hotel = numero_hotel
        self.checkin = checkin
        self.checkout = checkout

    @staticmethod
    def verificar_data_valida(data_str):
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @classmethod
    def pedir_data(cls, mensagem):
        while True:
            data_str = input(mensagem)
            if cls.verificar_data_valida(data_str):
                return datetime.strptime(data_str, "%d/%m/%Y")
            else:
                print("Data inválida. Tente novamente (formato: dd/mm/aaaa).")

    @classmethod
    def criar_reserva(cls):
        cpf = input("Digite o CPF da pessoa: ")
        numero_hotel = int(input("Digite o número do hotel: "))

        while True:
            try:
                checkin = cls.pedir_data("Digite a data de check-in (formato: dd/mm/aaaa): ")
                checkout = cls.pedir_data("Digite a data de check-out (formato: dd/mm/aaaa): ")

                if checkout <= checkin:
                    print("Erro: A data de check-out deve ser posterior à data de check-in.")
                else:
                    return cls(cpf, numero_hotel, checkin, checkout)
            except ValueError:
                print("Erro: Data inválida. Tente novamente.")

    def __str__(self):
        return f"CPF: {self.cpf}\nNúmero do hotel: {self.numero_hotel}\nData de check-in: {self.checkin.strftime('%d/%m/%Y')}\nData de check-out: {self.checkout.strftime('%d/%m/%Y')}"

def main():
    reserva = Reserva.criar_reserva()

    print("\nInformações registradas:")
    print(reserva)

if __name__ == "__main__":
    main()