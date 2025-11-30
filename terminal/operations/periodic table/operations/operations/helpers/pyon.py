class pyon():
    def run(fileName):
        with open(fileName, "r") as file:
            content = file.read()
        
        content = exec("globals()['parsedDictionary'] = dict({" + content + "})")
        return globals()['parsedDictionary']