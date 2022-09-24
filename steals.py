def input_signs():
    #Makes an empty list of signs 
    signs = []

    signals = True
    while signals:
        prompt = input("Please input a sign (Write exit to stop)\n> ")
        prompt = prompt.lower()
        #Exits if condition is met
        if prompt == "exit":
            break
        elif prompt == "":
            continue
        #Appends to signs as more are added
        else:
            signs.append(prompt)

    return signs


def main():
    signs = input_signs()
    print(signs)
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nHave a nice day!")