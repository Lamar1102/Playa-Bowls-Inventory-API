from config import rutherford_api_token,watchung_api_token,newark_api_token,uc_api_token,hoboken_api_token,elizabeth_api_token,mid_dictionary
import requests
import datetime
from datetime import timedelta



class OrderRequest:
    def __init__(self):

        self.today = datetime.date.today()
        self.yesterday = self.today - timedelta(days=1)

        self.newark_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                               self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["newark_mid"],
                               newark_api_token)
        self.rutherford_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                               self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["rutherford_mid"],
                               rutherford_api_token)
        self.watchung_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                               self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["watchung_mid"],
                               watchung_api_token)
        self.uc_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                               self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["uc_mid"],
                               uc_api_token)
        self.hoboken_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                               self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["hoboken_mid"],
                               hoboken_api_token)
        self.elizabeth_report = self.sales_request(self.date_to_timestamp(f'{self.yesterday} - 00:00:00'),
                            self.date_to_timestamp(f'{self.yesterday} - 23:59:59'), mid_dictionary["elizabteh_mid"],
                               elizabeth_api_token)

    def date_to_timestamp(self,date):
        date = datetime.datetime.strptime(date, "%Y-%m-%d - %H:%M:%S")
        date = datetime.datetime.timestamp(date)
        # print(round(date*1000))
        return round(date * 1000)


    def sales_request(self,time, time2, mid, token):
        header = {
            "accept": "application/json",
            "authorization": f"Bearer {token}"
        }
        params = {
            "limit": "1000",
        }

        inventory_sold = {

        }
        mod_dict = {

        }

        response = requests.get(
            url=f"https://api.clover.com/v3/merchants/{mid}/orders?filter=clientCreatedTime>={time}&filter=clientCreatedTime<={time2}&expand=discounts%2ClineItems.discounts%2Cpayments%2ClineItems.modifications",
            params=params, headers=header)

        data = response.json()
        data2 = response.text
        # print(data2)


        data_elements = data["elements"]



        for index in range(len(data_elements)):
            order = data_elements[index]
            # print(index)

            for i in range(len(order["lineItems"]["elements"])):

                item = order["lineItems"]["elements"][i]["name"]
                item = item.replace(" TPD","")
                item = item.replace("*","")
                item = item.replace("Bowl ","Bowl")

                if item in inventory_sold:
                    inventory_sold[item] += 1
                else:
                    inventory_sold[item] = 1


                try:
                    for ind in range(len(order["lineItems"]["elements"][i]["modifications"]["elements"])):

                        item_modification = order["lineItems"]["elements"][i]["modifications"]["elements"][ind]["name"]
                        item_modification = item_modification.replace("(or Extra) ","")
                        item_modification=item_modification.replace("or Extra ","")
                        item_modification=item_modification.replace("Strawberries","Strawberry")
                        item_modification=item_modification.replace("Substitute","Sub")
                        item_modification = item_modification.strip()

                        if item_modification in mod_dict:
                            mod_dict[item_modification] += 1
                        else:
                            mod_dict[item_modification] = 1
                except KeyError:
                    pass

        return [inventory_sold,mod_dict]

