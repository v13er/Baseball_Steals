#Constants 
def input_signs():
    #Makes an empty list of signs 
    signs = []
    signals = True
    while signals:
        prompt = input("Please input a sign (Write exit to stop)\n> ")
        prompt = prompt.lower()
        if prompt == "exit":
            break

    return signs


def main():
    signs = input_signs()

if __name__ == '__main__':
    main()