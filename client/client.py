
class Client:
    COMMANDS = {}

    @classmethod
    def command(cls, command):
        cls.COMMANDS[command.__name__] = command
        return command

    def __init__(self, communicator, identity, name, ip, port):
        self._name = name
        base = communicator.stringToProxy(f"{identity}/{name}:tcp -h {ip} -p {port} -z : udp -h {ip} -p {port} -z")
        self._stub = self.get_stub(base)

    def interact(self):
        while True:
            print(f'{self._name}> ', end='')
            try:
                command_name = input()
            except KeyboardInterrupt:
                break
            if command_name in self.COMMANDS.keys():
                self.COMMANDS[command_name](self)
            elif command_name == 'exit':
                return
            else:
                print('Invalid command, use help for commands list')


@Client.command
def help(self):
    print(f"Available commands: {', '. join(self.COMMANDS)}, exit")

