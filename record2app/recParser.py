import re
class Rec_parser:
    patterns={"date":r"(?P<date>\d{4}) (?P<weekday>\w{1})",
            "receiverec":r"[+]{1}(?P<item>.*) (?P<amount>\d+)",
            "transferrec":r"[~]{1}(?P<item>.*) (?P<amount>\d+)",
            "payrec":r"(?P<item>.*) (?P<amount>\d+)",
            "unknown":r"^.+$",
            "empty":r"(^$)",
            }
    recweekday=""
    recdate=""

    @classmethod
    def rec_match(self, rec_line):
        for pat in self.patterns:
            if re.match(self.patterns[pat], rec_line):
                # print("pat is:"+pat)
                return getattr(self,pat)(pat, self.patterns[pat], rec_line)
                # break

    @classmethod
    def empty(self, pat_name, pat, rec_line):
        # print("empty line:"+rec_line)
        # print()
        return {"pat_name":pat_name, "pat":pat}

    @classmethod
    def unknown(self, pat_name, pat, rec_line):
        # print("unknown line:"+rec_line)
        return {"pat_name":pat_name, "pat":pat}

    @classmethod
    def date(self, pat_name, pat, rec_line):
        pars = re.match(pat, rec_line)
        self.recdate=pars.group('date')
        self.recweekday=pars.group('weekday')
        # print("in this rec, date is %s and weekday is %s" 
                # %(self.recdate, self.recweekday))
        return {"pat_name":pat_name, "pat":pat, 'data':self.recdate, 'weekday':self.recweekday}

    @classmethod
    def payrec(self, pat_name, pat, rec_line):
        result = re.match(pat,rec_line)
        # print("%s cost item is %s, amount is %d" 
                # %(self.recdate,result.group('item'),int(result.group('amount'))))
        return {"pat_name":pat_name, 'pat':pat, 'item':result.group('item'), 'amount':result.group('amount')}

    @classmethod
    def receiverec(self, pat_name, pat, rec_line):
        result = re.match(pat,rec_line)
        # print("receive item is %s, amount is %d"
                # %(result.group('item'),int(result.group('amount'))))
        return {"pat_name":pat_name, 'pat':pat, 'item':result.group('item'), 'amount':result.group('amount')}

    @classmethod
    def transferrec(self, pat_name, pat, rec_line):
        result = re.match(pat,rec_line)
        print("transfer item is %s, amount is %d"
                %(result.group('item'),int(result.group('amount'))))

