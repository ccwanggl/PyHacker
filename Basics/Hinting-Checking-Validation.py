from pydantic import validate_call
from typing import NewType

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

type User = dict[str, str | int | RGB | None]


@validate_call
def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> dict[str, str | int | None]:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "fav_color": fav_color,
    }


user1: dict = create_user("Corey", "Schafer", 38, RGB((244, 223, 11)))
print(user1)
