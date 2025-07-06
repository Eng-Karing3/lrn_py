class SecureNote:

    def __init__(self):
        self.__note = ""

    def write_note(self, new_note):
        self.__note = new_note

    def read_note(self, password):
        if password == "secret123":
            return self.__note
        else:
            return "Access denied!"

note1 = SecureNote()

note1.write_note("This is top secret.")
print(note1.read_note("wrongpass"))      
print(note1.read_note("secret123"))     