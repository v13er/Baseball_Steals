def input_signs():
    #Makes an empty list of signs 
    signs = []

    #Gets all the signals
    _signals = True
    while _signals:
        _prompt = input("Please input a sign (Write exit to stop)\n> ")
        _prompt = _prompt.lower()
        match _prompt:
            case "exit":
                break
            case "":
                continue
            case _:
                signs.append(_prompt)
        
    return signs

def process_signs(signs):
    #Assigns each motion a symbol
    sign_symbols = {}
    for sign in range(0, len(signs)):
        sign_symbols[chr(sign+97)] = signs[sign]        
    return sign_symbols

def steal_sequences(sign_symbols):
    #Gets all the sequences
    _sequence = True
    sequences = []
    while _sequence:
        _prompt = input("Please input a sequence of symbols (Write done when finished)\n> ")
        _prompt = _prompt.lower()
        sqnc = []
        for sqc in range(0, len(_prompt)):
            match _prompt:
                case "done":
                    return sequences
                case "":
                    continue
                case _:
                    if _prompt[sqc] in sign_symbols.keys():
                        try:
                            two_chars = _prompt[sqc] + _prompt[sqc+1]
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
        _invalid = True
        while _invalid:
            _prompt = input(f"Was {sqc} a steal?\n> ")
            _prompt = _prompt.lower()
            _key_name = ''.join(sqc)
            match _prompt:
                case "y" | "yes":
                    sequence_data[_key_name]= True
                    _invalid = False
                case "n" | "no":
                    sequence_data[_key_name] = False
                    _invalid = False

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