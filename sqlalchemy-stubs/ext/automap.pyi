from typing import Any, Optional

def classname_for_table(base, tablename, table) -> str: ...
def name_for_scalar_relationship(base, local_cls, referred_cls, constraint) -> str: ...
def name_for_collection_relationship(base, local_cls, referred_cls, constraint) -> str: ...
def generate_relationship(base, direction, return_fn, attrname, local_cls, referred_cls, **kw): ...

class AutomapBase(object):
    __abstract__: bool = ...
    classes: Any = ...
    @classmethod
    def prepare(cls, engine: Optional[Any] = ..., reflect: bool = ...,
                schema: Optional[Any] = ..., classname_for_table: Any = ...,
                collection_class: Any = ..., name_for_scalar_relationship: Any = ...,
                name_for_collection_relationship: Any = ..., generate_relationship: Any = ...) -> None: ...

def automap_base(declarative_base: Optional[Any] = ..., **kw): ...
