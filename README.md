# asyncapi-schema-pydantic

AsyncAPI (v2) specification schema as [Pydantic](https://github.com/samuelcolvin/pydantic) classes.

The naming of the classes follows the schema in 
[AsyncAPI specification](https://github.com/asyncapi/spec/blob/master/spec/asyncapi.md#schema).

## Installation

`pip install asyncapi-schema-pydantic`

## Try me

```python
from asyncapi_schema_pydantic import (  AsyncAPI,
                                        Info,
                                        ChannelItem,
                                        Operation,
                                        Message,
                                        ChannelBindings,
                                        AmqpChannelBinding,
                                        AmqpQueue,
                                        Tag )

# Construct AsyncAPI by pydantic objects
async_api = AsyncAPI(
    info=Info(
        title="Email Service",
        version="1.0.0",
        description='description'
    ),
    channels={
        "user/signedup": ChannelItem(
            description='This channel is used to exchange messages about users signing up',
            subscribe=Operation(
                summary='A user signed up.',
                message=Message(
                    name='UserSignup',
                    title='User signup',
                    summary='Action to sign a user up.',
                    description='A longer description of the message',
                    contentType='application/json',
                    tags=[
                        Tag(name='user'),
                        Tag(name='signup'),
                        Tag(name='register')
                    ]
                ),
            ),
            bindings=ChannelBindings(
                amqp=AmqpChannelBinding(
                    param_is='queue',
                    queue=AmqpQueue(
                        name='my-queue-name',
                        durable=True,
                        exclusive=True,
                        autoDelete=False,
                        vhost='/'
                    )
                )
            )
        )
    }
)

print(async_api.json(by_alias=True, exclude_none=True, indent=2))
```

Result:

```json
{
  "asyncapi": "2.3.0",
  "info": {
    "title": "Email Service",
    "version": "1.0.0",
    "description": "description"
  },
  "channels": {
    "user/signedup": {
      "description": "This channel is used to exchange messages about users signing up",
      "subscribe": {
        "summary": "A user signed up.",
        "message": {
          "contentType": "application/json",
          "name": "UserSignup",
          "title": "User signup",
          "summary": "Action to sign a user up.",
          "description": "A longer description of the message",
          "tags": [
            {
              "name": "user"
            },
            {
              "name": "signup"
            },
            {
              "name": "register"
            }
          ]
        }
      },
      "bindings": {
        "amqp": {
          "queue": {
            "name": "my-queue-name",
            "durable": true,
            "exclusive": true,
            "autoDelete": false,
            "vhost": "/"
          }
        }
      }
    }
  }
}
```

## Take advantage of Pydantic

Pydantic is a great tool, allow you to use object / dict / mixed data for for input.

The following examples give the same AsyncAPI result as above:

```python
from asyncapi_schema_pydantic import AsyncAPI, ChannelItem, Operation

# Construct AsyncAPI from dict
async_api = AsyncAPI.parse_obj({
  "asyncapi": "2.3.0",
  "info": {
    "title": "Email Service",
    "version": "1.0.0",
    "description": "description"
  },
  "channels": {
    "user/signedup": {
      "description": "This channel is used to exchange messages about users signing up",
      "subscribe": {
        "summary": "A user signed up.",
        "message": {
          "contentType": "application/json",
          "name": "UserSignup",
          "title": "User signup",
          "summary": "Action to sign a user up.",
          "description": "A longer description of the message"
        }
      }
    }
  }
})

# Construct AsyncAPI with mix of dict/object
async_api = AsyncAPI.parse_obj({
  "asyncapi": "2.3.0",
  "info": {
    "title": "Email Service",
    "version": "1.0.0",
    "description": "description"
  },
  "channels": {
    "user/signedup": ChannelItem(
            description='This channel is used to exchange messages about users signing up',
            subscribe=Operation(
                summary='A user signed up.',
                message={
                  "contentType": "application/json",
                  "name": "UserSignup",
                  "title": "User signup",
                  "summary": "Action to sign a user up.",
                  "description": "A longer description of the message"
                }
            )
        )
  }
})
```

## Load and validate an AsyncAPI specification from a YAML file

```python
from asyncapi_schema_pydantic import AsyncAPI

async_api = AsyncAPI.load_from_file("tests/data/sample.yaml")
print(async_api.json(by_alias=True, exclude_none=True, indent=2))
```

## License

[MIT License](https://github.com/albertnadal/asyncapi-schema-pydantic/blob/main/LICENSE)
