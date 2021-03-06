import unittest
from patent_claim_text_converter import *

sample_claim_text = "1. A product tag system, comprising:\
an RFID tag adapted for attachment to a product;\
at least one data store in said tag for bar code information relating to said product;\
a tag detacher for removing said tag from said product at a point of sale;\
an RFID tag reader for retrieving said bar code information from said tag when said tag is placed in said tag detacher; and,\
a display for presenting said bar code information in a form which can be scanned by a conventional bar code scanner, said display associated with said tag detacher and said RFID tag reader at said point of sale.\
2. The system of claim 1, wherein said tag further comprises a detectable EAS element.\
3. The system of claim 1, wherein said tag detacher is inoperable for detaching said tag until said bar code information has been read.\
4. The system of claim 1, wherein said tag further comprises a further data store for further product information.\
5. The system of claim 1, further including a display for displaying human readable information related to said product.\
6. The system of claim 1, wherein said tag detacher is inoperable for detaching said tag until said tag detacher receives a confirmation signal that said bar code information has been successfully read by said bar code scanner.\
7. The system of claim 1, wherein said tag detacher comprises means for receiving a confirmation signal that said bar code information has been successfully read by said bar code scanner, said tag being detached responsive to said confirmation signal.\
8. The system of claim 1, wherein said tag detacher and said RFID tag reader are integrated in a single housing.\
9. The system of claim 1, wherein said tag detacher and said display are integrated in a single housing.\
10. The system of claim 9, wherein said single housing is adapted for mounting in a fixed position with respect to said conventional bar code scanner.\
11. The system of claim 1, wherein said display and said RFID tag reader are integrated in a single housing.\
12. The system of claim 11, wherein said single housing is adapted for mounting in a fixed position with respect to said conventional bar code scanner.\
13. The system of claim 11, wherein said single housing is adapted for mounting in a fixed position with respect to said conventional bar code scanner.\
14. The system of claim 11, wherein said tag detacher, said RFID tag reader and said display are integrated in a single housing.\
15. The system of claim 1, wherein said display is adapted for mounting in a fixed position with respect to said conventional bar code scanner.\
16. The system of claim 1, further comprising an RFID writer.\
17. The system of claim 16, wherein said tag comprises a further data store for receiving from said RFID writer information regarding said sale of said product, whereby said product sale information is available for subsequent use.\
18. A product tag system, comprising:\
an RFID tag adapted for attachment to a product;\
at least one data store in said tag for bar code information relating to said product;\
a tag detacher for removing said tag from said product at a point of sale;\
an RFID tag reader for retrieving said bar code information from said tag when said tag is placed in said tag detacher;\
a display for presenting said bat code information in a form which can be scanned by a conventional bar code scanner;\
a hand-held RFID reader adapted for attachment to a hand-held bar code scanner;\
a display on said hand-held RFID reader, said display being in an aligned position when said reader and said scanner are attached for presenting said bar code information in a form which can be scanned by said hand-held bar code scanner; and,\
a tag detacher remote from said reader for detaching said tag after said displayed bar code is scanned.\
19. The system of claim 18, wherein said tag detacher automatically detaches said tag responsive to a signal transmitted by said reader.\
20. A method for monitoring products, comprising the steps of:\
attaching an RFID tag to a product;\
writing bar code information onto said tag;\
retrieving said bar code information from said tag at a point of sale; and,\
displaying, at said point of sale, said bar code information in a form which can be scanned by a conventional bar code scanner at said point of sale.\
21. The method of claim 20, further comprising the step of activating a detectable EAS element in said tag prior to said retrieving step.\
22. The method of claim 21, wherein said attaching, writing and activating steps can occur in any order.\
23. The method of claim 20, further comprising the step of detaching said tag from said product.\
24. The method of claim 23, comprising the step of performing said retrieving, displaying and detaching steps with components disposed in a single housing.\
25. The method of claim 24, comprising the step of disposing said housing in a fixed position relative to said conventional bar code scanner.\
26. The method of claim 20, wherein said attaching and writing steps can occur in any order.\
27. The method of claim 20, further comprising the step of displaying said bar code information from a position fixed relative to said conventional bar code scanner.\
28. The method of claim 20, further comprising displaying said bar code information in human readable form.\
29. The method of claim 20, further comprising the step of writing to said tag, at said point of sale, information regarding said sale of said product, whereby said product sale information is available for subsequent use."

sample_claim_text_1 = "1. A product tag system, comprising:\
an RFID tag adapted for attachment to a product;\
at least one data store in said tag for bar code information relating to said product;\
a tag detacher for removing said tag from said product at a point of sale;\
an RFID tag reader for retrieving said bar code information from said tag when said tag is placed in said tag detacher; and,\
a display for presenting said bar code information in a form which can be scanned by a conventional bar code scanner, said display associated with said tag detacher and said RFID tag reader at said point of sale.\
2. The system of claim 1, wherein said tag further comprises a detectable EAS element."


class PatentClaimTextConverterTest(unittest.TestCase):

    def test_create_claim_marker(self):
        self.assertEqual(create_claim_marker(1), '1.')
        self.assertEqual(create_claim_marker(25), '25.')

    def test_find_claim_numbers(self):
        sample_claim_numbers = find_claim_numbers(sample_claim_text)
        self.assertEqual(sample_claim_numbers[0], 0)
        self.assertEqual(len(sample_claim_numbers), 29)

    def test_json_conversion(self):
        self.assertEqual(json.loads(convert_claim_text(sample_claim_text_1)), json.loads(
            '{\
              "1": [\
                "A product tag system, comprising:an RFID tag adapted for attachment to a product",\
                "at least one data store in said tag for bar code information relating to said product",\
                "a tag detacher for removing said tag from said product at a point of sale",\
                "an RFID tag reader for retrieving said bar code information from said tag when said tag is placed in said tag detacher",\
                " and,a display for presenting said bar code information in a form which can be scanned by a conventional bar code scanner, said display associated with said tag detacher and said RFID tag reader at said point of sale."\
              ],\
              "2": [\
                "The system of claim 1, wherein said tag further comprises a detectable EAS element."\
              ]\
            }'
        ))
