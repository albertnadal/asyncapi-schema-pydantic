from pydantic import BaseModel, Extra


class JmsChannelBinding(BaseModel):
    """
    This document defines how to describe JMS-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class JmsMessageBinding(BaseModel):
    """
    This document defines how to describe JMS-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class JmsOperationBinding(BaseModel):
    """
    This document defines how to describe JMS-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class JmsServerBinding(BaseModel):
    """
    This document defines how to describe JMS-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid
