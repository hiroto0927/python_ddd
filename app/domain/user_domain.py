class UserDomain:
    __name: str
    __age: int

    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("name must be str")

        if not isinstance(age, int):
            raise TypeError("age must be int")

        if age < 0:
            raise ValueError("age must be greater than or equal to 0")

        if len(name) == 0:
            raise ValueError("name must be greater than or equal to 1")

        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be str")

        if len(name) == 0:
            raise ValueError("name must be greater than or equal to 1")

        self.__name = name

    @age.setter
    def age(self, age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("age must be int")

        if age < 0:
            raise ValueError("age must be greater than or equal to 1")
        self.__age = age
