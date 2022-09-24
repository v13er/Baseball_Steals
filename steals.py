def input_signs():
    #Makes an empty list of signs 
    signs = []

    #Gets all the signals
    signals = True
    while signals:
        prompt = input("Please input a sign (Write exit to stop)\n> ")
        prompt = prompt.lower()
        match prompt:
            case "exit":
                break
            case "":
                continue
            case _:
                signs.append(prompt)
    return signs

def process_signs(signs):
    #Assigns each motion a symbol
    sign_symbols = {}
    for sign in range(0, len(signs)):
        sign_symbols[chr(sign+65)] = signs[sign]        
    return sign_symbols

def steal_sequences(sign_symbols):
    #Gets all the sequences
    sequence = True
    sequences = []
    while sequence:
        prompt = input("Please input a sequence of symbols (Write done when finished)\n> ")
        sqnc = tuple(prompt.lower())
        match prompt:
            case "done":
                break
            case "":
                continue
            case _:
                sequences.append(sqnc)

    return sequences

def main():
    signs = input_signs()
    sign_symbols = process_signs(signs)
    print(f'You sign symbols are {sign_symbols} (Remember these)!')
    sequences = steal_sequences(sign_symbols)
    print(sequences)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nHave a nice day!")