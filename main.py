from bank import Bank
from atm import ATM

def main():
    bank = Bank()
    atm = ATM(bank)
    atm.run()

if __name__ == "__main__":
    main()