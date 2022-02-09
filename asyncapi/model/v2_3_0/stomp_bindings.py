from pydantic import BaseModel, Extra


class StompChannelBinding(BaseModel):
    """
    This document defines how to describe STOMP-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class StompMessageBinding(BaseModel):
    """
    This document defines how to describe STOMP-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class StompOperationBinding(BaseModel):
    """
    This document defines how to describe STOMP-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class StompServerBinding(BaseModel):
    """
    This document defines how to describe STOMP-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid
