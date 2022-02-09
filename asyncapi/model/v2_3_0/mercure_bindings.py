from pydantic import BaseModel, Extra


class MercureChannelBinding(BaseModel):
    """
    This document defines how to describe Mercure-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class MercureMessageBinding(BaseModel):
    """
    This document defines how to describe Mercure-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class MercureOperationBinding(BaseModel):
    """
    This document defines how to describe Mercure-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid


class MercureServerBinding(BaseModel):
    """
    This document defines how to describe Mercure-specific information on AsyncAPI.

    This object MUST NOT contain any properties. Its name is reserved for future use.
    """


    class Config:
        extra = Extra.forbid
