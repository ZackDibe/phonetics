import unittest

import phonetics


class MetaphoneTestCase(unittest.TestCase):

    def test_single_result(self):
        result = phonetics.dmetaphone(u"aubrey")
        self.assertEquals(result, ('APR', ''))

    def test_double_result(self):
        result = phonetics.dmetaphone(u"richard")
        self.assertEquals(result, ('RXRT', 'RKRT'))

    def test_general_word_list(self):
        result = phonetics.dmetaphone('Jose')
        self.assertEquals(result, ('JS', 'HS'))
        result = phonetics.dmetaphone('cambrillo')
        self.assertEquals(result, ('KMPRL', 'KMPR'))
        result = phonetics.dmetaphone('otto')
        self.assertEquals(result, ('AT', ''))
        result = phonetics.dmetaphone('aubrey')
        self.assertEquals(result, ('APR', ''))
        result = phonetics.dmetaphone('maurice')
        self.assertEquals(result, ('MRS', ''))
        result = phonetics.dmetaphone('auto')
        self.assertEquals(result, ('AT', ''))
        result = phonetics.dmetaphone('maisey')
        self.assertEquals(result, ('MS', ''))
        result = phonetics.dmetaphone('catherine')
        self.assertEquals(result, ('K0RN', 'KTRN'))
        result = phonetics.dmetaphone('geoff')
        self.assertEquals(result, ('JF', 'KF'))
        result = phonetics.dmetaphone('Chile')
        self.assertEquals(result, ('XL', ''))
        result = phonetics.dmetaphone('katherine')
        self.assertEquals(result, ('K0RN', 'KTRN'))
        result = phonetics.dmetaphone('steven')
        self.assertEquals(result, ('STFN', ''))
        result = phonetics.dmetaphone('zhang')
        self.assertEquals(result, ('JNK', ''))
        result = phonetics.dmetaphone('bob')
        self.assertEquals(result, ('PP', ''))
        result = phonetics.dmetaphone('ray')
        self.assertEquals(result, ('R', ''))
        result = phonetics.dmetaphone('Tux')
        self.assertEquals(result, ('TKS', ''))
        result = phonetics.dmetaphone('bryan')
        self.assertEquals(result, ('PRN', ''))
        result = phonetics.dmetaphone('bryce')
        self.assertEquals(result, ('PRS', ''))
        result = phonetics.dmetaphone('Rapelje')
        self.assertEquals(result, ('RPL', ''))
        result = phonetics.dmetaphone('richard')
        self.assertEquals(result, ('RXRT', 'RKRT'))
        result = phonetics.dmetaphone('solilijs')
        self.assertEquals(result, ('SLLS', ''))
        result = phonetics.dmetaphone('Dallas')
        self.assertEquals(result, ('TLS', ''))
        result = phonetics.dmetaphone('Schwein')
        self.assertEquals(result, ('XN', 'XFN'))
        result = phonetics.dmetaphone('dave')
        self.assertEquals(result, ('TF', ''))
        result = phonetics.dmetaphone('eric')
        self.assertEquals(result, ('ARK', ''))
        result = phonetics.dmetaphone('Parachute')
        self.assertEquals(result, ('PRKT', ''))
        result = phonetics.dmetaphone('brian')
        self.assertEquals(result, ('PRN', ''))
        result = phonetics.dmetaphone('randy')
        self.assertEquals(result, ('RNT', ''))
        result = phonetics.dmetaphone('Through')
        self.assertEquals(result, ('0R', 'TR'))
        result = phonetics.dmetaphone('Nowhere')
        self.assertEquals(result, ('NR', ''))
        result = phonetics.dmetaphone('heidi')
        self.assertEquals(result, ('HT', ''))
        result = phonetics.dmetaphone('Arnow')
        self.assertEquals(result, ('ARN', 'ARNF'))
        result = phonetics.dmetaphone('Thumbail')
        self.assertEquals(result, ('0MPL', 'TMPL'))

    def test_homophones(self):
        self.assertEqual(
            phonetics.dmetaphone(u"tolled"),
            phonetics.dmetaphone(u"told"))
        self.assertEqual(
            phonetics.dmetaphone(u"katherine"),
            phonetics.dmetaphone(u"catherine"))
        self.assertEqual(
            phonetics.dmetaphone(u"brian"),
            phonetics.dmetaphone(u"bryan"))

    def test_similar_names(self):
        result = phonetics.dmetaphone(u"Bartosz")
        self.assertEquals(result, ('PRTS', 'PRTX'))
        result = phonetics.dmetaphone(u"Bartosch")
        self.assertEquals(result, ('PRTX', ''))
        result = phonetics.dmetaphone(u"Bartos")
        self.assertEquals(result, ('PRTS', ''))

        result = set(phonetics.dmetaphone(u"Jablonski")).intersection(
            phonetics.dmetaphone(u"Yablonsky"))
        self.assertEquals(list(result), ['APLNSK'])
        result = set(phonetics.dmetaphone(u"Smith")).intersection(
            phonetics.dmetaphone(u"Schmidt"))
        self.assertEquals(list(result), ['XMT'])

    def test_various_german(self):
        result = phonetics.dmetaphone("ach")
        self.assertEquals(result, ("AX", "AK"))
        result = phonetics.dmetaphone("bacher")
        self.assertEquals(result, ("PKR", ""))
        result = phonetics.dmetaphone("macher")
        self.assertEquals(result, ("MKR", ""))

    def test_various_italian(self):
        result = phonetics.dmetaphone("bacci")
        self.assertEquals(result, ("PX", ""))
        result = phonetics.dmetaphone("bertucci")
        self.assertEquals(result, ("PRTX", ""))
        result = phonetics.dmetaphone("bellocchio")
        self.assertEquals(result, ("PLX", ""))
        result = phonetics.dmetaphone("bacchus")
        self.assertEquals(result, ("PKS", ""))
        result = phonetics.dmetaphone("focaccia")
        self.assertEquals(result, ("FKX", ""))
        result = phonetics.dmetaphone("chianti")
        self.assertEquals(result, ("KNT", ""))
        result = phonetics.dmetaphone("tagliaro")
        self.assertEquals(result, ("TKLR", "TLR"))
        result = phonetics.dmetaphone("biaggi")
        self.assertEquals(result, ("PJ", "PK"))

    def test_various_spanish(self):
        result = phonetics.dmetaphone("bajador")
        self.assertEquals(result, ("PJTR", "PHTR"))
        result = phonetics.dmetaphone("cabrillo")
        self.assertEquals(result, ("KPRL", "KPR"))
        result = phonetics.dmetaphone("gallegos")
        self.assertEquals(result, ("KLKS", "KKS"))
        result = phonetics.dmetaphone("San Jacinto")
        self.assertEquals(result, ("SNHSNT", ""))

    def test_various_french(self):
        result = phonetics.dmetaphone("rogier")
        self.assertEquals(result, ("RJ", "RKR"))
        result = phonetics.dmetaphone("breaux")
        self.assertEquals(result, ("PR", ""))

    def test_various_slavic(self):
        result = phonetics.dmetaphone("Wewski")
        self.assertEquals(result, ("ASK", "FFSK"))

    def test_various_chinese(self):
        result = phonetics.dmetaphone("zhao")
        self.assertEquals(result, ("J", ""))

    def test_dutch_origin(self):
        result = phonetics.dmetaphone("school")
        self.assertEquals(result, ("SKL", ""))
        result = phonetics.dmetaphone("schooner")
        self.assertEquals(result, ("SKNR", ""))
        result = phonetics.dmetaphone("schermerhorn")
        self.assertEquals(result, ("XRMRRN", "SKRMRRN"))
        result = phonetics.dmetaphone("schenker")
        self.assertEquals(result, ("XNKR", "SKNKR"))

    def test_ch_words(self):
        result = phonetics.dmetaphone("Charac")
        self.assertEquals(result, ("KRK", ""))
        result = phonetics.dmetaphone("Charis")
        self.assertEquals(result, ("KRS", ""))
        result = phonetics.dmetaphone("chord")
        self.assertEquals(result, ("KRT", ""))
        result = phonetics.dmetaphone("Chym")
        self.assertEquals(result, ("KM", ""))
        result = phonetics.dmetaphone("Chia")
        self.assertEquals(result, ("K", ""))
        result = phonetics.dmetaphone("chem")
        self.assertEquals(result, ("KM", ""))
        result = phonetics.dmetaphone("chore")
        self.assertEquals(result, ("XR", ""))
        result = phonetics.dmetaphone("orchestra")
        self.assertEquals(result, ("ARKSTR", ""))
        result = phonetics.dmetaphone("architect")
        self.assertEquals(result, ("ARKTKT", ""))
        result = phonetics.dmetaphone("orchid")
        self.assertEquals(result, ("ARKT", ""))

    def test_cc_words(self):
        result = phonetics.dmetaphone("accident")
        self.assertEquals(result, ("AKSTNT", ""))
        result = phonetics.dmetaphone("accede")
        self.assertEquals(result, ("AKST", ""))
        result = phonetics.dmetaphone("succeed")
        self.assertEquals(result, ("SKST", ""))

    def test_mc_words(self):
        result = phonetics.dmetaphone("mac caffrey")
        self.assertEquals(result, ("MKFR", ""))
        result = phonetics.dmetaphone("mac gregor")
        self.assertEquals(result, ("MKRKR", ""))
        result = phonetics.dmetaphone("mc crae")
        self.assertEquals(result, ("MKR", ""))
        result = phonetics.dmetaphone("mcclain")
        self.assertEquals(result, ("MKLN", ""))

    def test_gh_words(self):
        result = phonetics.dmetaphone("laugh")
        self.assertEquals(result, ("LF", ""))
        result = phonetics.dmetaphone("cough")
        self.assertEquals(result, ("KF", ""))
        result = phonetics.dmetaphone("rough")
        self.assertEquals(result, ("RF", ""))

    def test_g3_words(self):
        result = phonetics.dmetaphone("gya")
        self.assertEquals(result, ("K", "J"))
        result = phonetics.dmetaphone("ges")
        self.assertEquals(result, ("KS", "JS"))
        result = phonetics.dmetaphone("gep")
        self.assertEquals(result, ("KP", "JP"))
        result = phonetics.dmetaphone("geb")
        self.assertEquals(result, ("KP", "JP"))
        result = phonetics.dmetaphone("gel")
        self.assertEquals(result, ("KL", "JL"))
        result = phonetics.dmetaphone("gey")
        self.assertEquals(result, ("K", "J"))
        result = phonetics.dmetaphone("gib")
        self.assertEquals(result, ("KP", "JP"))
        result = phonetics.dmetaphone("gil")
        self.assertEquals(result, ("KL", "JL"))
        result = phonetics.dmetaphone("gin")
        self.assertEquals(result, ("KN", "JN"))
        result = phonetics.dmetaphone("gie")
        self.assertEquals(result, ("K", "J"))
        result = phonetics.dmetaphone("gei")
        self.assertEquals(result, ("K", "J"))
        result = phonetics.dmetaphone("ger")
        self.assertEquals(result, ("KR", "JR"))
        result = phonetics.dmetaphone("danger")
        self.assertEquals(result, ("TNJR", "TNKR"))
        result = phonetics.dmetaphone("manager")
        self.assertEquals(result, ("MNKR", "MNJR"))
        result = phonetics.dmetaphone("dowager")
        self.assertEquals(result, ("TKR", "TJR"))

    def test_pb_words(self):
        result = phonetics.dmetaphone("Campbell")
        self.assertEquals(result, ("KMPL", ""))
        result = phonetics.dmetaphone("raspberry")
        self.assertEquals(result, ("RSPR", ""))
        result = phonetics.dmetaphone("wright")
        self.assertEquals(result, ("RT", ""))
        result = phonetics.dmetaphone("right")
        self.assertEquals(result, ("RT", ""))
        result = phonetics.dmetaphone("left")
        self.assertEquals(result, ("LFT", ""))

    def test_th_words(self):
        result = phonetics.dmetaphone("Thomas")
        self.assertEquals(result, ("TMS", ""))
        result = phonetics.dmetaphone("Thames")
        self.assertEquals(result, ("TMS", ""))

if __name__ == '__main__':
    unittest.main()
