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
        sign_symbols[chr(sign+97)] = signs[sign]        
    return sign_symbols

def steal_sequences(sign_symbols):
    #Gets all the sequences
    sequence = True
    sequences = []
    while sequence:
        prompt = input("Please input a sequence of symbols (Write done when finished)\n> ")
        prompt = prompt.lower()
        sqnc = []
        for sqc in range(0, len(prompt)):
            match prompt:
                case "done":
                    return sequences
                case "":
                    continue
                case _:
                    if prompt[sqc] in sign_symbols.keys():
                        try:
                            two_chars = prompt[sqc] + prompt[sqc+1]
                        except:
                            pass
                        else:
                            sqnc.append(two_chars)

                    else:
                        print("You inputted an invalid sign, please try again!\n")
                        return "INVALID"
        sequences.append(sqnc)

def steal_data(sequences):
    sequence_data = {}
    for sqc in sequences:
        invalid = True
        while invalid:
            prompt = input(f"Was {sqc} a steal?\n> ")
            prompt = prompt.lower()
            key_name = ''.join(sqc)
            match prompt:
                case "y" | "yes":
                    sequence_data[key_name]= True
                    invalid = False
                case "n" | "no":
                    sequence_data[key_name] = False
                    invalid = False

    return sequence_data


def main():
    signs = input_signs()
    sign_symbols = process_signs(signs)

    print("\n#######################################################")
    print(f'You sign symbols are {sign_symbols} (Remember these)!')
    print("#######################################################")

    invalid = True
    while invalid:
        sequences = steal_sequences(sign_symbols)
        if sequences != "INVALID":
            invalid = False 

    steal_info = steal_data(sequences)
    print("\n#######################################################")
    print("If any of this info is invalid, please press ctrl + c and rerun the program.\n")
    print(f'The steal data is\n {steal_info} (confirm them)')
    print("#######################################################")

    #note to self, make temporary variable to check for keys
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nHave a nice day!")