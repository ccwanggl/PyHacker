from pydantic import validate_call

@validate_call
def create_user(first_name:str, last_name:str, age:int) -> dict:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'age': age,
    }

user1 :dict = create_user("Corey", "Schafer", "38")
print(user1)
