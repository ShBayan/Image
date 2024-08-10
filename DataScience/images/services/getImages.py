import requests

class GetImages:
    def get_products(self,vendor,index):
        limit=40
        skip=index*limit
        response = requests.post("http://apps.rminno.com/customApi/VendorProduct/getProduct_fast", json={
            "limit": limit,
            "condition":
                [
                                 {
                                     "fieldName": "productType",
                                     "values": [
                                         {
                                             "fieldName": "productType",
                                             "count": 20,
                                             "parentCount": 2,
                                             "filterCountParent": 2,
                                             "fieldType": "text",
                                             "value": "simple",
                                             "text": "simple",
                                             "selected": True,
                                             "exceptMode": False,
                                             "values": True
                                         }
                                     ]
                                 },
                                {
                                    "fieldName": "isActive",
                                    "values": [
                                        {
                                            "fieldName": "isActive",
                                            "fieldType": "boolean",
                                            "value": True,
                                            "selected": True,
                                            "exceptMode": False,
                                            "values": True
                                        }
                                    ]
                                },
                                 {
                                     "fieldName": "vendorUniqueId",
                                     "values": [
                                         {
                                             "fieldName": "vendorUniqueId",
                                             "count": 14118,
                                             "parentCount": 49,
                                             "filterCountParent": 32,
                                             "fieldType": "text",
                                             "value": vendor,
                                             "selected": True,
                                             "exceptMode": False,
                                             "values": True
                                         }
                                     ]
                                 }

                             ],

            "classList": [
                "583199f0fee39def05ef0ad9",
                "58319ab9fee39def05ef0adc",
                "585829303b9e419c07a4ce1c",
                "58585b933b9e419c07a4ce9e",
                "58594a37884ebefe191f053b",
                "58594a63884ebefe191f05bf",
                "58594a72884ebefe191f05c0",
                "585af020c3acc73240f894cd"
            ],
            "sort": {},
            "fieldNavigate": "",
            "panel": "admin",
            "skip": skip

        },
                            headers={
                                "token": "eyJ0b2tlbiI6ImV5SmhiR2NpT2lKU1V6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUoxYzJWeVNXUWlPaUkxWVdVM01HUmlNR1JtWWpjeVpqVXhPREkwWVRWbE5EZ2lMQ0ptYVhKemRHNWhiV1VpT2lKdVlXNWplU0lzSW14aGMzUnVZVzFsSWpvaWFtRm1ZWEpwSWl3aWNtOXNaU0k2SW5KbGRHRnBiR1Z5SWl3aVlYQndJam9pWkdGMFlXeHBibXNpTENKbGJXRnBiQ0k2SW01aGJtTjVNVEZBYzNCaGJUUXViV1VpTENKdmQyNWxja2xrSWpwdWRXeHNMQ0pwYzBGa2JXbHVJanBtWVd4elpTd2lkbVZ1Wkc5eWN5STZXM3NpZG1WdVpHOXlJam9pUVcxbGNpSXNJblpsYm1SdmNrbGtJam9pTlRnMU1UUmxNV1F4WWpCaFlqQXhaVGM1T1RoallqZG1JbjBzZXlKMlpXNWtiM0lpT2lKT2IzVnlhWE52YmlJc0luWmxibVJ2Y2tsa0lqb2lOVGcxTVRVM1ltUXpZamxsTkRFNVl6QTNZVFJqTUdZeUluMHNleUoyWlc1a2IzSWlPaUpQVUUxSUlpd2lkbVZ1Wkc5eVNXUWlPaUkxWVdGaE16VmpOMkpsTVRCaE5HWTJNVGN3WVdJeU5ETWlmU3g3SW5abGJtUnZjaUk2SWs5eWFXVnVkR0ZzSUZkbFlYWmxjbk1pTENKMlpXNWtiM0pKWkNJNklqVTROVEUxWm1ZNU0ySTVaVFF4T1dNd04yRTBZekpqWWlKOUxIc2lkbVZ1Wkc5eUlqb2lVbUZrYVdOcElpd2lkbVZ1Wkc5eVNXUWlPaUkxT0RVeE5XRXdPRE5pT1dVME1UbGpNRGRoTkdNeU5HUWlmU3g3SW5abGJtUnZjaUk2SWtGa1pYTnpieUlzSW5abGJtUnZja2xrSWpvaU5UZzBOREZrTnpNeU1XWXhOREEwWWpGa01URTFaR1V4SW4wc2V5SjJaVzVrYjNJaU9pSkVZV3g1YmlJc0luWmxibVJ2Y2tsa0lqb2lOVGcxTVRVMU1EVXpZamxsTkRFNVl6QTNZVFJqTUdJekluMWRMQ0pyWlhsSlpDSTZJalZpWVRSbU9XTTNZalV4WWpOak5HRmpOalJoTmpjMU5pSXNJa0l5UTA5M2JtVnlJam9pTldJMk9UaGtZalV6Wm1Fek5UWTVOVE00WmpVMVpEbGpJaXdpYVdGMElqb3hOVE00TlRjd09ETXlmUS5DeHZSR2hMYTN3Z2RHQzVoZk5Ia0swTXhqQWtPc3VFLVRxRm0xTmh2WjdWT1Y0MEZiSkZaWjA2TnpvMkFKU1o5akdKbFNQZTNESTlwQnVpVnFQeERmRWJpOWVzOXF1SFZYby12SndPNXYtbWk4WmM1TWNqSEFzUUZrZXVyT1daZVNuczQ3MDZlbWpfcnhFQ3B5Q2FSa2h2R0FWaENpUlpKMHhQdVhMd3hLcldldG9OTkNYMkwyQ0w0R2F4c1dmS3ZBQVd4RWpLNjVXUGZaX2c3TXZzR1JrUDNYYXllX292b0tyOXdJUm1lM05YZHJyaWptSzVTQm54a1JURWVoU0FOMjhPMkMtZWVTMnNZNXB4ekZCRXBPZUc4VUNZRFNvUVFDcS1YWXpuZXdJdlQ2bGc5WF9tNzdmTjdPak5Yb1RjeUp0c0xBUmxqYkhkd0dGMGdxbldMOHciLCJlbWFpbCI6Im5hbmN5MTFAc3BhbTQubWUiLCJhcHAiOiJkYXRhbGluayIsImtleUlkIjoiNWJhNGY5YzdiNTFiM2M0YWM2NGE2NzU2In0="})

        return response

