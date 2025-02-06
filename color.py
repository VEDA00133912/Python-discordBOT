class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'  
    
    @staticmethod
    def print_red(text):
        print(f"{Color.RED}{text}{Color.RESET}")

    @staticmethod
    def print_green(text):
        print(f"{Color.GREEN}{text}{Color.RESET}")