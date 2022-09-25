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
        sqnc = []
        for sqc in range(0, len(prompt)):
            if prompt[sqc] in sign_symbols.values():
                try:
                    two_chars = prompt[sqc] + prompt[sqc+1]
                except:
                    pass
                else:
                    sqnc.append(two_chars)
                match prompt:
                    case "done":
                        return sequences
                    case "":
                        continue
                    case _:
                        sequences.append(sqnc)
            else:
                print("You inputted an invalid sign, please try again!")
                return "INVALID"
def main():
    signs = input_signs()
    sign_symbols = process_signs(signs)
    print(f'You sign symbols are {sign_symbols} (Remember these)!')

    invalid = True
    while invalid:
        sequences = steal_sequences(sign_symbols)
        if sequences != "INVALID":
            Invalid = False 
            

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nHave a nice day!")