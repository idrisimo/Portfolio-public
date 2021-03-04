import boto3
from botocore.exceptions import ClientError


AWS_AccessKey_Id = "AWS_AccessKey_Id"
AWS_Secret_Key = "AWS_Secret_Key"




host_key = "DCBA"
host_user = "Eve"
thy_user_details = {"Juliet": {"Genre Preference": ["History"], "Release Date": "01-02-2020"},
                    "Steve": {"Genre Preference": ["Action", "Romance"], "Release Date": "02-03-2020"},
                    "Barbra": {"Genre Preference": ["Scifi", "Adventure", "Drama"], "Release Date": "03-04-2020"},
                    "James": {"Genre Preference": ["Animation"], "Release Date": "04-05-2020"},
                    "Smith": {"Genre Preference": ["Action"], "Release Date": "05-06-2020"}}
my_user_details = {"Eve": {"Genre Preference": ["Romance"], "Release Date": "10-02-2020"}}

class Party_planner(object):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=AWS_AccessKey_Id,
                              aws_secret_access_key=AWS_Secret_Key,
                              region_name="us-east-2")

    def __init__(self, host_key, host_user, **kwargs):
        self.table = self.dynamodb.Table("Voting_DB")
        self.host_key = host_key
        self.host_user = host_user
        self.user_details = kwargs.get("user_details", {})
        self.movie_list = kwargs.get("movie_list", {})

    def get_party_list(self):
        print("Getting party....")
        response = self.table.get_item(Key={'Host Key': self.host_key, "Host User": self.host_user})
        print("Party list retrieved")
        return response

    def create_party(self):
        print("Hosting party...")
        response = self.table.put_item(Item={"Host Key": self.host_key, "Host User": self.host_user})
        if str(response["ResponseMetadata"]["HTTPStatusCode"]) == "200":
            print("Party created successfully!")
            return response
        else:
            print("There was an issue...")

    def add_party_members(self):
        print("Adding party member...")
        for user, details in self.user_details.items():
            response = self.table.update_item(Key={"Host Key": self.host_key, "Host User": self.host_user},
                                              UpdateExpression=f"set #usergroup.{user}= :uservalue",
                                              ExpressionAttributeNames={"#usergroup": "Users"},
                                              ExpressionAttributeValues={":uservalue": details},
                                              ReturnValues="UPDATED_NEW",
                                              ConditionExpression=f"attribute_exists(Host Key)")
            print("Party member added!")
        '''try:
            for user, details in self.user_details.items():
                response = self.table.update_item(Key={"Host Key": self.host_key, "Host User": self.host_user},
                                             UpdateExpression=f"set #usergroup.{user}= :uservalue",
                                             ExpressionAttributeNames={"#usergroup": "Users"},
                                             ExpressionAttributeValues={":uservalue": details},
                                             ReturnValues="UPDATED_NEW",
                                                  ConditionExpression="attribute_exists(Host Key)")
                print("Party member added!")
        except ClientError as e:
            if e.response["Error"]["Code"] == "ValidationException":
                response = self.table.update_item(Key={"Host Key": self.host_key, "Host User": self.host_user},
                                             UpdateExpression=f"set #usergroup= :uservalue",
                                             ExpressionAttributeNames={"#usergroup": "Users"},
                                             ExpressionAttributeValues={":uservalue": self.user_details},
                                             ReturnValues="UPDATED_NEW")
                print(f"There was an issue: {e}")'''
        return response

    def get_movie_list(self):
        response = self.table.get_item(Key={'Host Key': self.host_key, "Host User": self.host_user})
        return response

    def store_movie_list(self):
        response = self.table.update_item(Key={"Host Key": self.host_key, "Host User": self.host_user},
                                     UpdateExpression=f"set #moviegroup= :movievalue",
                                     ExpressionAttributeNames={"#moviegroup": "Preferred Movies"},
                                     ExpressionAttributeValues={":movievalue": self.movie_list},
                                     ReturnValues="UPDATED_NEW")

        return response

'''planner = Party_planner(host_key, host_user, user_details=thy_user_details)

planner.add_party_members()

planner.get_party_list()'''
