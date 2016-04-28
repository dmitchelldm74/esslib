def ch(li, num):
    try:
        return li[num]
    except:
        return ""
class ESS1():
    def __init__(self, text):
        #f = open("test1.css", "r").read()
        self.f = text
    def parse(self):
        self.csstree = {}
        self.vars = {}
        self.comments = []
        word = ""
        cssname = ""
        cssproperty = ""
        varn = ""
        nomen = False
        define = False
        comment = False
        dun = False
        stopident = False
        DO_NOT_STOP = False
        stop = False
        curident = 0
        last = ""
        i = 0
        #print "hello"
        for c in self.f:
            #print word
            next = ch(self.f, i + 1)
            at = ch(self.f, i + 2)
            leading_spaces = len(word) - len(word.lstrip()) + 1
            if c == " " and next != " ":
                #print word
                stopident = False
                #print leading_spaces
            elif stopident == False and leading_spaces < curident and DO_NOT_STOP == False:
                stopident = True
            #if last == " " and c == " ":
            if c != "": # and c != " ":
                if c == ":" and last != "\\" and comment != True:
                    nomen = True
                    stop = True
                    self.csstree[word] = {}
                    cssname = word
                    word = ""
                elif stopident == True and comment != True:
                    stop = False
                    cssname = ""
                elif c == "/" and next == "*" and comment != True:
                    comment = True
                    dun = True
                elif c == "*" and next == "/":
                    comment = False
                    self.comments.append(word)
                    dun = True
                    word = ""
                elif c == "#" and next == "&" or next == "!" and comment != True:
                    comment = True
                    dun = True
                elif c == "?" and last != "\\" and comment != True:
                    comment = True
                elif c == "\n" and comment == True:
                    comment = False
                    self.comments.append(word)
                    word = ""
                elif c == "=" and last != "\\" and comment != True:# and nomen == True:
                    if define == False and nomen == True:
                        #print cssname
                        if cssname != "":
                            self.csstree[cssname][word.replace(" ", "")] = ""
                            cssproperty = word.replace(" ", "")
                            DO_NOT_STOP = True
                            word = ""
                    elif define == True and nomen == False:
                        try:
                            varn = "$" + word
                            word = ""
                            nomen = False
                        except:
                            word = word + c
                    else:
                        word = word + c
                elif c == "\n" and len(word) != 0 and word != " " and comment != True:
                    if define == False:
                        #print word
                        if word[0] == " ":
                            w = list(word)
                            w[0] = ""
                            word = "".join(w)
                        if "$" in word:
                            out = word
                            for w in self.vars:
                                out = out.replace(w, self.vars[w])
                            #print "true"
                        else:
                            out = word
                        #try:
                        self.csstree[cssname][cssproperty] = out
                        #print "error"
                        #print out, cssname
                        DO_NOT_STOP = False
                        word = ""
                    else:
                        if word[0] == " ":
                            w = list(word)
                            w[0] = ""
                            word = "".join(w)
                        self.vars[varn] = word
                        varn = ""
                        word = ""
                        define = False
                        #DO_NOT_STOP = False
                elif c == "$" and last != "\\" and cssname == "" and comment != True:
                    define = True
                    nomen = False
                elif c == "&" and last != "\\" and stop == True and comment != True:
                    word = word + ":"
                elif c == "%" and last != "\\" and stop == True and comment != True:
                    word = word + "="
                elif c == "@" and last != "\\" and stop == True and comment != True:
                    word = word + "="
                else:
                    if dun == True:
                        dun = False
                    elif c != "\n":
                        word = word + c
                #print c
            i = i + 1
        #print self.csstree
        #print self.comments
        #print self.vars
    def getItem(self, itemname):
        return self.csstree[itemname]
    def getIds(self):
        all_ids = {}
        for a in self.csstree:
            if a[0] == "#":
                all_ids[a] = self.csstree[a]
        return all_ids
    def getClasses(self):
        all_ids = {}
        for a in self.csstree:
            if a[0] == ".":
                all_ids[a] = self.csstree[a]
        return all_ids
    def getAllStartWith(self, sw):
        all_ids = {}
        for a in self.csstree:
            if a[0] == sw:
                all_ids[a] = self.csstree[a]
        return all_ids
    def get(self, name):
        if name == '__tree__':
            return self.csstree
        elif name == '__vars__':
            return self.vars
        elif name == '__comments__':
            return self.comments
        else:
            print """
Use '__tree__' to get the css tree
Use '__vars__' to get the vars
Use '__comments__' to get the comments
            """
            return ""
    def toCSS(self):
        text = ""
        for c in self.csstree:
            text = text + c + "{"
            for cc in self.csstree[c]:
                text = text + cc + ":" + self.csstree[c][cc] + ";"
            text = text + "}"
        return text
        
#ess = ESS1(open("test1.ess", "r").read())
#ess.parse()   
#open("out.css", "w").write(ess.toCSS())    
