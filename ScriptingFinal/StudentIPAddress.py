class StudentIPAddress:
    _oct1 = 0
    _oct2 = 0
    _oct3 = 0
    _oct4 = 0
    _ip = ""

    def DottedDecimalNotation(self):
        return self.__str__()

    def startingCheck(self):
        if self._oct1 == '':
            self._oct1 = 0
        if self._oct2 == '':
            self._oct2 = 0
        if self._oct3 == '':
            self._oct3 = 0
        if self._oct4 == '':
            self._oct4 = 0
        self._ip = str(self._oct1) + "." + str(self._oct2) + "." + str(self._oct3) + "." + str(self._oct4)

    def startingValidIPAddress(self, ip):
        try:
            parts = ip.split(".")
            if parts[0] == '':
                parts[0] = '0'
            if parts[1] == '':
                parts[1] = '0'
            if parts[2] == '':
                parts[2] = '0'
            if parts[3] == '':
                parts[3] = '0'
            # print(parts[0], parts[1], parts[2], parts[3])
            if len(parts) != 4:
                return False  # "invalid IP Address. It should contain exactly 4 octets."
            else:
                while len(parts) == 4:
                    self._oct1 = int(parts[0])
                    self._oct2 = int(parts[1])
                    self._oct3 = int(parts[2])
                    self._oct4 = int(parts[3])
                    if self._oct1 < 0 or self._oct1 > 255:
                        return False  # "invalid IP address"
                    elif self._oct2 > 255 or self._oct2 < 0:
                        return False  # "should not be greater than 255 or less than 0 B"
                    elif self._oct3 > 255 or self._oct3 < 0:
                        return False  # "should not be greater than 255 or less than 0 C"
                    elif self._oct4 > 255 or self._oct4 < 0:
                        return False  # "should not be greater than 255 or less than 0 D"
                    else:
                        self._ip = parts[0] + "." + parts[1] + "." + parts[2] + "." + parts[3]
                        # print(self._ip)
                        return True  # "Valid IP address ", ip
        except IndexError:
            return False

    def endingValidIPAddress(self, ip):
        try:
            parts = ip.split(".")
            if parts[0] == '':
                parts[0] = '255'
            if parts[1] == '':
                parts[1] = '255'
            if parts[2] == '':
                parts[2] = '255'
            if parts[3] == '':
                parts[3] = '255'
            if len(parts) != 4:
                return False  # "invalid IP Address. It should contain exactly 4 octets."
            else:
                while len(parts) == 4:
                    self._oct1 = int(parts[0])
                    self._oct2 = int(parts[1])
                    self._oct3 = int(parts[2])
                    self._oct4 = int(parts[3])

                    if self._oct1 < 0 or self._oct1 > 255:
                        return False  # "invalid IP address"
                    elif self._oct2 > 255 or self._oct2 < 0:
                        return False  # "should not be greater than 255 or less than 0 B"
                    elif self._oct3 > 255 or self._oct3 < 0:
                        return False  # "should not be greater than 255 or less than 0 C"
                    elif self._oct4 > 255 or self._oct4 < 0:
                        return False  # "should not be greater than 255 or less than 0 D"
                    else:
                        self._ip = parts[0] + "." + parts[1] + "." + parts[2] + "." + parts[3]
                        # print(self._ip)
                        return True  # "Valid IP address ", ip
        except IndexError:
            return False

    def NextAddress(self):
        if self._oct1 <= 254 and self._oct2 == 255 and self._oct3 == 255 and self._oct4 == 255:
            self._oct4 = 0
            self._oct3 = 0
            self._oct2 = 0
            self._oct1 += 1
        elif self._oct1 == 255 and self._oct2 == 255 and self._oct3 == 255 and self._oct4 == 255:
            self._oct4 = 256
            self._oct3 = 256
            self._oct2 = 256
            self._oct1 = 256
        elif self._oct2 <= 254 and self._oct3 == 255 and self._oct4 == 255:
            self._oct4 = 0
            self._oct3 = 0
            self._oct2 += 1
        elif self._oct2 == 255 and self._oct3 == 255 and self._oct4 == 255:
            self._oct4 = 0
            self._oct3 = 0
            self._oct2 = 0
            self._oct1 += 1
        elif self._oct3 <= 254 and self._oct4 == 255:
            self._oct4 = 0
            self._oct3 += 1
        elif self._oct3 == 255 and self._oct4 == 255:
            self._oct4 = 0
            self._oct3 = 0
            self._oct2 += 1
        elif self._oct4 <= 254:
            self._oct4 += 1

        self._ip = str(self._oct1) + "." + str(self._oct2) + "." + str(self._oct3) + "." + str(self._oct4)
        # print(self._ip)

        if self._oct4 == 256 and self._oct3 == 256 and self._oct2 == 256 and self._oct1 == 256:
            return False

        return True

    def __init__(self):
        return

    def __str__(self):
        return str(self._ip) + "\n"

    def IsSmaller(self, other):
        parts = str(other).split(".")
        other1 = int(parts[0])
        other2 = int(parts[1])
        other3 = int(parts[2])
        other4 = int(parts[3])
        if self._oct1 < other1:
            return True
        elif self._oct1 <= other1 and self._oct2 < other2:
            return True
        elif self._oct1 <= other1 and self._oct2 <= other2 and self._oct3 < other3:
            return True
        elif self._oct1 <= other1 and self._oct2 <= other2 and self._oct3 <= other3 and self._oct4 < other4:
            return True
        else:
            return False
