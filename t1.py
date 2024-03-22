from marshmallow import Schema, fields, post_load, ValidationError, validates, validate
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Person:
    name: str
    email: str
    age: float = field(default=10)

def validate_age(age):
    if age < 20:
        # return False                            # 'Invalid value.' will be outputed.
        raise ValidationError("Too Young")

class PersonSchema(Schema):
    name = fields.String(validate=validate.Length(max=2))
    age = fields.Integer()                         # validate=validate_age      another option to use
    email = fields.Email(required=True)

    @validates('age')
    def validate_age(self, age):
        if age < 20:
            raise ValidationError("Too Young")

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)

try:
    schema = PersonSchema()
    p = schema.load({"name": 'ABC', "age": 10, "email": "abc@abc.com"})

    result = schema.dump(p)
    print(result)

except ValidationError as err:
    print(err)
    print(err.valid_data)

# if __name__ == "__main__":
#     p = Person("abc", 20)
#     pp = Person("a")
#     print(p)
#     print(pp)